#!/usr/bin/env python3
"""Gera páginas de conteúdo, slides e arquivos Jekyll para math.rpmhub.dev."""

from pathlib import Path
import html
import sys

sys.path.insert(0, str(Path(__file__).parent))
from topics import TOPICS, BLOCOS

DOCS = Path(__file__).resolve().parent.parent / "docs"
ASSETS = DOCS / "assets"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def esc(text: str) -> str:
    """Escapes HTML entities for inserção em atributos/conteúdo HTML."""
    return html.escape(text, quote=False)


def strip_html(text: str) -> str:
    """Converte tags HTML simples para equivalentes Markdown."""
    pairs = [
        ('<strong>', '**'), ('</strong>', '**'),
        ('<em>', '*'),      ('</em>',     '*'),
        ('<br><br>', '\n\n'), ('<br>', '  \n'),
        ('&lt;', '<'), ('&gt;', '>'), ('&amp;', '&'),
    ]
    for old, new in pairs:
        text = text.replace(old, new)
    return text


# ---------------------------------------------------------------------------
# CSS embutido no content.html — combina com o tema just-the-docs
# ---------------------------------------------------------------------------

RUNNER_CSS = """\
.python-runner {
  margin: 1.5rem 0;
  border: 1px solid #e6e1e8;
  border-radius: 6px;
  overflow: hidden;
}
.python-runner .toolbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.55rem 1rem;
  background: #f5f6fa;
  border-bottom: 1px solid #e6e1e8;
  font-size: 0.78rem;
  color: #5c5962;
}
.python-runner .run-btn {
  background: #7253ed;
  color: #fff;
  border: none;
  border-radius: 4px;
  padding: 4px 16px;
  font-size: 0.78rem;
  font-weight: 600;
  cursor: pointer;
  font-family: inherit;
}
.python-runner .run-btn:hover { background: #5e41d0; }
.python-runner .run-btn:disabled { opacity: 0.5; cursor: wait; }
.python-runner textarea.code-input {
  display: block;
  width: 100%;
  min-height: 240px;
  padding: 1rem;
  margin: 0;
  background: #1e1e2e;
  color: #cdd6f4;
  border: none;
  resize: vertical;
  outline: none;
  font-family: 'Menlo', 'Monaco', 'Consolas', monospace;
  font-size: 0.82rem;
  line-height: 1.6;
  tab-size: 4;
}
.python-runner .code-output {
  display: none;
  padding: 0.75rem 1rem;
  border-top: 1px solid #e6e1e8;
  font-family: 'Menlo', 'Monaco', 'Consolas', monospace;
  font-size: 0.78rem;
  color: #1a6a1a;
  white-space: pre-wrap;
  max-height: 420px;
  overflow-y: auto;
  background: #f6fff6;
}
.python-runner .code-output.visible { display: block; }
.python-runner .code-output.error   { color: #c62828; background: #fff6f6; }
.python-runner .code-output img {
  max-width: 100%;
  margin-top: 0.5rem;
  border-radius: 4px;
  display: block;
}
.py-loading {
  position: fixed;
  bottom: 1.5rem;
  right: 1.5rem;
  background: #fff;
  border: 1px solid #7253ed;
  border-radius: 6px;
  padding: 0.55rem 1rem;
  font-size: 0.78rem;
  color: #5c5962;
  z-index: 1000;
  display: none;
  box-shadow: 0 2px 8px rgba(0,0,0,0.12);
}
.py-loading.visible { display: block; }"""


# ---------------------------------------------------------------------------
# content.html — página Jekyll, só o runner Python
# ---------------------------------------------------------------------------

def content_html(topic: dict) -> str:
    """Página Jekyll com layout do site, contendo apenas o runner Python."""
    context = topic.get('python_context', '')
    context_block = f"\n{context}\n" if context else ""
    back_fname = topic['dir'][2:] + '.html'   # e.g. 02pearson -> pearson.html

    return f"""---
layout: default
title: "{esc(topic['title'])} — Código Python"
nav_exclude: true
---

## 🐍 Enc. {topic['num']} — {topic['title']}
{context_block}
<style>
{RUNNER_CSS}
</style>

<div class="python-runner">
  <div class="toolbar">
    <span>🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false">{esc(topic['python_code'])}</textarea>
  <pre class="code-output"></pre>
</div>

[← Voltar ao conteúdo]({back_fname})

<script src="https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js"></script>
<script src="/assets/js/py-runner.js"></script>
"""


# ---------------------------------------------------------------------------
# jekyll_md — .md principal com todo o conteúdo didático
# ---------------------------------------------------------------------------

def jekyll_md(topic: dict) -> str:
    """Gera o .md Jekyll com metáfora, serve, quando usar, refs e link para o runner."""
    bloco = BLOCOS[topic["bloco"]]

    metaphor_label = topic.get('metaphor_label', 'Imagine isso…')
    metaphor_text  = strip_html(topic['metaphor'])

    serve_paras = "\n\n".join(strip_html(p) for p in topic['serve'])

    quando_items = "\n".join(f"- {strip_html(item)}" for item in topic['quando'])

    tip_block = ""
    if topic.get('tip'):
        tip_block = f"\n{{: .highlight }}\n> {strip_html(topic['tip'])}\n"

    context = topic.get('python_context', '')
    python_context_line = f"\n{context}\n" if context else ""

    ref_rows = "\n".join(
        f"| **{tag}** | {strip_html(text)} |"
        for tag, text in topic['refs']
    )

    # Kramdown class attributes usam { } — escapar do f-string com {{ }}
    fname = topic['dir'][2:] + '.html'   # back link de content.html -> aqui

    return f"""---
layout: default
title: {topic['title']}
nav_order: {topic['nav_order']}
parent: Encontros
has_children: false
---

# Enc. {topic['num']} — {topic['title']}

`{topic['subtitle']}`
{{: .fs-5 .fw-300 }}

---

## 🍊 Metáfora

> **{metaphor_label}**
>
> {metaphor_text}

---

## 🎯 Para que serve

{serve_paras}

---

## 📋 Quando usar

{quando_items}
{tip_block}
---

## 🐍 Exemplo Python
{python_context_line}
[▶ Abrir código executável](content.html){{: .btn .btn-primary }}

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/{topic['dir']}/slides/index.html#/" title="{topic['title']}" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 📚 Referências

| | |
|:--|:--|
{ref_rows}

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
"""


# ---------------------------------------------------------------------------
# Slides Reveal.js
# ---------------------------------------------------------------------------

def slides_md(topic: dict) -> str:
    bloco = BLOCOS[topic["bloco"]]
    quando = "\n".join(f"- {item}" for item in topic["quando"][:4])
    refs = "\n".join(
        f"- **{tag}:** {text.replace('<em>', '*').replace('</em>', '*')}"
        for tag, text in topic["refs"][:3]
    )
    metaphor = (
        topic["metaphor"]
        .replace("<strong>", "**").replace("</strong>", "**")
        .replace("<em>", "*").replace("</em>", "*")
        .replace("<br><br>", "\n\n")
    )
    serve_text = (
        "\n\n".join(topic["serve"])
        .replace("<strong>", "**").replace("</strong>", "**")
        .replace("<em>", "*").replace("</em>", "*")
    )
    code_preview = topic["python_code"][:600]
    if len(topic["python_code"]) > 600:
        code_preview += "\n..."

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
Código <strong>executável</strong> na página do encontro — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

{refs}

---

## 🔗 Materiais

[Conteúdo completo + código executável](../{topic['dir'][2:]}.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
"""


# ---------------------------------------------------------------------------
# Shell dos slides Reveal.js
# ---------------------------------------------------------------------------

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


# ---------------------------------------------------------------------------
# materiais.html — visão geral (standalone, sem Jekyll)
# ---------------------------------------------------------------------------

def materiais_html() -> str:
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
        md_fname = topic['dir'][2:] + '.html'
        cards.append(f"""<div class="card">
  <div class="card-header">
    <div class="enc-num">{topic['num']}</div>
    <div><h2><a href="{topic['dir']}/{md_fname}" style="color:inherit;text-decoration:none">{topic['title']}</a></h2>
    <p>{topic['subtitle']}</p></div>
  </div>
  <div class="section" style="padding:12px 22px">
    <a href="{topic['dir']}/{md_fname}" style="color:#90c0ff;margin-right:16px">📖 Conteúdo</a>
    <a href="{topic['dir']}/content.html" style="color:#90e090;margin-right:16px">🐍 Código Python</a>
    <a href="{topic['dir']}/slides/index.html" style="color:#d4b8f5">📊 Slides</a>
  </div>
</div>""")

    nav = "\n".join(
        f'    <a href="#{b["id"]}" class="nav-{b["class"]}">'
        f'{b["emoji"]} Bloco {n} — {b["name"]} ({b["range"]})</a>'
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


# ---------------------------------------------------------------------------
# Introdução (Enc. 1) — sem código Python
# ---------------------------------------------------------------------------

def intro_jekyll() -> str:
    return """---
layout: default
title: Introdução
nav_order: 3
parent: Encontros
has_children: false
---

# Enc. 1 — Análise de Dados Conversacionais

`Objetivos · Estrutura do curso · Ferramentas Python`
{: .fs-5 .fw-300 }

---

## 🎯 Objetivo

Este curso apresenta métodos estatísticos para analisar **dados conversacionais** em contextos educacionais:
logs de chatbots, turnos de diálogo, escores de compreensão, perfis de uso e desfechos de aprendizagem.

---

## 📋 Estrutura — 3 blocos

| Bloco | Encontros | Foco |
|:------|:----------|:-----|
| 🔗 1 — Associação | 2 a 5 | Correlações, qui-quadrado, análise fatorial |
| ⚖️ 2 — Comparação | 6 a 10 | Testes t, não-paramétricos, ANOVA, LMM |
| 📈 3 — Predição | 11 a 13 | Regressão linear, logística e de contagem |

Cada encontro inclui **slides** e **código Python executável** no navegador (sem instalar nada).

---

## 🐍 Ferramentas Python

`pandas` · `scipy` · `pingouin` · `statsmodels` · `scikit-learn` · `matplotlib`

Os exemplos rodam diretamente no navegador via [Pyodide](https://pyodide.org). Clique em **▶ Executar** em qualquer encontro — na primeira execução o Python carrega em ~30 s.

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/01introducao/slides/index.html#/" title="Introdução" width="90%" height="500" style="border:none;"></iframe>
</center>

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
"""


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

[math.rpmhub.dev/materiais.html](https://math.rpmhub.dev/materiais.html)
"""


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    # Introdução (sem Python runner)
    intro_dir = DOCS / "01introducao"
    intro_dir.mkdir(parents=True, exist_ok=True)
    (intro_dir / "introducao.md").write_text(intro_jekyll(), encoding="utf-8")
    slides_dir = intro_dir / "slides"
    slides_dir.mkdir(exist_ok=True)
    (slides_dir / "slides.md").write_text(intro_slides_md(), encoding="utf-8")
    (slides_dir / "index.html").write_text(
        SLIDES_SHELL.format(title="Introdução"), encoding="utf-8"
    )
    print("  ✓ 01introducao")

    # Tópicos 2–13
    for topic in TOPICS:
        tdir = DOCS / topic["dir"]
        tdir.mkdir(parents=True, exist_ok=True)

        fname = topic["dir"][2:] + ".md"           # e.g. pearson.md
        (tdir / fname).write_text(jekyll_md(topic), encoding="utf-8")
        (tdir / "content.html").write_text(content_html(topic), encoding="utf-8")

        sdir = tdir / "slides"
        sdir.mkdir(exist_ok=True)
        (sdir / "slides.md").write_text(slides_md(topic), encoding="utf-8")
        (sdir / "index.html").write_text(
            SLIDES_SHELL.format(title=topic["title"]), encoding="utf-8"
        )
        print(f"  ✓ {topic['dir']}")

    # Visão geral standalone
    (DOCS / "materiais.html").write_text(materiais_html(), encoding="utf-8")
    print("  ✓ materiais.html")
    print(f"\nGerados {len(TOPICS)} tópicos + introdução em {DOCS}")


if __name__ == "__main__":
    main()
