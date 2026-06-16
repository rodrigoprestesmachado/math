---
layout: default
title: Qui-quadrado e V de Cramér
nav_order: 6
parent: Encontros
has_children: false
---

# Enc. 4 — Qui-quadrado e V de Cramér

`scipy.stats.chi2_contingency · cálculo manual de V`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/04qui-quadrado/slides/index.html#/" title="Qui-quadrado e V de Cramér" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Imagine um cardápio com três pratos (factual, conceitual, procedimental) e três tipos de clientes. O qui-quadrado compara o *observado* com o *esperado* se não houvesse relação. O **V de Cramér** quantifica a força dessa associação, livre do tamanho amostral.

---

## 🎯 Para que serve

Testa se duas variáveis **categóricas** são independentes. O **p-valor do χ²** indica significância; o **V de Cramér** quantifica a força.

Exemplo: *o tipo de pergunta ao chatbot varia conforme o perfil de uso do estudante?*

---

## 📋 Quando usar

- ✅ Ambas as variáveis são **categóricas nominais**.
- ✅ Frequência esperada ≥ 5 em pelo menos 80% das células (senão, Fisher exato).
- ❌ Não use com variáveis ordinais — Spearman é mais adequado.
- ❌ Nunca interpretar apenas o p-valor: sempre reporte V de Cramér.

{: .highlight }
> **V de Cramér:** pequeno ≈ 0.10 · médio ≈ 0.30 · grande ≈ 0.50

---

## 🐍 Exemplo Python


<div class="python-runner" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false">import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

tabela = pd.DataFrame(
    [[30,15,10],[20,25,18],[10,20,35]],
    index   = ['factual','conceitual','procedimental'],
    columns = ['passivo','ativo','intensivo']
)
print(tabela, "\n")

chi2, p, gl, esperadas = chi2_contingency(tabela)
print(f"χ² = {chi2:.3f}  gl = {gl}  p = {p:.4f}")

n = tabela.values.sum()
k = min(tabela.shape) - 1
V = np.sqrt(chi2 / (n * k))
efeito = 'pequeno' if V &lt; .3 else 'médio' if V &lt; .5 else 'grande'
print(f"V de Cramér = {V:.3f}  → efeito {efeito}")</textarea>
  <pre class="code-output"></pre>
</div>

---

## 📚 Referências

| | |
|:--|:--|
| **seminal** | Cramér, H. (1946). *Mathematical Methods of Statistics*. Princeton University Press. |
| **didático** | Agresti, A. (2013). *Categorical Data Analysis* (3ª ed.). Wiley. |
| **tamanho efeito** | Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Cap. 7. |
| **crítico** | Kim, H. Y. (2017). Chi-squared test and Fisher's exact test. *Restorative Dentistry & Endodontics, 42*(2), 152–155. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
