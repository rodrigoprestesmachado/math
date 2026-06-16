---
layout: default
title: Regressão Logística (binária e ordinal)
nav_order: 14
parent: Encontros
has_children: false
---

# Enc. 12 — Regressão Logística (binária e ordinal)

`statsmodels Logit() · mord · sklearn ROC/AUC`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/12regressao-logistica/slides/index.html#/" title="Regressão Logística (binária e ordinal)" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Para prever *engajou ou não engajou*, a logística usa uma sigmoid que espreme valores em [0, 1] — probabilidade. Coeficientes como **odds ratios**: OR = 2 significa chances dobradas. A **curva ROC** mede a qualidade do modelo (AUC).

---

## 🎯 Para que serve

Modelar desfechos **categóricos**: binária (engajou/não) ou ordinal (baixo/médio/alto).

---

## 📋 Quando usar

- ✅ **Binária:** duas categorias mutuamente exclusivas.
- ✅ **Ordinal:** 3+ categorias ordenadas.
- ✅ AUC > 0.70 aceitável · > 0.80 bom · > 0.90 excelente.
- ❌ Não use regressão linear para desfecho binário.

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="aW1wb3J0IHN0YXRzbW9kZWxzLmFwaSBhcyBzbQppbXBvcnQgcGFuZGFzIGFzIHBkCmltcG9ydCBudW1weSBhcyBucApmcm9tIHNrbGVhcm4ubWV0cmljcyBpbXBvcnQgcm9jX2F1Y19zY29yZQoKZGYgPSBwZC5EYXRhRnJhbWUoewogICAgJ2VuZ2Fqb3UnOiAgICAgWzEsMCwxLDEsMCwxLDAsMSwwLDEsMCwxXSwKICAgICd1c29fY2hhdGJvdCc6IFs4LDIsOSw3LDMsMTAsMSw4LDQsOSwyLDExXSwKICAgICdtZXRhY29nbmljYW8nOls2NSw0MCw3MCw2OCwzOCw3NSwzNSw3Miw0Miw3OCwzMyw4MF0KfSkKClggPSBzbS5hZGRfY29uc3RhbnQoZGZbWyd1c29fY2hhdGJvdCcsICdtZXRhY29nbmljYW8nXV0pCm1vZGVsbyA9IHNtLkxvZ2l0KGRmWydlbmdham91J10sIFgpLmZpdChkaXNwPTApCnByaW50KG1vZGVsby5zdW1tYXJ5KCkpCgpPUiA9IG5wLmV4cChtb2RlbG8ucGFyYW1zKQpwcmludCgiXG5PZGRzIFJhdGlvczoiKQpwcmludChPUi5yb3VuZCgzKSkKCnlfcHJlZCA9IG1vZGVsby5wcmVkaWN0KFgpCmF1YyA9IHJvY19hdWNfc2NvcmUoZGZbJ2VuZ2Fqb3UnXSwgeV9wcmVkKQpwcmludChmIlxuQVVDID0ge2F1YzouM2Z9Iik=" markdown="0">
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
| **referência** | Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). *Applied Logistic Regression* (3ª ed.). |
| **didático** | Field, A. (2024). *Discovering Statistics*. Cap. 20. |
| **ROC** | Fawcett, T. (2006). An introduction to ROC analysis. *Pattern Recognition Letters, 27*(8), 861–874. |
| **ordinal** | McCullagh, P. (1980). Regression models for ordinal data. *JRSS B, 42*(2), 109–142. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
