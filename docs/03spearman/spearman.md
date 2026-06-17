---
layout: default
title: Correlação de Spearman e Kendall
nav_order: 3
parent: Associação
has_children: false
---

# Enc. 3 — Correlação de Spearman e Kendall

`scipy.stats.spearmanr · scipy.stats.kendalltau`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/03spearman/slides/index.html#/" title="Correlação de Spearman e Kendall" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Em vez de medir a velocidade exata de cada atleta, você registra a **posição deles na corrida**: 1º, 2º, 3º… Spearman e Kendall trocam os valores originais pelos seus *postos* (rankings). **Kendall** é mais conservador: conta quantos pares estão na ordem certa versus errada — útil quando há muitos empates.

---

## 🎯 Para que serve

Alternativas **não-paramétricas** a Pearson. Medem relações *monotônicas*. Ideais para dados ordinais como escalas Likert.

Exemplo: *a satisfação do estudante com o chatbot (escala 1–5) está associada à quantidade de sessões voluntárias?*

---

## 📋 Quando usar

- ✅ Uma ou ambas as variáveis são **ordinais** (Likert).
- ✅ Os dados violam normalidade (Shapiro-Wilk: p < .05).
- ✅ Há outliers que não devem ser removidos.
- ✅ Use **Kendall** com n < 30 ou muitos empates.
- ❌ Não diferencia relações lineares de curvilíneas — só detecta monotonicidade.

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZAppbXBvcnQgbnVtcHkgYXMgbnAKZnJvbSBzY2lweSBpbXBvcnQgc3RhdHMKCmRmID0gcGQuRGF0YUZyYW1lKHsKICAgICdzYXRpc2ZhY2FvJzogWzIsNCwxLDUsMyw1LDQsMiwzLDVdLAogICAgJ3Nlc3NvZXMnOiAgICBbMyw4LDEsMTIsNSwxMSw5LDIsNCwxM10KfSkKCiMgU3BlYXJtYW4KcmhvLCBwX3MgPSBzdGF0cy5zcGVhcm1hbnIoZGZbJ3NhdGlzZmFjYW8nXSwgZGZbJ3Nlc3NvZXMnXSkKcHJpbnQoZiJTcGVhcm1hbiDPgSA9IHtyaG86LjNmfSwgcCA9IHtwX3M6LjRmfSIpCgojIEtlbmRhbGwKdGF1LCBwX2sgPSBzdGF0cy5rZW5kYWxsdGF1KGRmWydzYXRpc2ZhY2FvJ10sIGRmWydzZXNzb2VzJ10pCnByaW50KGYiS2VuZGFsbCAgz4QgPSB7dGF1Oi4zZn0sIHAgPSB7cF9rOi40Zn0iKQoKIyBJQyA5NSUgcGFyYSDPgSB2aWEgdHJhbnNmb3JtYcOnw6NvIGRlIEZpc2hlcgpuID0gbGVuKGRmKQp6ICA9IG5wLmFyY3RhbmgocmhvKQpzZSA9IDEuMCAvIG5wLnNxcnQobiAtIDMpCmNpX2xvLCBjaV9oaSA9IG5wLnRhbmgoeiAtIDEuOTYqc2UpLCBucC50YW5oKHogKyAxLjk2KnNlKQpwcmludChmIgpuPXtufSwgSUMgOTUlID0gW3tjaV9sbzouMmZ9LCB7Y2lfaGk6LjJmfV0iKQoKIyBWaXN1YWxpemHDp8OjbyBkb3MgcG9zdG9zCmRmWydyYW5rX3NhdCddID0gZGZbJ3NhdGlzZmFjYW8nXS5yYW5rKCkKZGZbJ3Jhbmtfc2VzJ10gPSBkZlsnc2Vzc29lcyddLnJhbmsoKQppbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CmRmLnBsb3Quc2NhdHRlcih4PSdyYW5rX3NhdCcsIHk9J3Jhbmtfc2VzJywgY29sb3I9JyNjNzkyZWEnLAogICAgICAgICAgICAgICAgdGl0bGU9J1Bvc3RvczogU2F0aXNmYcOnw6NvIMOXIFNlc3PDtWVzJykKcGx0LnhsYWJlbCgnUG9zdG8g4oCTIHNhdGlzZmHDp8OjbycpCnBsdC55bGFiZWwoJ1Bvc3RvIOKAkyBzZXNzw7VlcycpCnBsdC5zaG93KCk=" markdown="0">
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
| **seminal** | Spearman, C. (1904). The proof and measurement of association between two things. *American Journal of Psychology, 15*(1), 72–101. |
| **didático** | Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6ª ed.). SAGE. Cap. 8. |
| **python** | Vallat, R. (2018). Pingouin: statistics in Python. *Journal of Open Source Software, 3*(31), 1026. |
| **aplicado** | Norman, G. (2010). Likert scales, levels of measurement and the "laws" of statistics. *Advances in Health Sciences Education, 15*, 625–632. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
