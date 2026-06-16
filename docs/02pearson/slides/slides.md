<!-- .slide: class="title-slide" -->

# Enc. 2

## Correlação de Pearson

🔗 Bloco 1 — Associação

<p class="small">scipy.stats.pearsonr · pandas DataFrame.corr(method='pearson')</p>

---

## 🍊 Metáfora

Pense em dois atletas correndo numa pista lado a lado. Quando um acelera, o outro também acelera na mesma proporção; quando um desacelera, o outro acompanha. Isso é **r = +1**: movem-se em perfeita sincronia na mesma direção. Se um acelera e o outro desacelera exatamente na mesma medida, temos **r = −1**. Se cada um faz o que quer, independentemente do outro, **r ≈ 0**. Pearson mede essa sincronia — mas *apenas quando a pista é reta*.

---

## 🎯 Para que serve

Mede a **força** e a **direção** de uma relação *linear* entre duas variáveis numéricas contínuas. O coeficiente *r* vai de −1 a +1.
Em dados conversacionais: *quanto maior o número de turnos em uma sessão, maior o escore de compreensão do estudante?*

---

## 📋 Quando usar

- ✅ Ambas as variáveis são contínuas e numéricas.
- ✅ A relação esperada é <strong>linear</strong> — verificar com scatter plot antes de calcular.
- ✅ Cada variável segue aproximadamente distribuição normal (Shapiro-Wilk).
- ❌ Não usar com dados ordinais (Likert) — use Spearman.

---

## 🐍 Exemplo Python

```python
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'turnos':      [4,7,3,9,5,11,6,8,2,10],
    'escore_comp': [52,71,48,80,60,85,66,75,40,82]
})

# Passo 1: sempre visualize antes
df.plot.scatter(x='turnos', y='escore_comp', color='#c792ea',
               title='Turnos × Escore de Compreensão')
plt.show()

# Passo 2: calcular
r, p = stats.pearsonr(df['turnos'], df['escore_comp'])
print(f"r = {r:.3f}, p = {p:.4f}")
```

<div class="destaque">
Código <strong>executável</strong> na página de conteúdo — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **clássico:** Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Lawrence Erlbaum.
- **didático:** Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6ª ed.). SAGE. Cap. 8.
- **python:** McKinney, W. (2022). *Python for Data Analysis* (3ª ed.). O'Reilly. Cap. 13.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../content.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
