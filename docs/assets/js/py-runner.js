(function () {
  'use strict';

  let pyodide        = null;
  let pyodideReady   = false;
  let pyodideLoading = false;

  // Toast de progresso
  const loadingEl = document.createElement('div');
  loadingEl.className = 'py-loading';
  loadingEl.textContent = '⏳ Carregando Python (Pyodide)… ~30 s na primeira vez';
  document.body.appendChild(loadingEl);

  // Carrega o script do Pyodide CDN apenas quando o usuário clica Executar
  function loadPyodideScript() {
    if (window.loadPyodide) return Promise.resolve();
    return new Promise(function (resolve, reject) {
      var s  = document.createElement('script');
      s.src  = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js';
      s.onload  = resolve;
      s.onerror = function () { reject(new Error('Falha ao carregar Pyodide CDN')); };
      document.head.appendChild(s);
    });
  }

  async function initPyodide() {
    if (pyodideReady) return pyodide;
    if (pyodideLoading) {
      while (!pyodideReady) {
        await new Promise(function (r) { setTimeout(r, 200); });
      }
      return pyodide;
    }
    pyodideLoading = true;
    loadingEl.classList.add('visible');

    await loadPyodideScript();
    pyodide = await window.loadPyodide();
    await pyodide.loadPackage([
      'micropip', 'numpy', 'pandas',
      'matplotlib', 'scipy', 'statsmodels', 'scikit-learn'
    ]);

    var micropip = pyodide.pyimport('micropip');
    try {
      // Instala dependências puras do pingouin primeiro, depois o pingouin
      await micropip.install(['tabulate', 'pandas_flavor', 'pingouin']);
    } catch (e) { console.warn('pingouin install warning:', e); }

    await pyodide.runPythonAsync(`
import sys, io, warnings, os
warnings.filterwarnings('ignore', category=DeprecationWarning)
warnings.filterwarnings('ignore', category=FutureWarning)
# Desativa o update-check do pingouin (faz requisição de rede que falha no browser)
os.environ['PINGOUIN_DISABLE_UPDATE_CHECK'] = '1'
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class _Capture(io.StringIO):
    def write(self, s):
        super().write(s)
        return len(s)

_stdout = _Capture()
_stderr = _Capture()
sys.stdout = _stdout
sys.stderr = _stderr
_figures  = []

def _capture_show(*a, **kw):
    fig = plt.gcf()
    if fig.get_axes():
        buf = io.BytesIO()
        fig.savefig(buf, format='png', bbox_inches='tight', facecolor='white')
        import base64
        _figures.append(base64.b64encode(buf.getvalue()).decode())
        plt.close(fig)

plt.show = _capture_show

def _reset():
    global _stdout, _stderr, _figures
    _stdout = _Capture()
    _stderr = _Capture()
    sys.stdout = _stdout
    sys.stderr = _stderr
    _figures  = []

def _get_output():
    out  = _stdout.getvalue()
    err  = _stderr.getvalue()
    figs = list(_figures)
    _reset()
    return out, err, figs
`);

    pyodideReady   = true;
    pyodideLoading = false;
    loadingEl.classList.remove('visible');
    return pyodide;
  }

  async function runCode(btn) {
    var runner = btn.closest('.python-runner');
    var ta     = runner.querySelector('.code-input');
    var output = runner.querySelector('.code-output');
    var code   = ta.value;

    btn.disabled = true;
    output.classList.add('visible');
    output.classList.remove('error');
    output.textContent = 'Executando…';

    try {
      var py = await initPyodide();
      await py.runPythonAsync('_reset()');
      await py.runPythonAsync(code);
      var result  = await py.runPythonAsync('_get_output()');
      var parts   = result.toJs();
      var stdout  = parts[0];
      var stderr  = parts[1];
      var figures = parts[2];

      var html = '';
      if (stdout) html += esc(stdout);
      if (stderr) html += (html ? '\n' : '') + esc(stderr);
      if (!html && figures.length === 0) html = '(sem saída)';

      output.innerHTML = html;
      figures.forEach(function (b64) {
        var img = document.createElement('img');
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

  function esc(t) {
    return t.replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
  }

  // Decodifica base64 UTF-8 → string JS (suporta acentos, ×, etc.)
  function decodeB64(str) {
    try {
      var bytes = Uint8Array.from(atob(str), function (c) { return c.charCodeAt(0); });
      return new TextDecoder().decode(bytes);
    } catch (e) {
      // fallback para navegadores muito antigos
      return decodeURIComponent(escape(atob(str)));
    }
  }

  function attachHandlers() {
    document.querySelectorAll('.python-runner').forEach(function (runner) {
      var ta  = runner.querySelector('.code-input');
      var btn = runner.querySelector('.run-btn');

      // O código está em base64 no data-code — decodifica e popula o textarea
      if (ta && runner.hasAttribute('data-code')) {
        ta.value = decodeB64(runner.getAttribute('data-code'));
        runner.removeAttribute('data-code');
      }

      if (btn) {
        btn.addEventListener('click', function () { runCode(btn); });
      }
    });
  }

  // Funciona quando o script carrega via <head defer> (readyState = 'interactive')
  // ou quando é injetado no body (readyState = 'complete')
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', attachHandlers);
  } else {
    attachHandlers();
  }
})();
