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


<div class="python-runner" data-code="aW1wb3J0IHN0YXRzbW9kZWxzLmZvcm11bGEuYXBpIGFzIHNtZgppbXBvcnQgcGFuZGFzIGFzIHBkCmZyb20gc3RhdHNtb2RlbHMuc3RhdHMub3V0bGllcnNfaW5mbHVlbmNlIGltcG9ydCB2YXJpYW5jZV9pbmZsYXRpb25fZmFjdG9yCgpkZiA9IHBkLkRhdGFGcmFtZSh7CiAgICAnZXNjb3JlX2ZpbmFsJzogIFs3Miw4NSw2MCw5MCw2OCw3OCw4Miw1NSw4OCw3NF0sCiAgICAndXNvX2NoYXRib3QnOiAgIFs1LDksMywxMiw0LDcsMTAsMiwxMSw2XSwKICAgICdtZXRhY29nbmljYW8nOiAgWzYwLDcyLDU1LDgwLDU4LDY4LDc1LDUwLDc4LDY1XSwKICAgICdsZXRyYW1lbnRvX2lhJzogWzQwLDU1LDM1LDY1LDQyLDUyLDYwLDMwLDYyLDQ4XQp9KQoKbW9kZWxvID0gc21mLm9scygnZXNjb3JlX2ZpbmFsIH4gdXNvX2NoYXRib3QgKyBtZXRhY29nbmljYW8gKyBsZXRyYW1lbnRvX2lhJywgZGF0YT1kZikuZml0KCkKcHJpbnQobW9kZWxvLnN1bW1hcnkoKSkKClggPSBkZltbJ3Vzb19jaGF0Ym90JywnbWV0YWNvZ25pY2FvJywnbGV0cmFtZW50b19pYSddXQp2aWYgPSBwZC5EYXRhRnJhbWUoewogICAgJ3ZhcmnDoXZlbCc6IFguY29sdW1ucywKICAgICdWSUYnOiBbdmFyaWFuY2VfaW5mbGF0aW9uX2ZhY3RvcihYLnZhbHVlcywgaSkgZm9yIGkgaW4gcmFuZ2UoWC5zaGFwZVsxXSldCn0pCnByaW50KHZpZik=" markdown="0">
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
