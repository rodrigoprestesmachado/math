---
layout: default
title: ANOVA de uma via e Kruskal-Wallis
nav_order: 10
parent: Encontros
has_children: false
---

# Enc. 8 — ANOVA de uma via e Kruskal-Wallis

`pingouin.anova() · scipy.stats.kruskal · scikit_posthocs`
{: .fs-5 .fw-300 }

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

[▶ Abrir código executável](content.html){: .btn .btn-primary }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/08anova/slides/index.html#/" title="ANOVA de uma via e Kruskal-Wallis" width="90%" height="500" style="border:none;"></iframe>
</center>

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
