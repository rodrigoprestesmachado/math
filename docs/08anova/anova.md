---
layout: default
title: ANOVA de uma via e Kruskal-Wallis
nav_order: 3
parent: Comparação
has_children: false
---

# Enc. 8 — ANOVA de uma via e Kruskal-Wallis

`pingouin.anova() · scipy.stats.kruskal · scikit_posthocs`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/08anova/slides/index.html#/" title="ANOVA de uma via e Kruskal-Wallis" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Vários testes t acumulam erro (quase 15% com 3 comparações). ANOVA faz uma só pergunta: *há pelo menos um grupo diferente?* Compara variação *entre* vs. *dentro* dos grupos. Se F for significativo, o **pós-hoc de Tukey** indica onde.

---

## 🎯 Para que serve

Compara médias (ANOVA) ou distribuições de postos (Kruskal-Wallis) entre **três ou mais grupos**.

---

## 📋 Quando usar

- ✅ Comparar ≥ 3 grupos independentes.
- ✅ **ANOVA:** dados normais e variâncias homogêneas. Reporte η².
- ✅ **Kruskal-Wallis:** dados ordinais ou não-normais. Pós-hoc: Dunn.
- ❌ ANOVA significativa sem pós-hoc não diz onde está a diferença.

{: .highlight }
> **Eta-quadrado (η²):** pequeno = 0.01 · médio = 0.06 · grande = 0.14

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="aW1wb3J0IHBpbmdvdWluIGFzIHBnCmltcG9ydCBwYW5kYXMgYXMgcGQKZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQga3J1c2thbAoKZGYgPSBwZC5EYXRhRnJhbWUoewogICAgJ3Blcmd1bnRhcyc6IFszLDQsMiw1LCA3LDgsNiw5LCAxMiwxNCwxMSwxM10sCiAgICAncGVyZmlsJzogICAgWydwYXNzaXZvJ10qNCArIFsnYXRpdm8nXSo0ICsgWydpbnRlbnNpdm8nXSo0Cn0pCgphb3YgPSBwZy5hbm92YShkYXRhPWRmLCBkdj0ncGVyZ3VudGFzJywgYmV0d2Vlbj0ncGVyZmlsJywgZGV0YWlsZWQ9VHJ1ZSkKcHJpbnQoYW92W1snU291cmNlJywnRicsJ3AtdW5jJywnbnAyJ11dKQoKcGggPSBwZy5wYWlyd2lzZV90dWtleShkYXRhPWRmLCBkdj0ncGVyZ3VudGFzJywgYmV0d2Vlbj0ncGVyZmlsJykKcHJpbnQocGhbWydBJywnQicsJ2RpZmYnLCdwLXR1a2V5JywnaGVkZ2VzJ11dKQoKSCwgcF9rID0ga3J1c2thbCgKICAgIGRmW2RmLnBlcmZpbD09J3Bhc3Npdm8nXS5wZXJndW50YXMsCiAgICBkZltkZi5wZXJmaWw9PSdhdGl2byddLnBlcmd1bnRhcywKICAgIGRmW2RmLnBlcmZpbD09J2ludGVuc2l2byddLnBlcmd1bnRhcwopCnByaW50KGYiXG5LcnVza2FsLVdhbGxpczogSCA9IHtIOi4zZn0sIHAgPSB7cF9rOi40Zn0iKQ==" markdown="0">
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
| **seminal** | Fisher, R. A. (1925). *Statistical Methods for Research Workers*. |
| **seminal** | Kruskal, W. H., & Wallis, W. A. (1952). *Journal of the American Statistical Association, 47*(260), 583–621. |
| **didático** | Field, A. (2024). *Discovering Statistics*. Caps. 12–13. |
| **python** | Pohlert, T. (2014). PMCMR package — lógica do pós-hoc de Dunn. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
