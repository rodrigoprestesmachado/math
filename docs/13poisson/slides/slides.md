<!-- .slide: class="title-slide" -->

# Enc. 13

## Regressão de Poisson e Binomial Negativa

📈 Bloco 3 — Predição

<p class="small">statsmodels poisson() · negativebinomial()</p>

---

## 🍊 Metáfora

Contagens (perguntas ao chatbot) são inteiras e nunca negativas. Poisson modela a taxa de eventos. Se a variância explode (superdispersão), a **Binomial Negativa** adiciona folga extra.

---

## 🎯 Para que serve

Modelar desfechos de **contagem**: turnos, perguntas, mensagens. Poisson para equidispersão; BN para superdispersão.

---

## 📋 Quando usar

- ✅ Desfecho são contagens inteiras não-negativas.
- ✅ <strong>Poisson:</strong> variância/média ≈ 1.
- ✅ <strong>BN:</strong> índice de dispersão &gt; 1.5.
- ✅ Comparar via AIC: menor = melhor.

---

## 🐍 Exemplo Python

```python
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np

np.random.seed(7)
n = 80
df = pd.DataFrame({
    'perguntas':    np.random.negative_binomial(2, 0.3, n),
    'metacognicao': np.random.normal(60, 10, n),
    'tempo_sessao': np.random.normal(20, 5, n)
})

media, var = df.perguntas.mean(), df.perguntas.var()
print(f"Média={media:.2f}  Variância={var:.2f}  Índice={var/media:.2f}")

mod_p  = smf.poisson('perguntas ~ metacognicao + tempo_sessao', data=df).fit(disp=0)
mod_nb = smf.negativebinomial('perguntas ~ metacognicao + tempo_sessao', data=df).fit(disp=0)

print(f"AI...
```

<div class="destaque">
Código <strong>executável</strong> na página de conteúdo — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **referência:** Cameron, A. C., & Trivedi, P. K. (2013). *Regression Analysis of Count Data* (2ª ed.).
- **didático:** Hilbe, J. M. (2011). *Negative Binomial Regression* (2ª ed.).
- **comparação:** Ver Hoef, J. M., & Boveng, P. L. (2007). Quasi-Poisson vs. negative binomial. *Ecology, 88*(11), 2766–2772.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../content.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
