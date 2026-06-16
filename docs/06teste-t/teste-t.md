---
layout: default
title: Teste t (independente e pareado)
nav_order: 8
parent: Encontros
has_children: false
---

# Enc. 6 — Teste t (independente e pareado)

`pingouin.ttest() · scipy.stats.ttest_ind · ttest_rel`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/06teste-t/slides/index.html#/" title="Teste t (independente e pareado)" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Duas balanças: escores com feedback vs. sem feedback. O teste t pergunta se a diferença é grande o suficiente para não ser mero acaso. O **Cohen's d** mede o quanto as distribuições se separam. O **t pareado** mede a mudança nas *mesmas* pessoas antes e depois.

---

## 🎯 Para que serve

Compara a **média** de uma variável numérica entre **exatamente dois grupos**.

---

## 📋 Quando usar

- ✅ Variável dependente contínua e exatamente dois grupos.
- ✅ Verificar normalidade (Shapiro-Wilk) e homocedasticidade (Levene).
- ✅ Se Levene rejeitar → usar Welch (padrão no scipy).
- ❌ Se normalidade violada com n pequeno → Mann-Whitney.
- ⚠️ Sempre reporte Cohen's d além do p-valor.

---

## 🐍 Exemplo Python


<div class="python-runner" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false">import pingouin as pg
from scipy.stats import shapiro, levene

feedback     = [72,85,78,90,68,82,76,88]
sem_feedback = [60,65,70,58,63,72,55,67]

_, p_n1 = shapiro(feedback);     print(f"Shapiro G1: p={p_n1:.3f}")
_, p_n2 = shapiro(sem_feedback);  print(f"Shapiro G2: p={p_n2:.3f}")
_, p_lv = levene(feedback, sem_feedback); print(f"Levene:     p={p_lv:.3f}")

res = pg.ttest(feedback, sem_feedback, paired=False, correction='auto')
print(res[['T', 'dof', 'p-val', 'cohen-d', 'power']])</textarea>
  <pre class="code-output"></pre>
</div>

---

## 📚 Referências

| | |
|:--|:--|
| **seminal** | Student [Gosset, W. S.] (1908). The probable error of a mean. *Biometrika, 6*(1), 1–25. |
| **tamanho efeito** | Cohen, J. (1988). *Statistical Power Analysis*. Cap. 2. |
| **didático** | Field, A. (2024). *Discovering Statistics*. Cap. 10. |
| **crítico** | Sullivan, G. M., & Feinn, R. (2012). Using effect size. *Journal of Graduate Medical Education, 4*(3), 279–282. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
