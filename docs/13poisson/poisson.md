---
layout: default
title: Regressão de Poisson e Binomial Negativa
nav_order: 15
parent: Encontros
has_children: false
---

# Enc. 13 — Regressão de Poisson e Binomial Negativa

`statsmodels poisson() · negativebinomial()`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/13poisson/slides/index.html#/" title="Regressão de Poisson e Binomial Negativa" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Contagens (perguntas ao chatbot) são inteiras e nunca negativas. Poisson modela a taxa de eventos. Se a variância explode (superdispersão), a **Binomial Negativa** adiciona folga extra.

---

## 🎯 Para que serve

Modelar desfechos de **contagem**: turnos, perguntas, mensagens. Poisson para equidispersão; BN para superdispersão.

---

## 📋 Quando usar

- ✅ Desfecho são contagens inteiras não-negativas.
- ✅ **Poisson:** variância/média ≈ 1.
- ✅ **BN:** índice de dispersão > 1.5.
- ✅ Comparar via AIC: menor = melhor.
- ❌ Não use regressão linear para contagens.

{: .highlight }
> **Interpretar coeficientes:** exp(coef) = Risk Ratio. RR = 1.3 → 30% mais eventos por unidade.

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="import statsmodels.formula.api as smf&#10;import pandas as pd&#10;import numpy as np&#10;&#10;np.random.seed(7)&#10;n = 80&#10;df = pd.DataFrame({&#10;    &#x27;perguntas&#x27;:    np.random.negative_binomial(2, 0.3, n),&#10;    &#x27;metacognicao&#x27;: np.random.normal(60, 10, n),&#10;    &#x27;tempo_sessao&#x27;: np.random.normal(20, 5, n)&#10;})&#10;&#10;media, var = df.perguntas.mean(), df.perguntas.var()&#10;print(f&quot;Média={media:.2f}  Variância={var:.2f}  Índice={var/media:.2f}&quot;)&#10;&#10;mod_p  = smf.poisson(&#x27;perguntas ~ metacognicao + tempo_sessao&#x27;, data=df).fit(disp=0)&#10;mod_nb = smf.negativebinomial(&#x27;perguntas ~ metacognicao + tempo_sessao&#x27;, data=df).fit(disp=0)&#10;&#10;print(f&quot;AIC Poisson = {mod_p.aic:.1f}&quot;)&#10;print(f&quot;AIC BN      = {mod_nb.aic:.1f}&quot;)&#10;&#10;print(&quot;\nRisk Ratios (BN):&quot;)&#10;print(np.exp(mod_nb.params).round(3))" markdown="0">
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
| **referência** | Cameron, A. C., & Trivedi, P. K. (2013). *Regression Analysis of Count Data* (2ª ed.). |
| **didático** | Hilbe, J. M. (2011). *Negative Binomial Regression* (2ª ed.). |
| **comparação** | Ver Hoef, J. M., & Boveng, P. L. (2007). Quasi-Poisson vs. negative binomial. *Ecology, 88*(11), 2766–2772. |
| **educação** | Coxe, S., West, S. G., & Aiken, L. S. (2009). The analysis of count data. *Journal of Personality Assessment, 91*(2), 121–136. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
