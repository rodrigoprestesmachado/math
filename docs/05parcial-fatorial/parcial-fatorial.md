---
layout: default
title: Correlação Parcial e Análise Fatorial
nav_order: 7
parent: Encontros
has_children: false
---

# Enc. 5 — Correlação Parcial e Análise Fatorial

`pingouin.partial_corr() · factor_analyzer`
{: .fs-5 .fw-300 }

---

## 🍊 Metáfora

> **Duas metáforas, um encontro**
>
> **Correlação parcial — o filtro de ruído:** como usar um equalizador para *silenciar o baixo* e ouvir a guitarra — remove o efeito de uma variável de confusão.

**Análise Fatorial — o organizador de gavetas:** agrupa variáveis que se movem juntas em fatores latentes interpretáveis (ex.: "metacognição").

---

## 🎯 Para que serve

**Correlação parcial:** isola a relação entre X e Y removendo o efeito de uma terceira variável.

**EFA:** reduz muitas variáveis correlacionadas a poucos fatores latentes. Valida instrumentos.

---

## 📋 Quando usar

- ✅ **Parcial:** quando há variável de confusão (ex.: conhecimento prévio).
- ✅ **EFA:** quando há ≥ 5 variáveis correlacionadas e suspeita-se de construtos latentes.
- ✅ **EFA:** n ≥ 100; regra de 10 sujeitos por item.
- ❌ EFA não é para predição — use regressão.

---

## 🐍 Exemplo Python

[▶ Abrir código executável](content.html){: .btn .btn-primary }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/05parcial-fatorial/slides/index.html#/" title="Correlação Parcial e Análise Fatorial" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 📚 Referências

| | |
|:--|:--|
| **didático** | Tabachnick, B. G., & Fidell, L. S. (2019). *Using Multivariate Statistics* (7ª ed.). Cap. 13. |
| **aplicado** | Costello, A. B., & Osborne, J. W. (2005). Best practices in exploratory factor analysis. *Practical Assessment, Research & Evaluation, 10*(7). |
| **python** | Biggs, J. (2023). *factor_analyzer* package documentation. |
| **conceitual** | MacCallum, R. C. (2009). Factor analysis. In *The SAGE Handbook of Quantitative Methods in Psychology*. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
