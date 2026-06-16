<!-- .slide: class="title-slide" -->

# Enc. 9

## ANOVA Fatorial e Medidas Repetidas

⚖️ Bloco 2 — Comparação

<p class="small">pingouin.anova() · pingouin.rm_anova() · statsmodels AnovaRM</p>

---

## 🍊 Metáfora

**Fatorial:** verifica efeito de cada fator e a *interação* (ex.: café ajuda de manhã mas não à noite).

**Medidas Repetidas:** o mesmo estudante medido em pré, durante e pós — cada pessoa é seu próprio controle.

---

## 🎯 Para que serve

**Fatorial:** avalia múltiplos fatores e interações. **MR:** compara os mesmos sujeitos em ≥ 3 momentos.

---

## 📋 Quando usar

- ✅ <strong>Fatorial:</strong> dois ou mais fatores categóricos com interesse na interação.
- ✅ <strong>MR:</strong> mesmo sujeito em ≥ 3 momentos longitudinais.
- ✅ Verificar esfericidade (Mauchly) — se violada, correção Greenhouse-Geisser.
- ❌ Dropout sistemático → prefira LMM.

---

## 🐍 Exemplo Python

```python
import pingouin as pg
import pandas as pd

df_rm = pd.DataFrame({
    'sujeito': list(range(8)) * 3,
    'momento': ['pre']*8 + ['durante']*8 + ['pos']*8,
    'escore':  [50,55,48,60,52,58,45,53,
                62,68,59,72,65,70,57,64,
                75,80,70,85,78,83,68,76]
})

rm = pg.rm_anova(data=df_rm, dv='escore', within='momento',
                 subject='sujeito', correction=True)
print(rm[['Source','F','p-unc','p-GG-corr','ng2']])

ph = pg.pairwise_tests(data=df_rm, dv='escore', within='momento',
                       subject='sujeito', padjust='bonf')
print(ph[['A','B','T','p-cor
...
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **didático:** Field, A. (2024). *Discovering Statistics*. Caps. 14–15.
- **técnico:** Greenhouse, S. W., & Geisser, S. (1959). *Psychometrika, 24*(2), 95–112.
- **python:** Vallat, R. (2018). Pingouin: statistics in Python.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../anova-fatorial.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
