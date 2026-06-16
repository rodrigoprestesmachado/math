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


<div class="python-runner" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false">import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score

df = pd.DataFrame({
    'engajou':     [1,0,1,1,0,1,0,1,0,1,0,1],
    'uso_chatbot': [8,2,9,7,3,10,1,8,4,9,2,11],
    'metacognicao':[65,40,70,68,38,75,35,72,42,78,33,80]
})

X = sm.add_constant(df[['uso_chatbot', 'metacognicao']])
modelo = sm.Logit(df['engajou'], X).fit(disp=0)
print(modelo.summary())

OR = np.exp(modelo.params)
print("\nOdds Ratios:")
print(OR.round(3))

y_pred = modelo.predict(X)
auc = roc_auc_score(df['engajou'], y_pred)
print(f"\nAUC = {auc:.3f}")</textarea>
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
