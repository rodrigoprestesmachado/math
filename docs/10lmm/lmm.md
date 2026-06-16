---
layout: default
title: Modelos Lineares Mistos (LMM)
nav_order: 12
parent: Encontros
has_children: false
---

# Enc. 10 — Modelos Lineares Mistos (LMM)

`statsmodels.formula.api.mixedlm · pingouin.mixed_anova()`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/10lmm/slides/index.html#/" title="Modelos Lineares Mistos (LMM)" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Dados aninhados (mensagens em sessões, sessões em estudantes) violam independência. LMM tem **efeitos fixos** (o efeito na população) e **efeitos aleatórios** (variabilidade de cada estudante/turma). Cada sujeito ganha seu próprio ponto de partida.

---

## 🎯 Para que serve

Modelar dados com estrutura **hierárquica**: mensagens → sessões → estudantes → turmas.

---

## 📋 Quando usar

- ✅ Observações aninhadas em grupos.
- ✅ Dados longitudinais com faltantes ou grupos desiguais.
- ✅ Quando ANOVA MR não converge.
- ❌ Comece com modelos simples (só intercepto aleatório).

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="import statsmodels.formula.api as smf&#10;import pandas as pd&#10;import numpy as np&#10;&#10;np.random.seed(42)&#10;n_est, n_ses = 20, 5&#10;&#10;df = pd.DataFrame({&#10;    &#x27;estudante&#x27;: np.repeat(range(n_est), n_ses),&#10;    &#x27;sessao&#x27;:    list(range(n_ses)) * n_est,&#10;    &#x27;turnos&#x27;:    np.random.poisson(6, n_est*n_ses),&#10;    &#x27;escore&#x27;:    np.random.normal(70, 10, n_est*n_ses)&#10;})&#10;df[&#x27;escore&#x27;] += df[&#x27;turnos&#x27;] * 1.5&#10;&#10;modelo = smf.mixedlm(&quot;escore ~ turnos&quot;, data=df, groups=df[&quot;estudante&quot;]).fit(reml=True)&#10;print(modelo.summary())" markdown="0">
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
| **referência** | Gelman, A., & Hill, J. (2007). *Data Analysis Using Regression and Multilevel Models*. |
| **acessível** | Winter, B. (2019). *Statistics for Linguists*. Routledge. |
| **educação** | Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical Linear Models* (2ª ed.). |
| **python** | Seabold, S., & Perktold, J. (2010). Statsmodels. *SciPy Proceedings*. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
