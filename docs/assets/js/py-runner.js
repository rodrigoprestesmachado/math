(function () {
  let pyodide = null;
  let pyodideReady = false;
  let pyodideLoading = false;

  const loadingEl = document.createElement('div');
  loadingEl.className = 'py-loading';
  loadingEl.textContent = '⏳ Carregando Python (Pyodide)… primeira execução pode levar ~30s';
  document.body.appendChild(loadingEl);

  async function initPyodide() {
    if (pyodideReady) return pyodide;
    if (pyodideLoading) {
      while (!pyodideReady) await new Promise(r => setTimeout(r, 200));
      return pyodide;
    }
    pyodideLoading = true;
    loadingEl.classList.add('visible');

    pyodide = await loadPyodide();
    await pyodide.loadPackage(['micropip', 'numpy', 'pandas', 'matplotlib', 'scipy', 'statsmodels', 'scikit-learn']);

    const micropip = pyodide.pyimport('micropip');
    try {
      await micropip.install('pingouin');
    } catch (e) {
      console.warn('pingouin install warning:', e);
    }

    await pyodide.runPythonAsync(`
import sys, io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class _OutCapture(io.StringIO):
    def write(self, s):
        if s.strip():
            super().write(s)
        return len(s)

_stdout = _OutCapture()
_stderr = _OutCapture()
sys.stdout = _stdout
sys.stderr = _stderr
_figures = []

def _capture_show(*args, **kwargs):
    fig = plt.gcf()
    if fig.get_axes():
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
        import base64
        _figures.append(base64.b64encode(buf.getvalue()).decode())
        plt.close(fig)
plt.show = _capture_show

def _reset_capture():
    global _stdout, _stderr, _figures
    _stdout = _OutCapture()
    _stderr = _OutCapture()
    sys.stdout = _stdout
    sys.stderr = _stderr
    _figures = []

def _get_output():
  out = _stdout.getvalue()
  err = _stderr.getvalue()
  figs = list(_figures)
  _reset_capture()
  return out, err, figs
`);

    pyodideReady = true;
    pyodideLoading = false;
    loadingEl.classList.remove('visible');
    return pyodide;
  }

  async function runCode(btn) {
    const runner = btn.closest('.python-runner');
    const code = runner.querySelector('.code-input').value;
    const output = runner.querySelector('.code-output');
    btn.disabled = true;
    output.classList.add('visible');
    output.classList.remove('error');
    output.textContent = 'Executando…';

    try {
      const py = await initPyodide();
      await py.runPythonAsync('_reset_capture()');
      await py.runPythonAsync(code);
      const result = await py.runPythonAsync('_get_output()');
      const [stdout, stderr, figures] = result.toJs();

      let html = '';
      if (stdout) html += escapeHtml(stdout);
      if (stderr) html += (html ? '\n' : '') + escapeHtml(stderr);
      if (!html && figures.length === 0) html = '(sem saída)';

      output.innerHTML = html;
      figures.forEach(b64 => {
        const img = document.createElement('img');
        img.src = 'data:image/png;base64,' + b64;
        img.alt = 'Gráfico matplotlib';
        output.appendChild(img);
      });
    } catch (err) {
      output.classList.add('error');
      output.textContent = String(err);
    } finally {
      btn.disabled = false;
    }
  }

  function escapeHtml(text) {
    return text
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;');
  }

  window.runPythonCode = runCode;

  // Handles both cases: script runs before or after DOMContentLoaded
  function attachHandlers() {
    document.querySelectorAll('.python-runner .run-btn').forEach(btn => {
      btn.addEventListener('click', () => runCode(btn));
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachHandlers);
  } else {
    attachHandlers();
  }
})();
