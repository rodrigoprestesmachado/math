<!-- .slide: class="title-slide" -->

# Enc. 4

## Qui-quadrado e V de Cramér

🔗 Bloco 1 — Associação

<p class="small">scipy.stats.chi2_contingency · cálculo manual de V</p>

---

## 🍊 Metáfora

Imagine um cardápio com três pratos (factual, conceitual, procedimental) e três tipos de clientes. O qui-quadrado compara o *observado* com o *esperado* se não houvesse relação. O **V de Cramér** quantifica a força dessa associação, livre do tamanho amostral.

---

## 🎯 Para que serve

Testa se duas variáveis **categóricas** são independentes. O **p-valor do χ²** indica significância; o **V de Cramér** quantifica a força.
Exemplo: *o tipo de pergunta ao chatbot varia conforme o perfil de uso do estudante?*

---

## 📋 Quando usar

- ✅ Ambas as variáveis são <strong>categóricas nominais</strong>.
- ✅ Frequência esperada ≥ 5 em pelo menos 80% das células (senão, Fisher exato).
- ❌ Não use com variáveis ordinais — Spearman é mais adequado.
- ❌ Nunca interpretar apenas o p-valor: sempre reporte V de Cramér.

---

## 🐍 Exemplo Python

```python
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

tabela = pd.DataFrame(
    [[30,15,10],[20,25,18],[10,20,35]],
    index   = ['factual','conceitual','procedimental'],
    columns = ['passivo','ativo','intensivo']
)
print(tabela, "\n")

chi2, p, gl, esperadas = chi2_contingency(tabela)
print(f"χ² = {chi2:.3f}  gl = {gl}  p = {p:.4f}")

n = tabela.values.sum()
k = min(tabela.shape) - 1
V = np.sqrt(chi2 / (n * k))
efeito = 'pequeno' if V < .3 else 'médio' if V < .5 else 'grande'
print(f"V de Cramér = {V:.3f}  → efeito {efeito}")
```

<div class="destaque">
Código <strong>executável</strong> na página de conteúdo — clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **seminal:** Cramér, H. (1946). *Mathematical Methods of Statistics*. Princeton University Press.
- **didático:** Agresti, A. (2013). *Categorical Data Analysis* (3ª ed.). Wiley.
- **tamanho efeito:** Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Cap. 7.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../content.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
