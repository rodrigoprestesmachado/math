---
layout: default
title: Regressão Linear (simples e múltipla)
nav_order: 13
parent: Encontros
has_children: false
---

# Enc. 11 — Regressão Linear (simples e múltipla)

`statsmodels.formula.api.ols() · sklearn LinearRegression`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/11regressao-linear/slides/index.html#/" title="Regressão Linear (simples e múltipla)" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> A regressão traça a *linha reta que erra menos* para todos os pontos. A múltipla adiciona dimensões: cada coeficiente é o efeito *único* da variável, mantendo as outras constantes.

---

## 🎯 Para que serve

Modelar e predizer um desfecho **numérico contínuo** a partir de preditores.

---

## 📋 Quando usar

- ✅ Desfecho numérico contínuo.
- ✅ Relação linear entre preditores e desfecho.
- ✅ Resíduos normais e homocedásticos.
- ✅ VIF > 5 indica multicolinearidade.
- ❌ Para inferência científica use statsmodels; para ML use sklearn.

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="import statsmodels.formula.api as smf&#10;import pandas as pd&#10;from statsmodels.stats.outliers_influence import variance_inflation_factor&#10;&#10;df = pd.DataFrame({&#10;    &#x27;escore_final&#x27;:  [72,85,60,90,68,78,82,55,88,74],&#10;    &#x27;uso_chatbot&#x27;:   [5,9,3,12,4,7,10,2,11,6],&#10;    &#x27;metacognicao&#x27;:  [60,72,55,80,58,68,75,50,78,65],&#10;    &#x27;letramento_ia&#x27;: [40,55,35,65,42,52,60,30,62,48]&#10;})&#10;&#10;modelo = smf.ols(&#x27;escore_final ~ uso_chatbot + metacognicao + letramento_ia&#x27;, data=df).fit()&#10;print(modelo.summary())&#10;&#10;X = df[[&#x27;uso_chatbot&#x27;,&#x27;metacognicao&#x27;,&#x27;letramento_ia&#x27;]]&#10;vif = pd.DataFrame({&#10;    &#x27;variável&#x27;: X.columns,&#10;    &#x27;VIF&#x27;: [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]&#10;})&#10;print(vif)" markdown="0">
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
| **referência** | Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8ª ed.). Cap. 4. |
| **didático** | James, G., et al. (2023). *An Introduction to Statistical Learning* (2ª ed.). Cap. 3. |
| **VIF** | O'Brien, R. M. (2007). A caution regarding rules of thumb for VIF. *Quality & Quantity, 41*, 673–690. |
| **python** | McKinney, W. (2022). *Python for Data Analysis*. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
