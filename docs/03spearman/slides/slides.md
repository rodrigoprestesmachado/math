<!-- .slide: class="title-slide" -->

# Enc. 3

## Correlação de Spearman e Kendall

🔗 Bloco 1 — Associação

<p class="small">scipy.stats.spearmanr · scipy.stats.kendalltau · pingouin.corr()</p>

---

## 🍊 Metáfora

Em vez de medir a velocidade exata de cada atleta, você registra a **posição deles na corrida**: 1º, 2º, 3º… Spearman e Kendall trocam os valores originais pelos seus *postos* (rankings). **Kendall** é mais conservador: conta quantos pares estão na ordem certa versus errada — útil quando há muitos empates.

---

## 🎯 Para que serve

Alternativas **não-paramétricas** a Pearson. Medem relações *monotônicas*. Ideais para dados ordinais como escalas Likert.

Exemplo: *a satisfação do estudante com o chatbot (escala 1–5) está associada à quantidade de sessões voluntárias?*

---

## 📋 Quando usar

- ✅ Uma ou ambas as variáveis são <strong>ordinais</strong> (Likert).
- ✅ Os dados violam normalidade (Shapiro-Wilk: p &lt; .05).
- ✅ Há outliers que não devem ser removidos.
- ✅ Use <strong>Kendall</strong> com n &lt; 30 ou muitos empates.

---

## 🐍 Exemplo Python

```python
import pandas as pd
from scipy import stats
import pingouin as pg

df = pd.DataFrame({
    'satisfacao': [2,4,1,5,3,5,4,2,3,5],
    'sessoes':    [3,8,1,12,5,11,9,2,4,13]
})

rho, p_s = stats.spearmanr(df['satisfacao'], df['sessoes'])
print(f"Spearman ρ = {rho:.3f}, p = {p_s:.4f}")

tau, p_k = stats.kendalltau(df['satisfacao'], df['sessoes'])
print(f"Kendall  τ = {tau:.3f}, p = {p_k:.4f}")

res = pg.corr(df['satisfacao'], df['sessoes'], method='spearman')
print(res[['n', 'r', 'CI95%', 'p-val', 'power']])
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **seminal:** Spearman, C. (1904). The proof and measurement of association between two things. *American Journal of Psychology, 15*(1), 72–101.
- **didático:** Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6ª ed.). SAGE. Cap. 8.
- **python:** Vallat, R. (2018). Pingouin: statistics in Python. *Journal of Open Source Software, 3*(31), 1026.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../spearman.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
