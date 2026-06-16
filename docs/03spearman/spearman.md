---
layout: default
title: Correlação de Spearman e Kendall
nav_order: 5
parent: Encontros
has_children: false
---

# Enc. 3 — Correlação de Spearman e Kendall

`scipy.stats.spearmanr · scipy.stats.kendalltau · pingouin.corr()`
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


<div class="python-runner" data-code="import pandas as pd&#10;from scipy import stats&#10;import pingouin as pg&#10;&#10;df = pd.DataFrame({&#10;    &#x27;satisfacao&#x27;: [2,4,1,5,3,5,4,2,3,5],&#10;    &#x27;sessoes&#x27;:    [3,8,1,12,5,11,9,2,4,13]&#10;})&#10;&#10;rho, p_s = stats.spearmanr(df[&#x27;satisfacao&#x27;], df[&#x27;sessoes&#x27;])&#10;print(f&quot;Spearman ρ = {rho:.3f}, p = {p_s:.4f}&quot;)&#10;&#10;tau, p_k = stats.kendalltau(df[&#x27;satisfacao&#x27;], df[&#x27;sessoes&#x27;])&#10;print(f&quot;Kendall  τ = {tau:.3f}, p = {p_k:.4f}&quot;)&#10;&#10;res = pg.corr(df[&#x27;satisfacao&#x27;], df[&#x27;sessoes&#x27;], method=&#x27;spearman&#x27;)&#10;print(res[[&#x27;n&#x27;, &#x27;r&#x27;, &#x27;CI95%&#x27;, &#x27;p-val&#x27;, &#x27;power&#x27;]])" markdown="0">
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
