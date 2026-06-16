<!-- .slide: class="title-slide" -->

# Enc. 12

## Regressão Logística (binária e ordinal)

📈 Bloco 3 — Predição

<p class="small">statsmodels Logit() · mord · sklearn ROC/AUC</p>

---

## 🍊 Metáfora

Para prever *engajou ou não engajou*, a logística usa uma sigmoid que espreme valores em [0, 1] — probabilidade. Coeficientes como **odds ratios**: OR = 2 significa chances dobradas. A **curva ROC** mede a qualidade do modelo (AUC).

---

## 🎯 Para que serve

Modelar desfechos **categóricos**: binária (engajou/não) ou ordinal (baixo/médio/alto).

---

## 📋 Quando usar

- ✅ <strong>Binária:</strong> duas categorias mutuamente exclusivas.
- ✅ <strong>Ordinal:</strong> 3+ categorias ordenadas.
- ✅ AUC &gt; 0.70 aceitável · &gt; 0.80 bom · &gt; 0.90 excelente.
- ❌ Não use regressão linear para desfecho binário.

---

## 🐍 Exemplo Python

```python
import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score

df = pd.DataFrame({
    'engajou':     [1,0,1,1,0,1,0,1,0,1,0,1],
    'uso_chatbot': [8,2,9,7,3,10,1,8,4,9,2,11],
    'metacognicao':[65,40,70,68,38,75,35,72,42,78,33,80]
})

X = sm.add_constant(df[['uso_chatbot', 'metacognicao']])
modelo = sm.Logit(df['engajou'], X).fit(disp=0)
print(modelo.summary())

OR = np.exp(modelo.params)
print("\nOdds Ratios:")
print(OR.round(3))

y_pred = modelo.predict(X)
auc = roc_auc_score(df['engajou'], y_pred)
print(f"\nAUC = {auc:.3f}")
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **referência:** Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). *Applied Logistic Regression* (3ª ed.).
- **didático:** Field, A. (2024). *Discovering Statistics*. Cap. 20.
- **ROC:** Fawcett, T. (2006). An introduction to ROC analysis. *Pattern Recognition Letters, 27*(8), 861–874.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../regressao-logistica.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
