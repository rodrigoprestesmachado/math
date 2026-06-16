<!-- .slide: class="title-slide" -->

# Enc. 11

## Regressão Linear (simples e múltipla)

📈 Bloco 3 — Predição

<p class="small">statsmodels.formula.api.ols() · sklearn LinearRegression</p>

---

## 🍊 Metáfora

A regressão traça a *linha reta que erra menos* para todos os pontos. A múltipla adiciona dimensões: cada coeficiente é o efeito *único* da variável, mantendo as outras constantes.

---

## 🎯 Para que serve

Modelar e predizer um desfecho **numérico contínuo** a partir de preditores.

---

## 📋 Quando usar

- ✅ Desfecho numérico contínuo.
- ✅ Relação linear entre preditores e desfecho.
- ✅ Resíduos normais e homocedásticos.
- ✅ VIF &gt; 5 indica multicolinearidade.

---

## 🐍 Exemplo Python

```python
import statsmodels.formula.api as smf
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.DataFrame({
    'escore_final':  [72,85,60,90,68,78,82,55,88,74],
    'uso_chatbot':   [5,9,3,12,4,7,10,2,11,6],
    'metacognicao':  [60,72,55,80,58,68,75,50,78,65],
    'letramento_ia': [40,55,35,65,42,52,60,30,62,48]
})

modelo = smf.ols('escore_final ~ uso_chatbot + metacognicao + letramento_ia', data=df).fit()
print(modelo.summary())

X = df[['uso_chatbot','metacognicao','letramento_ia']]
vif = pd.DataFrame({
    'variável': X.columns,
    'VIF': [v...
```

<div class="destaque">
Código <strong>executável</strong> na página de conteúdo — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **referência:** Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8ª ed.). Cap. 4.
- **didático:** James, G., et al. (2023). *An Introduction to Statistical Learning* (2ª ed.). Cap. 3.
- **VIF:** O'Brien, R. M. (2007). A caution regarding rules of thumb for VIF. *Quality & Quantity, 41*, 673–690.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../content.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
