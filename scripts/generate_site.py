#!/usr/bin/env python3
"""Gera páginas de conteúdo, slides e arquivos Jekyll para math.rpmhub.dev."""

from pathlib import Path
import html
import sys

sys.path.insert(0, str(Path(__file__).parent))
from topics import TOPICS, BLOCOS

DOCS = Path(__file__).resolve().parent.parent / "docs"
ASSETS = DOCS / "assets"


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def ul_items(items: list[str]) -> str:
    return "<ul>\n" + "\n".join(f"        <li>{item}</li>" for item in items) + "\n      </ul>"


def ref_list(refs: list[tuple]) -> str:
    lines = []
    for tag, text in refs:
        lines.append(f'        <li><span class="ref-tag">{esc(tag)}</span>{text}</li>')
    return "<ul class=\"ref-list\">\n" + "\n".join(lines) + "\n      </ul>"


def python_runner(code: str) -> str:
    return f"""      <div class="python-runner">
        <div class="toolbar">
          <span>🐍 Python — executável no navegador (Pyodide)</span>
          <button type="button" class="run-btn">▶ Executar</button>
        </div>
        <textarea class="code-input" spellcheck="false">{esc(code)}</textarea>
        <pre class="code-output"></pre>
      </div>"""


def content_html(topic: dict) -> str:
    bloco = BLOCOS[topic["bloco"]]
    tip = ""
    if topic.get("tip"):
        tip = f'      <div class="tip">{topic["tip"]}</div>\n'

    py_ctx = ""
    if topic.get("python_context"):
        py_ctx = f'      <p>{topic["python_context"]}</p>\n'

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Enc. {topic['num']} — {esc(topic['title'])}</title>
<link rel="stylesheet" href="../assets/css/math.css">
</head>
<body>

<header>
  <h1>Enc. {topic['num']} — {topic['title']}</h1>
  <p>{topic['subtitle']}</p>
  <a class="back-link" href="../materiais.html">← Voltar aos materiais</a>
</header>

<div class="bloco-title {bloco['class']}">{bloco['emoji']} Bloco {topic['bloco']} — {bloco['name']}</div>

<div class="card">
  <div class="card-header">
    <div class="enc-num">{topic['num']}</div>
    <div><h2>{topic['title']}</h2><p>{topic['subtitle']}</p></div>
  </div>

  <div class="section">
    <div class="section-label lbl-meta">🍊 Metáfora</div>
    <div class="metaphor">
      <span class="metaphor-label">{topic.get('metaphor_label', 'Imagine isso…')}</span>
      {topic['metaphor']}
    </div>
  </div>

  <div class="section">
    <div class="section-label lbl-serve">🎯 Para que serve</div>
    {''.join(f'<p>{p}</p>' for p in topic['serve'])}
  </div>

  <div class="section">
    <div class="section-label lbl-quando">📋 Quando usar — e quando NÃO usar</div>
    {ul_items(topic['quando'])}
{tip}  </div>

  <div class="section">
    <div class="section-label lbl-python">🐍 Exemplo Python</div>
{py_ctx}{python_runner(topic['python_code'])}
  </div>

  <div class="section">
    <div class="section-label lbl-ref">📚 Referências</div>
    {ref_list(topic['refs'])}
  </div>
</div>

<footer class="page-footer">
  <a href="slides/index.html">📊 Ver slides</a> ·
  <a href="https://math.rpmhub.dev">math.rpmhub.dev</a> ·
  <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>
</footer>

<script src="https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js"></script>
<script src="../assets/js/py-runner.js"></script>
</body>
</html>
"""


def slides_md(topic: dict) -> str:
    bloco = BLOCOS[topic["bloco"]]
    quando = "\n".join(f"- {item}" for item in topic["quando"][:4])
    refs = "\n".join(f"- **{tag}:** {text.replace('<em>', '*').replace('</em>', '*')}" for tag, text in topic["refs"][:3])
    metaphor = (
        topic["metaphor"]
        .replace("<strong>", "**").replace("</strong>", "**")
        .replace("<em>", "*").replace("</em>", "*")
        .replace("<br><br>", "\n\n")
    )
    serve_text = chr(10).join(topic["serve"]).replace("<strong>", "**").replace("</strong>", "**").replace("<em>", "*").replace("</em>", "*")
    code_preview = topic["python_code"][:600]
    if len(topic["python_code"]) > 600:
        code_preview += "..."

    return f"""<!-- .slide: class="title-slide" -->

# Enc. {topic['num']}

## {topic['title']}

{bloco['emoji']} Bloco {topic['bloco']} — {bloco['name']}

<p class="small">{topic['subtitle']}</p>

---

## 🍊 Metáfora

{metaphor}

---

## 🎯 Para que serve

{serve_text}

---

## 📋 Quando usar

{quando}

---

## 🐍 Exemplo Python

```python
{code_preview}
```

<div class="destaque">
Código <strong>executável</strong> na página de conteúdo — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

{refs}

---

## 🔗 Materiais

[Conteúdo completo + código executável](../content.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
"""


def jekyll_md(topic: dict) -> str:
    slug = topic["dir"]
    title = topic["title"]
    return f"""---
layout: default
title: {title}
nav_order: {topic['nav_order']}
parent: Encontros
has_children: false
---

# Enc. {topic['num']} — {title}

<p>{topic['subtitle']}</p>

## Slides

<center>
<iframe src="https://math.rpmhub.dev/{slug}/slides/index.html#/" title="{title}" width="90%" height="500" style="border:none;"></iframe>
</center>

## Conteúdo interativo

O material completo com metáforas, referências e **código Python executável** no navegador:

<p><a href="https://math.rpmhub.dev/{slug}/content.html" class="btn btn-primary">Abrir conteúdo interativo →</a></p>

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
"""


SLIDES_SHELL = '''<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>{title} — Slides</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,600;1,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reset.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/theme/black.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/github-dark.min.css">
    <link rel="stylesheet" href="../../assets/css/slides.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-markdown="slides.md"
                     data-separator="^---$"
                     data-separator-vertical="^--$"
                     data-charset="utf-8">
            </section>
        </div>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/markdown/markdown.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/notes/notes.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/plugin/highlight/highlight.min.js"></script>
    <script>
        Reveal.initialize({{
            hash: true, width: 1280, height: 800, margin: 0.08,
            transition: 'fade', slideNumber: 'c/t',
            plugins: [RevealMarkdown, RevealHighlight, RevealNotes]
        }});
    </script>
</body>
</html>
'''


def materiais_html() -> str:
    """Página única com todos os tópicos (visão geral)."""
    cards = []
    current_bloco = None
    for topic in TOPICS:
        bloco = BLOCOS[topic["bloco"]]
        if topic["bloco"] != current_bloco:
            current_bloco = topic["bloco"]
            cards.append(
                f'<div id="{bloco["id"]}" class="bloco-title {bloco["class"]}">'
                f'{bloco["emoji"]} Bloco {topic["bloco"]} — {bloco["name"]}</div>'
            )
        cards.append(f"""<div class="card">
  <div class="card-header">
    <div class="enc-num">{topic['num']}</div>
    <div><h2><a href="{topic['dir']}/content.html" style="color:inherit;text-decoration:none">{topic['title']}</a></h2>
    <p>{topic['subtitle']}</p></div>
  </div>
  <div class="section" style="padding:12px 22px">
    <a href="{topic['dir']}/content.html" style="color:#90c0ff;margin-right:16px">📖 Conteúdo + código</a>
    <a href="{topic['dir']}/slides/index.html" style="color:#d4b8f5">📊 Slides</a>
  </div>
</div>""")

    nav = "\n".join(
        f'    <a href="#{b["id"]}" class="nav-{b["class"]}">{b["emoji"]} Bloco {n} — {b["name"]} ({b["range"]})</a>'
        for n, b in BLOCOS.items()
    )

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Materiais Didáticos — Análise de Dados Conversacionais</title>
<link rel="stylesheet" href="assets/css/math.css">
</head>
<body>
<header>
  <h1>Materiais Didáticos — Análise de Dados Conversacionais</h1>
  <p>Disciplina de mestrado · 13 encontros · Metáforas · Exemplos · Código Python executável · Referências</p>
  <div class="bloco-nav">
{nav}
  </div>
</header>
{''.join(cards)}
<footer class="page-footer">
  <a href="index.html">Documentação Jekyll</a> · <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0</a>
</footer>
</body>
</html>"""


def intro_content() -> str:
    return """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Introdução — Análise de Dados Conversacionais</title>
<link rel="stylesheet" href="../assets/css/math.css">
</head>
<body>
<header>
  <h1>Análise de Dados Conversacionais</h1>
  <p>Disciplina de mestrado · Estatística aplicada a logs de chatbots e interações educacionais</p>
  <a class="back-link" href="../materiais.html">← Ver todos os materiais</a>
</header>

<div class="card">
  <div class="card-header">
    <div class="enc-num">1</div>
    <div><h2>Introdução ao curso</h2><p>Objetivos · Estrutura · Ferramentas</p></div>
  </div>

  <div class="section">
    <div class="section-label lbl-serve">🎯 Objetivo</div>
    <p>Este curso apresenta métodos estatísticos para analisar <strong>dados conversacionais</strong> em contextos educacionais: logs de chatbots, turnos de diálogo, escores de compreensão, perfis de uso e desfechos de aprendizagem.</p>
  </div>

  <div class="section">
    <div class="section-label lbl-quando">📋 Estrutura — 3 blocos</div>
    <ul>
      <li><strong>Bloco 1 — Associação (Enc. 2–5):</strong> correlações, qui-quadrado, análise fatorial</li>
      <li><strong>Bloco 2 — Comparação (Enc. 6–10):</strong> testes t, não-paramétricos, ANOVA, modelos mistos</li>
      <li><strong>Bloco 3 — Predição (Enc. 11–13):</strong> regressão linear, logística e de contagem</li>
    </ul>
  </div>

  <div class="section">
    <div class="section-label lbl-python">🐍 Ferramentas Python</div>
    <p><code>pandas</code>, <code>scipy</code>, <code>pingouin</code>, <code>statsmodels</code>, <code>scikit-learn</code>, <code>matplotlib</code></p>
    <div class="tip"><strong>Código executável:</strong> cada encontro inclui exemplos que rodam direto no navegador via <a href="https://pyodide.org" style="color:#90c0ff">Pyodide</a> — sem instalar Python.</div>
  </div>
</div>

<footer class="page-footer">
  <a href="../materiais.html">📚 Todos os materiais</a> ·
  <a href="slides/index.html">📊 Slides</a>
</footer>
</body>
</html>"""


def intro_slides_md() -> str:
    return """<!-- .slide: class="title-slide" -->

# Análise de Dados Conversacionais

## Encontro 1 — Introdução

Estatística aplicada a logs de chatbots e interações educacionais

---

## Objetivo do curso

Analisar **dados conversacionais** em contextos educacionais:

- Logs de chatbots e turnos de diálogo
- Escores de compreensão e perfis de uso
- Desfechos de aprendizagem

---

## Estrutura — 3 blocos

| Bloco | Encontros | Foco |
|-------|-----------|------|
| 🔗 1 | 2–5 | **Associação** |
| ⚖️ 2 | 6–10 | **Comparação** |
| 📈 3 | 11–13 | **Predição** |

---

## Ferramentas

- `pandas`, `scipy`, `pingouin`
- `statsmodels`, `scikit-learn`
- `matplotlib`

<div class="destaque">
Exemplos <strong>executáveis no navegador</strong> (Pyodide) — sem instalar Python.
</div>

---

## Materiais

[materiais.html](https://math.rpmhub.dev/materiais.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
"""


def intro_jekyll() -> str:
    return """---
layout: default
title: Introdução
nav_order: 3
parent: Encontros
has_children: false
---

# Introdução

Disciplina de mestrado sobre **análise estatística de dados conversacionais** em contextos educacionais com chatbots e sistemas de IA.

## Slides

<center>
<iframe src="https://math.rpmhub.dev/01introducao/slides/index.html#/" title="Introdução" width="90%" height="500" style="border:none;"></iframe>
</center>

## Conteúdo

<p><a href="https://math.rpmhub.dev/01introducao/content.html">Abrir conteúdo →</a></p>

<p><a href="https://math.rpmhub.dev/materiais.html">Ver todos os 13 encontros →</a></p>

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
"""


def main():
    # Slides CSS (purple theme for reveal.js)
    # Intro
    intro_dir = DOCS / "01introducao"
    intro_dir.mkdir(parents=True, exist_ok=True)
    (intro_dir / "content.html").write_text(intro_content(), encoding="utf-8")
    (intro_dir / "introducao.md").write_text(intro_jekyll(), encoding="utf-8")
    slides_dir = intro_dir / "slides"
    slides_dir.mkdir(exist_ok=True)
    (slides_dir / "slides.md").write_text(intro_slides_md(), encoding="utf-8")
    (slides_dir / "index.html").write_text(
        SLIDES_SHELL.format(title="Introdução"), encoding="utf-8"
    )

    # Topics
    for topic in TOPICS:
        tdir = DOCS / topic["dir"]
        tdir.mkdir(parents=True, exist_ok=True)
        (tdir / "content.html").write_text(content_html(topic), encoding="utf-8")
        slug = topic["dir"].split("-", 1)[-1] if "-" in topic["dir"] else topic["dir"]
        md_name = slug + ".md" if not topic["dir"].startswith("0") else topic["dir"][2:] + ".md"
        # use dir suffix as filename: 02pearson -> pearson.md
        parts = topic["dir"]
        fname = parts[2:] + ".md"  # remove leading number prefix like 02
        (tdir / fname).write_text(jekyll_md(topic), encoding="utf-8")
        sdir = tdir / "slides"
        sdir.mkdir(exist_ok=True)
        (sdir / "slides.md").write_text(slides_md(topic), encoding="utf-8")
        (sdir / "index.html").write_text(
            SLIDES_SHELL.format(title=topic["title"]), encoding="utf-8"
        )
        print(f"  ✓ {topic['dir']}")

    # Overview page
    (DOCS / "materiais.html").write_text(materiais_html(), encoding="utf-8")
    print("  ✓ materiais.html")
    print(f"\nGerados {len(TOPICS)} tópicos + introdução em {DOCS}")


if __name__ == "__main__":
    main()
