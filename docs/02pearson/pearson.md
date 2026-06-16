---
layout: default
title: Correlação de Pearson
nav_order: 4
parent: Encontros
has_children: false
---

# Enc. 2 — Correlação de Pearson

`scipy.stats.pearsonr · pandas DataFrame.corr(method='pearson')`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/02pearson/slides/index.html#/" title="Correlação de Pearson" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Pense em dois atletas correndo numa pista lado a lado. Quando um acelera, o outro também acelera na mesma proporção; quando um desacelera, o outro acompanha. Isso é **r = +1**: movem-se em perfeita sincronia na mesma direção. Se um acelera e o outro desacelera exatamente na mesma medida, temos **r = −1**. Se cada um faz o que quer, independentemente do outro, **r ≈ 0**. Pearson mede essa sincronia — mas *apenas quando a pista é reta*.

---

## 🎯 Para que serve

Mede a **força** e a **direção** de uma relação *linear* entre duas variáveis numéricas contínuas. O coeficiente *r* vai de −1 a +1.

Em dados conversacionais: *quanto maior o número de turnos em uma sessão, maior o escore de compreensão do estudante?*

---

## 📋 Quando usar

- ✅ Ambas as variáveis são contínuas e numéricas.
- ✅ A relação esperada é **linear** — verificar com scatter plot antes de calcular.
- ✅ Cada variável segue aproximadamente distribuição normal (Shapiro-Wilk).
- ❌ Não usar com dados ordinais (Likert) — use Spearman.
- ❌ Não usar se houver outliers extremos — eles puxam r para si sozinhos.
- ❌ Correlação não implica causalidade.

{: .highlight }
> **Convenção de Cohen (1988):** |r| < 0.10 negligível · 0.10–0.29 pequeno · 0.30–0.49 médio · ≥ 0.50 grande

---

## 🐍 Exemplo Python


Contexto: verificar se o número de turnos por sessão se associa ao escore de compreensão.

<div class="python-runner" data-code="import pandas as pd&#10;from scipy import stats&#10;import matplotlib.pyplot as plt&#10;&#10;df = pd.DataFrame({&#10;    &#x27;turnos&#x27;:      [4,7,3,9,5,11,6,8,2,10],&#10;    &#x27;escore_comp&#x27;: [52,71,48,80,60,85,66,75,40,82]&#10;})&#10;&#10;# Passo 1: sempre visualize antes&#10;df.plot.scatter(x=&#x27;turnos&#x27;, y=&#x27;escore_comp&#x27;, color=&#x27;#c792ea&#x27;,&#10;               title=&#x27;Turnos × Escore de Compreensão&#x27;)&#10;plt.show()&#10;&#10;# Passo 2: calcular&#10;r, p = stats.pearsonr(df[&#x27;turnos&#x27;], df[&#x27;escore_comp&#x27;])&#10;print(f&quot;r = {r:.3f}, p = {p:.4f}&quot;)" markdown="0">
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
| **clássico** | Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Lawrence Erlbaum. |
| **didático** | Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6ª ed.). SAGE. Cap. 8. |
| **python** | McKinney, W. (2022). *Python for Data Analysis* (3ª ed.). O'Reilly. Cap. 13. |
| **artigo** | Mukaka, M. M. (2012). A guide to appropriate use of correlation coefficient in medical research. *Malawi Medical Journal, 24*(3), 69–71. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
