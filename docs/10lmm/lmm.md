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

[▶ Abrir código executável](content.html){: .btn .btn-primary }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/10lmm/slides/index.html#/" title="Modelos Lineares Mistos (LMM)" width="90%" height="500" style="border:none;"></iframe>
</center>

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
