<!-- .slide: class="title-slide" -->

# Enc. 6

## Teste t (independente e pareado)

⚖️ Bloco 2 — Comparação

<p class="small">pingouin.ttest() · scipy.stats.ttest_ind · ttest_rel</p>

---

## 🍊 Metáfora

Duas balanças: escores com feedback vs. sem feedback. O teste t pergunta se a diferença é grande o suficiente para não ser mero acaso. O **Cohen's d** mede o quanto as distribuições se separam. O **t pareado** mede a mudança nas *mesmas* pessoas antes e depois.

---

## 🎯 Para que serve

Compara a **média** de uma variável numérica entre **exatamente dois grupos**.

---

## 📋 Quando usar

- ✅ Variável dependente contínua e exatamente dois grupos.
- ✅ Verificar normalidade (Shapiro-Wilk) e homocedasticidade (Levene).
- ✅ Se Levene rejeitar → usar Welch (padrão no scipy).
- ❌ Se normalidade violada com n pequeno → Mann-Whitney.

---

## 🐍 Exemplo Python

```python
import pingouin as pg
from scipy.stats import shapiro, levene

feedback     = [72,85,78,90,68,82,76,88]
sem_feedback = [60,65,70,58,63,72,55,67]

_, p_n1 = shapiro(feedback);     print(f"Shapiro G1: p={p_n1:.3f}")
_, p_n2 = shapiro(sem_feedback);  print(f"Shapiro G2: p={p_n2:.3f}")
_, p_lv = levene(feedback, sem_feedback); print(f"Levene:     p={p_lv:.3f}")

res = pg.ttest(feedback, sem_feedback, paired=False, correction='auto')
print(res[['T', 'dof', 'p-val', 'cohen-d', 'power']])
```

<div class="destaque">
Código <strong>executável</strong> na página de conteúdo — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **seminal:** Student [Gosset, W. S.] (1908). The probable error of a mean. *Biometrika, 6*(1), 1–25.
- **tamanho efeito:** Cohen, J. (1988). *Statistical Power Analysis*. Cap. 2.
- **didático:** Field, A. (2024). *Discovering Statistics*. Cap. 10.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../content.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
