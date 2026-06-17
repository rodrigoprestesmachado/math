---
layout: default
title: Teste t (independente e pareado)
nav_order: 1
parent: Comparação
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


<div class="python-runner" data-code="aW1wb3J0IHBpbmdvdWluIGFzIHBnCmZyb20gc2NpcHkuc3RhdHMgaW1wb3J0IHNoYXBpcm8sIGxldmVuZQoKZmVlZGJhY2sgICAgID0gWzcyLDg1LDc4LDkwLDY4LDgyLDc2LDg4XQpzZW1fZmVlZGJhY2sgPSBbNjAsNjUsNzAsNTgsNjMsNzIsNTUsNjddCgpfLCBwX24xID0gc2hhcGlybyhmZWVkYmFjayk7ICAgICBwcmludChmIlNoYXBpcm8gRzE6IHA9e3BfbjE6LjNmfSIpCl8sIHBfbjIgPSBzaGFwaXJvKHNlbV9mZWVkYmFjayk7ICBwcmludChmIlNoYXBpcm8gRzI6IHA9e3BfbjI6LjNmfSIpCl8sIHBfbHYgPSBsZXZlbmUoZmVlZGJhY2ssIHNlbV9mZWVkYmFjayk7IHByaW50KGYiTGV2ZW5lOiAgICAgcD17cF9sdjouM2Z9IikKCnJlcyA9IHBnLnR0ZXN0KGZlZWRiYWNrLCBzZW1fZmVlZGJhY2ssIHBhaXJlZD1GYWxzZSwgY29ycmVjdGlvbj0nYXV0bycpCnByaW50KHJlc1tbJ1QnLCAnZG9mJywgJ3AtdmFsJywgJ2NvaGVuLWQnLCAncG93ZXInXV0p" markdown="0">
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
| **seminal** | Student [Gosset, W. S.] (1908). The probable error of a mean. *Biometrika, 6*(1), 1–25. |
| **tamanho efeito** | Cohen, J. (1988). *Statistical Power Analysis*. Cap. 2. |
| **didático** | Field, A. (2024). *Discovering Statistics*. Cap. 10. |
| **crítico** | Sullivan, G. M., & Feinn, R. (2012). Using effect size. *Journal of Graduate Medical Education, 4*(3), 279–282. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
