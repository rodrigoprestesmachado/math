<!-- .slide: class="title-slide" -->

# Enc. 7

## Mann-Whitney e Wilcoxon

⚖️ Bloco 2 — Comparação

<p class="small">scipy.stats.mannwhitneyu · wilcoxon · pingouin.mwu()</p>

---

## 🍊 Metáfora

Em vez de comparar médias, junta todos numa fila ordenada e verifica se um grupo tende a ocupar posições mais altas. Não importa *quanto* mais alto — só *que é mais alto*.

---

## 🎯 Para que serve

Compara a **distribuição de postos** entre dois grupos sem assumir normalidade.

**Mann-Whitney U**: independentes. **Wilcoxon signed-rank**: pareadas.

---

## 📋 Quando usar

- ✅ Dados ordinais (Likert) ou numéricos que violam normalidade.
- ✅ Amostras pequenas (n &lt; 30).
- ✅ Outliers que não devem ser removidos.
- ❌ Não testa diferença de médias — testa diferença de distribuições.

---

## 🐍 Exemplo Python

```python
import pingouin as pg
from scipy.stats import wilcoxon

grupo_a = [3,5,4,6,7,4,5]
grupo_b = [2,3,1,4,3,2,3]

res_mw = pg.mwu(grupo_a, grupo_b, alternative='two-sided')
print("Mann-Whitney:")
print(res_mw[['U-val', 'p-val', 'RBC', 'CLES']])

pre  = [3,5,4,6,4,3]
pos  = [5,6,6,7,6,5]
stat, p_w = wilcoxon(pre, pos, alternative='two-sided')
print(f"\nWilcoxon: W = {stat:.0f}, p = {p_w:.4f}")
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **seminal:** Mann, H. B., & Whitney, D. R. (1947). *Annals of Mathematical Statistics, 18*(1), 50–60.
- **seminal:** Wilcoxon, F. (1945). *Biometrics Bulletin, 1*(6), 80–83.
- **didático:** Field, A. (2024). *Discovering Statistics*. Cap. 7.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../mann-whitney.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
