---
layout: default
title: ANOVA Fatorial e Medidas Repetidas
nav_order: 11
parent: Encontros
has_children: false
---

# Enc. 9 — ANOVA Fatorial e Medidas Repetidas

`pingouin.anova() · pingouin.rm_anova() · statsmodels AnovaRM`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/09anova-fatorial/slides/index.html#/" title="ANOVA Fatorial e Medidas Repetidas" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Duas variações do mesmo instrumento**
>
> **Fatorial:** verifica efeito de cada fator e a *interação* (ex.: café ajuda de manhã mas não à noite).

**Medidas Repetidas:** o mesmo estudante medido em pré, durante e pós — cada pessoa é seu próprio controle.

---

## 🎯 Para que serve

**Fatorial:** avalia múltiplos fatores e interações. **MR:** compara os mesmos sujeitos em ≥ 3 momentos.

---

## 📋 Quando usar

- ✅ **Fatorial:** dois ou mais fatores categóricos com interesse na interação.
- ✅ **MR:** mesmo sujeito em ≥ 3 momentos longitudinais.
- ✅ Verificar esfericidade (Mauchly) — se violada, correção Greenhouse-Geisser.
- ❌ Dropout sistemático → prefira LMM.

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="aW1wb3J0IHBpbmdvdWluIGFzIHBnCmltcG9ydCBwYW5kYXMgYXMgcGQKCmRmX3JtID0gcGQuRGF0YUZyYW1lKHsKICAgICdzdWplaXRvJzogbGlzdChyYW5nZSg4KSkgKiAzLAogICAgJ21vbWVudG8nOiBbJ3ByZSddKjggKyBbJ2R1cmFudGUnXSo4ICsgWydwb3MnXSo4LAogICAgJ2VzY29yZSc6ICBbNTAsNTUsNDgsNjAsNTIsNTgsNDUsNTMsCiAgICAgICAgICAgICAgICA2Miw2OCw1OSw3Miw2NSw3MCw1Nyw2NCwKICAgICAgICAgICAgICAgIDc1LDgwLDcwLDg1LDc4LDgzLDY4LDc2XQp9KQoKcm0gPSBwZy5ybV9hbm92YShkYXRhPWRmX3JtLCBkdj0nZXNjb3JlJywgd2l0aGluPSdtb21lbnRvJywKICAgICAgICAgICAgICAgICBzdWJqZWN0PSdzdWplaXRvJywgY29ycmVjdGlvbj1UcnVlKQpwcmludChybVtbJ1NvdXJjZScsJ0YnLCdwLXVuYycsJ3AtR0ctY29ycicsJ25nMiddXSkKCnBoID0gcGcucGFpcndpc2VfdGVzdHMoZGF0YT1kZl9ybSwgZHY9J2VzY29yZScsIHdpdGhpbj0nbW9tZW50bycsCiAgICAgICAgICAgICAgICAgICAgICAgc3ViamVjdD0nc3VqZWl0bycsIHBhZGp1c3Q9J2JvbmYnKQpwcmludChwaFtbJ0EnLCdCJywnVCcsJ3AtY29ycicsJ2NvaGVuLWQnXV0p" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false"></textarea>
  <pre class="code-output"></pre>
</div>

---

## 📚 Referências

| | |
|:--|:--|
| **didático** | Field, A. (2024). *Discovering Statistics*. Caps. 14–15. |
| **técnico** | Greenhouse, S. W., & Geisser, S. (1959). *Psychometrika, 24*(2), 95–112. |
| **python** | Vallat, R. (2018). Pingouin: statistics in Python. |
| **aplicado** | Girden, E. R. (1992). *ANOVA: Repeated Measures*. SAGE. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
