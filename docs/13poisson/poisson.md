---
layout: default
title: Regressão de Poisson e Binomial Negativa
nav_order: 15
parent: Encontros
has_children: false
---

# Enc. 13 — Regressão de Poisson e Binomial Negativa

`statsmodels poisson() · negativebinomial()`
{: .fs-5 .fw-300 }

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Contagens (perguntas ao chatbot) são inteiras e nunca negativas. Poisson modela a taxa de eventos. Se a variância explode (superdispersão), a **Binomial Negativa** adiciona folga extra.

---

## 🎯 Para que serve

Modelar desfechos de **contagem**: turnos, perguntas, mensagens. Poisson para equidispersão; BN para superdispersão.

---

## 📋 Quando usar

- ✅ Desfecho são contagens inteiras não-negativas.
- ✅ **Poisson:** variância/média ≈ 1.
- ✅ **BN:** índice de dispersão > 1.5.
- ✅ Comparar via AIC: menor = melhor.
- ❌ Não use regressão linear para contagens.

{: .highlight }
> **Interpretar coeficientes:** exp(coef) = Risk Ratio. RR = 1.3 → 30% mais eventos por unidade.

---

## 🐍 Exemplo Python

[▶ Abrir código executável](content.html){: .btn .btn-primary }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/13poisson/slides/index.html#/" title="Regressão de Poisson e Binomial Negativa" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 📚 Referências

| | |
|:--|:--|
| **referência** | Cameron, A. C., & Trivedi, P. K. (2013). *Regression Analysis of Count Data* (2ª ed.). |
| **didático** | Hilbe, J. M. (2011). *Negative Binomial Regression* (2ª ed.). |
| **comparação** | Ver Hoef, J. M., & Boveng, P. L. (2007). Quasi-Poisson vs. negative binomial. *Ecology, 88*(11), 2766–2772. |
| **educação** | Coxe, S., West, S. G., & Aiken, L. S. (2009). The analysis of count data. *Journal of Personality Assessment, 91*(2), 121–136. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
