<!-- .slide: class="title-slide" -->

# Enc. 8

## ANOVA de uma via e Kruskal-Wallis

⚖️ Bloco 2 — Comparação

<p class="small">pingouin.anova() · scipy.stats.kruskal · scikit_posthocs</p>

---

## 🍊 Metáfora

Vários testes t acumulam erro (quase 15% com 3 comparações). ANOVA faz uma só pergunta: *há pelo menos um grupo diferente?* Compara variação *entre* vs. *dentro* dos grupos. Se F for significativo, o **pós-hoc de Tukey** indica onde.

---

## 🎯 Para que serve

Compara médias (ANOVA) ou distribuições de postos (Kruskal-Wallis) entre **três ou mais grupos**.

---

## 📋 Quando usar

- ✅ Comparar ≥ 3 grupos independentes.
- ✅ <strong>ANOVA:</strong> dados normais e variâncias homogêneas. Reporte η².
- ✅ <strong>Kruskal-Wallis:</strong> dados ordinais ou não-normais. Pós-hoc: Dunn.
- ❌ ANOVA significativa sem pós-hoc não diz onde está a diferença.

---

## 🐍 Exemplo Python

```python
import pingouin as pg
import pandas as pd
from scipy.stats import kruskal

df = pd.DataFrame({
    'perguntas': [3,4,2,5, 7,8,6,9, 12,14,11,13],
    'perfil':    ['passivo']*4 + ['ativo']*4 + ['intensivo']*4
})

aov = pg.anova(data=df, dv='perguntas', between='perfil', detailed=True)
print(aov[['Source','F','p-unc','np2']])

ph = pg.pairwise_tukey(data=df, dv='perguntas', between='perfil')
print(ph[['A','B','diff','p-tukey','hedges']])

H, p_k = kruskal(
    df[df.perfil=='passivo'].perguntas,
    df[df.perfil=='ativo'].perguntas,
    df[df.perfil=='intensivo'].perguntas
)
print(f"\nKruskal-Wa
...
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **seminal:** Fisher, R. A. (1925). *Statistical Methods for Research Workers*.
- **seminal:** Kruskal, W. H., & Wallis, W. A. (1952). *Journal of the American Statistical Association, 47*(260), 583–621.
- **didático:** Field, A. (2024). *Discovering Statistics*. Caps. 12–13.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../anova.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
