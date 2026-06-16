---
layout: default
title: Correlação Parcial e Análise Fatorial
nav_order: 7
parent: Encontros
has_children: false
---

# Enc. 5 — Correlação Parcial e Análise Fatorial

`pingouin.partial_corr() · factor_analyzer`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/05parcial-fatorial/slides/index.html#/" title="Correlação Parcial e Análise Fatorial" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Duas metáforas, um encontro**
>
> **Correlação parcial — o filtro de ruído:** como usar um equalizador para *silenciar o baixo* e ouvir a guitarra — remove o efeito de uma variável de confusão.

**Análise Fatorial — o organizador de gavetas:** agrupa variáveis que se movem juntas em fatores latentes interpretáveis (ex.: "metacognição").

---

## 🎯 Para que serve

**Correlação parcial:** isola a relação entre X e Y removendo o efeito de uma terceira variável.

**EFA:** reduz muitas variáveis correlacionadas a poucos fatores latentes. Valida instrumentos.

---

## 📋 Quando usar

- ✅ **Parcial:** quando há variável de confusão (ex.: conhecimento prévio).
- ✅ **EFA:** quando há ≥ 5 variáveis correlacionadas e suspeita-se de construtos latentes.
- ✅ **EFA:** n ≥ 100; regra de 10 sujeitos por item.
- ❌ EFA não é para predição — use regressão.

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="import pingouin as pg&#10;import pandas as pd&#10;&#10;df = pd.DataFrame({&#10;    &#x27;uso_chatbot&#x27;:   [3,7,2,9,5,11,4,8],&#10;    &#x27;aprendizagem&#x27;:  [55,70,50,82,63,88,58,76],&#10;    &#x27;conhec_previo&#x27;: [40,55,35,70,50,75,45,60]&#10;})&#10;&#10;r_bruta = pg.corr(df[&#x27;uso_chatbot&#x27;], df[&#x27;aprendizagem&#x27;])&#10;print(&quot;Pearson bruto:      r =&quot;, round(r_bruta[&#x27;r&#x27;].values[0], 3))&#10;&#10;r_parcial = pg.partial_corr(&#10;    data=df, x=&#x27;uso_chatbot&#x27;, y=&#x27;aprendizagem&#x27;, covar=&#x27;conhec_previo&#x27;&#10;)&#10;print(&quot;Pearson parcial:    r =&quot;, round(r_parcial[&#x27;r&#x27;].values[0], 3))" markdown="0">
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
| **didático** | Tabachnick, B. G., & Fidell, L. S. (2019). *Using Multivariate Statistics* (7ª ed.). Cap. 13. |
| **aplicado** | Costello, A. B., & Osborne, J. W. (2005). Best practices in exploratory factor analysis. *Practical Assessment, Research & Evaluation, 10*(7). |
| **python** | Biggs, J. (2023). *factor_analyzer* package documentation. |
| **conceitual** | MacCallum, R. C. (2009). Factor analysis. In *The SAGE Handbook of Quantitative Methods in Psychology*. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
