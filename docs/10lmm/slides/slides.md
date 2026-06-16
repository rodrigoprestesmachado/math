<!-- .slide: class="title-slide" -->

# Enc. 10

## Modelos Lineares Mistos (LMM)

⚖️ Bloco 2 — Comparação

<p class="small">statsmodels.formula.api.mixedlm · pingouin.mixed_anova()</p>

---

## 🍊 Metáfora

Dados aninhados (mensagens em sessões, sessões em estudantes) violam independência. LMM tem **efeitos fixos** (o efeito na população) e **efeitos aleatórios** (variabilidade de cada estudante/turma). Cada sujeito ganha seu próprio ponto de partida.

---

## 🎯 Para que serve

Modelar dados com estrutura **hierárquica**: mensagens → sessões → estudantes → turmas.

---

## 📋 Quando usar

- ✅ Observações aninhadas em grupos.
- ✅ Dados longitudinais com faltantes ou grupos desiguais.
- ✅ Quando ANOVA MR não converge.
- ❌ Comece com modelos simples (só intercepto aleatório).

---

## 🐍 Exemplo Python

```python
import statsmodels.formula.api as smf
import pandas as pd
import numpy as np

np.random.seed(42)
n_est, n_ses = 20, 5

df = pd.DataFrame({
    'estudante': np.repeat(range(n_est), n_ses),
    'sessao':    list(range(n_ses)) * n_est,
    'turnos':    np.random.poisson(6, n_est*n_ses),
    'escore':    np.random.normal(70, 10, n_est*n_ses)
})
df['escore'] += df['turnos'] * 1.5

modelo = smf.mixedlm("escore ~ turnos", data=df, groups=df["estudante"]).fit(reml=True)
print(modelo.summary())
```

<div class="destaque">
Código <strong>executável</strong> na página de conteúdo — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **referência:** Gelman, A., & Hill, J. (2007). *Data Analysis Using Regression and Multilevel Models*.
- **acessível:** Winter, B. (2019). *Statistics for Linguists*. Routledge.
- **educação:** Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical Linear Models* (2ª ed.).

---

## 🔗 Materiais

[Conteúdo completo + código executável](../content.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
