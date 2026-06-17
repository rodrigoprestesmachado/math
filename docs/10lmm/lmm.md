---
layout: default
title: Modelos Lineares Mistos (LMM)
nav_order: 5
parent: Comparação
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


<div class="python-runner" data-code="aW1wb3J0IHN0YXRzbW9kZWxzLmZvcm11bGEuYXBpIGFzIHNtZgppbXBvcnQgcGFuZGFzIGFzIHBkCmltcG9ydCBudW1weSBhcyBucAoKbnAucmFuZG9tLnNlZWQoNDIpCm5fZXN0LCBuX3NlcyA9IDIwLCA1CgpkZiA9IHBkLkRhdGFGcmFtZSh7CiAgICAnZXN0dWRhbnRlJzogbnAucmVwZWF0KHJhbmdlKG5fZXN0KSwgbl9zZXMpLAogICAgJ3Nlc3Nhbyc6ICAgIGxpc3QocmFuZ2Uobl9zZXMpKSAqIG5fZXN0LAogICAgJ3R1cm5vcyc6ICAgIG5wLnJhbmRvbS5wb2lzc29uKDYsIG5fZXN0Km5fc2VzKSwKICAgICdlc2NvcmUnOiAgICBucC5yYW5kb20ubm9ybWFsKDcwLCAxMCwgbl9lc3Qqbl9zZXMpCn0pCmRmWydlc2NvcmUnXSArPSBkZlsndHVybm9zJ10gKiAxLjUKCm1vZGVsbyA9IHNtZi5taXhlZGxtKCJlc2NvcmUgfiB0dXJub3MiLCBkYXRhPWRmLCBncm91cHM9ZGZbImVzdHVkYW50ZSJdKS5maXQocmVtbD1UcnVlKQpwcmludChtb2RlbG8uc3VtbWFyeSgpKQ==" markdown="0">
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
