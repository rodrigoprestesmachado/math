<!-- .slide: class="title-slide" -->

# Enc. 5

## Correlação Parcial e Análise Fatorial

🔗 Bloco 1 — Associação

<p class="small">pingouin.partial_corr() · factor_analyzer</p>

---

## 🍊 Metáfora

**Correlação parcial — o filtro de ruído:** como usar um equalizador para *silenciar o baixo* e ouvir a guitarra — remove o efeito de uma variável de confusão.

**Análise Fatorial — o organizador de gavetas:** agrupa variáveis que se movem juntas em fatores latentes interpretáveis (ex.: "metacognição").

---

## 🎯 Para que serve

**Correlação parcial:** isola a relação entre X e Y removendo o efeito de uma terceira variável.

**EFA:** reduz muitas variáveis correlacionadas a poucos fatores latentes. Valida instrumentos.

---

## 📋 Quando usar

- ✅ <strong>Parcial:</strong> quando há variável de confusão (ex.: conhecimento prévio).
- ✅ <strong>EFA:</strong> quando há ≥ 5 variáveis correlacionadas e suspeita-se de construtos latentes.
- ✅ <strong>EFA:</strong> n ≥ 100; regra de 10 sujeitos por item.
- ❌ EFA não é para predição — use regressão.

---

## 🐍 Exemplo Python

```python
import pingouin as pg
import pandas as pd

df = pd.DataFrame({
    'uso_chatbot':   [3,7,2,9,5,11,4,8],
    'aprendizagem':  [55,70,50,82,63,88,58,76],
    'conhec_previo': [40,55,35,70,50,75,45,60]
})

r_bruta = pg.corr(df['uso_chatbot'], df['aprendizagem'])
print("Pearson bruto:      r =", round(r_bruta['r'].values[0], 3))

r_parcial = pg.partial_corr(
    data=df, x='uso_chatbot', y='aprendizagem', covar='conhec_previo'
)
print("Pearson parcial:    r =", round(r_parcial['r'].values[0], 3))
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **didático:** Tabachnick, B. G., & Fidell, L. S. (2019). *Using Multivariate Statistics* (7ª ed.). Cap. 13.
- **aplicado:** Costello, A. B., & Osborne, J. W. (2005). Best practices in exploratory factor analysis. *Practical Assessment, Research & Evaluation, 10*(7).
- **python:** Biggs, J. (2023). *factor_analyzer* package documentation.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../parcial-fatorial.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
