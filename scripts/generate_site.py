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
# Bloco HTML do runner Python para embutir no .md
# O CSS vem de runner.css (via head_custom.html), não precisa de <style> inline.
# ---------------------------------------------------------------------------

def python_runner_block(topic: dict) -> str:
    """Retorna o bloco HTML do runner para inserção no .md."""
    context = topic.get('python_context', '')
    ctx_line = f"\n{context}\n" if context else ""
    return f"""{ctx_line}
<div class="python-runner" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false">{esc(topic['python_code'])}</textarea>
  <pre class="code-output"></pre>
</div>"""


# ---------------------------------------------------------------------------
# content.html — redireciona para o .md principal (mantido por compatibilidade)
# ---------------------------------------------------------------------------

def content_html(topic: dict) -> str:
    """Redireciona links antigos para a página principal do tópico."""
    back = topic['dir'][2:] + '.html'
    return f"""---
layout: null
---
<meta http-equiv="refresh" content="0; url={back}">
<p>Redirecionando... <a href="{back}">Clique aqui</a></p>
"""


# ---------------------------------------------------------------------------
# jekyll_md — .md principal com todo o conteúdo didático
# ---------------------------------------------------------------------------

def jekyll_md(topic: dict) -> str:
    """Gera o .md completo: slides no topo, todo conteúdo didático e runner Python."""
    bloco = BLOCOS[topic["bloco"]]

    metaphor_label = topic.get('metaphor_label', 'Imagine isso…')
    metaphor_text  = strip_html(topic['metaphor'])

    serve_paras = "\n\n".join(strip_html(p) for p in topic['serve'])

    quando_items = "\n".join(f"- {strip_html(item)}" for item in topic['quando'])

    tip_block = ""
    if topic.get('tip'):
        tip_block = f"\n{{: .highlight }}\n> {strip_html(topic['tip'])}\n"

    ref_rows = "\n".join(
        f"| **{tag}** | {strip_html(text)} |"
        for tag, text in topic['refs']
    )

    runner = python_runner_block(topic)

    # Kramdown class attributes usam { } — escapar do f-string com {{ }}
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

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/{topic['dir']}/slides/index.html#/" title="{topic['title']}" width="90%" height="500" style="border:none;"></iframe>
</center>

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

{runner}

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

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/01introducao/slides/index.html#/" title="Introdução" width="90%" height="500" style="border:none;"></iframe>
</center>

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

Cada encontro inclui **slides** e **código Python executável** direto na página.

---

## 🐍 Ferramentas Python

`pandas` · `scipy` · `pingouin` · `statsmodels` · `scikit-learn` · `matplotlib`

Os exemplos rodam no navegador via [Pyodide](https://pyodide.org) — sem instalar Python. Clique em **▶ Executar** em qualquer encontro. Na primeira execução o runtime Python carrega em ~30 s.

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
