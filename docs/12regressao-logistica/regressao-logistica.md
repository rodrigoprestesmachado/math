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


<div class="python-runner" data-code="import statsmodels.api as sm&#10;import pandas as pd&#10;import numpy as np&#10;from sklearn.metrics import roc_auc_score&#10;&#10;df = pd.DataFrame({&#10;    &#x27;engajou&#x27;:     [1,0,1,1,0,1,0,1,0,1,0,1],&#10;    &#x27;uso_chatbot&#x27;: [8,2,9,7,3,10,1,8,4,9,2,11],&#10;    &#x27;metacognicao&#x27;:[65,40,70,68,38,75,35,72,42,78,33,80]&#10;})&#10;&#10;X = sm.add_constant(df[[&#x27;uso_chatbot&#x27;, &#x27;metacognicao&#x27;]])&#10;modelo = sm.Logit(df[&#x27;engajou&#x27;], X).fit(disp=0)&#10;print(modelo.summary())&#10;&#10;OR = np.exp(modelo.params)&#10;print(&quot;\nOdds Ratios:&quot;)&#10;print(OR.round(3))&#10;&#10;y_pred = modelo.predict(X)&#10;auc = roc_auc_score(df[&#x27;engajou&#x27;], y_pred)&#10;print(f&quot;\nAUC = {auc:.3f}&quot;)" markdown="0">
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
