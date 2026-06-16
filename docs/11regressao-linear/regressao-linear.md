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

[▶ Abrir código executável](content.html){: .btn .btn-primary }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/11regressao-linear/slides/index.html#/" title="Regressão Linear (simples e múltipla)" width="90%" height="500" style="border:none;"></iframe>
</center>

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
