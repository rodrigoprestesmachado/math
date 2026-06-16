---
layout: default
title: Mann-Whitney e Wilcoxon
nav_order: 9
parent: Encontros
has_children: false
---

# Enc. 7 — Mann-Whitney e Wilcoxon

`scipy.stats.mannwhitneyu · wilcoxon · pingouin.mwu()`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/07mann-whitney/slides/index.html#/" title="Mann-Whitney e Wilcoxon" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Em vez de comparar médias, junta todos numa fila ordenada e verifica se um grupo tende a ocupar posições mais altas. Não importa *quanto* mais alto — só *que é mais alto*.

---

## 🎯 Para que serve

Compara a **distribuição de postos** entre dois grupos sem assumir normalidade.

**Mann-Whitney U**: independentes. **Wilcoxon signed-rank**: pareadas.

---

## 📋 Quando usar

- ✅ Dados ordinais (Likert) ou numéricos que violam normalidade.
- ✅ Amostras pequenas (n < 30).
- ✅ Outliers que não devem ser removidos.
- ❌ Não testa diferença de médias — testa diferença de distribuições.

{: .highlight }
> **Tamanho de efeito r:** r = Z / √N. Pequeno ≥ 0.10 · médio ≥ 0.30 · grande ≥ 0.50.

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="aW1wb3J0IHBpbmdvdWluIGFzIHBnCmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IHdpbGNveG9uCgpncnVwb19hID0gWzMsNSw0LDYsNyw0LDVdCmdydXBvX2IgPSBbMiwzLDEsNCwzLDIsM10KCnJlc19tdyA9IHBnLm13dShncnVwb19hLCBncnVwb19iLCBhbHRlcm5hdGl2ZT0ndHdvLXNpZGVkJykKcHJpbnQoIk1hbm4tV2hpdG5leToiKQpwcmludChyZXNfbXdbWydVLXZhbCcsICdwLXZhbCcsICdSQkMnLCAnQ0xFUyddXSkKCnByZSAgPSBbMyw1LDQsNiw0LDNdCnBvcyAgPSBbNSw2LDYsNyw2LDVdCnN0YXQsIHBfdyA9IHdpbGNveG9uKHByZSwgcG9zLCBhbHRlcm5hdGl2ZT0ndHdvLXNpZGVkJykKcHJpbnQoZiJcbldpbGNveG9uOiBXID0ge3N0YXQ6LjBmfSwgcCA9IHtwX3c6LjRmfSIp" markdown="0">
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
| **seminal** | Mann, H. B., & Whitney, D. R. (1947). *Annals of Mathematical Statistics, 18*(1), 50–60. |
| **seminal** | Wilcoxon, F. (1945). *Biometrics Bulletin, 1*(6), 80–83. |
| **didático** | Field, A. (2024). *Discovering Statistics*. Cap. 7. |
| **efeito** | Kerby, D. S. (2014). The simple difference formula. *Comprehensive Psychology, 3*. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
