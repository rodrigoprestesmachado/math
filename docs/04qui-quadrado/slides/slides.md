<!-- .slide: class="title-slide" -->

# Enc. 4

## Qui-quadrado e V de Cramér

🔗 Bloco 1: Associação

<p class="small">scipy.stats.chi2_contingency · cálculo manual de V</p>

---

## 🍊 Metáfora

<p class="small">Um restaurante serve três pratos (factual, conceitual, procedimental) para três tipos de clientes (passivo, ativo, intensivo).</p>

<p class="small">

- Se o tipo de cliente não influenciasse o prato escolhido, esperaríamos a mesma proporção de pratos em cada grupo.
- O qui-quadrado (χ²) compara essa distribuição **esperada** (sem relação) com o que foi **observado** de fato.
- Quanto maior a diferença, maior o χ², e mais evidência de associação.

</p>

--

<div class="destaque">
O χ² cresce junto com o tamanho da amostra: com muitas observações, até uma associação fraca pode gerar um χ² grande e um <em>p</em> pequeno. Por isso χ² responde <strong>existe associação?</strong> (significância), e o <strong>V de Cramér</strong> responde <strong>quão forte é?</strong> (tamanho do efeito).
</div>

---

## 🎯 Para que serve

Testa se duas variáveis **categóricas nominais** são **independentes**, organizadas numa **tabela de contingência**: linhas e colunas são categorias, cada célula conta quantos estudantes caem naquela combinação.

Exemplo: *o tipo de pergunta ao chatbot varia conforme o perfil de uso do estudante?*

<div class="destaque">
<strong>H₀:</strong> as duas variáveis são independentes (não há associação na população).<br>
<strong>H₁:</strong> as duas variáveis são associadas.
</div>

---

# 📐 Qui-quadrado (χ²)

## 🧮 Fórmula

<p class="small">Soma, célula a célula, o quanto o observado se afasta do esperado sob independência.</p>

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.3em; margin:8px auto;">
<tr>
<td rowspan="2" style="padding-right:12px; vertical-align:middle;"><em>χ²</em> =</td>
<td style="text-align:center; padding:2px 12px; border-bottom:2px solid currentColor;">Σ (Oᵢ − Eᵢ)²</td>
</tr>
<tr>
<td style="text-align:center; padding:2px 12px;">Eᵢ</td>
</tr>
</table>
</center>

<div class="destaque">
<em>Oᵢ</em>: frequência observada em cada célula · <em>Eᵢ</em>: frequência esperada sob independência, calculada por (total da linha × total da coluna) / n.
</div>

--

## 🪜 Passo a passo do cálculo

1. Monte a tabela de contingência com as frequências **observadas**.
2. Calcule os totais de linha, de coluna, e o total geral (n).
3. Para cada célula: E = (total da linha × total da coluna) / n.
4. Para cada célula: (O − E)² / E.
5. Some tudo → **χ²**.

--

## 🧩 Aplicação simples: χ² na mão

<p class="small">40 estudantes fictícios · nível (iniciante/avançado) × tipo de pergunta (factual/conceitual)</p>

| | Factual (O) | Conceitual (O) | Total |
|:--|:-:|:-:|:-:|
| **Iniciante** | 15 | 5 | 20 |
| **Avançado** | 5 | 15 | 20 |
| **Total** | 20 | 20 | **n = 40** |

<div class="destaque">
Todas as células esperam E = (20 × 20) / 40 = 10.<br><br>
(O − E)²/E = 2,5 em cada célula → <em>χ²</em> = 2,5 × 4 = <strong>10,00</strong> (gl = 1) → suficiente para rejeitar H₀.
</div>

---

# 📐 V de Cramér

## 🧮 Fórmula

<p class="small">χ² sozinho não diz o quão forte é a associação; V reescala pelo tamanho da amostra.</p>

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.3em; margin:8px auto;">
<tr>
<td style="padding-right:12px; vertical-align:middle;"><em>V</em> = √</td>
<td style="text-align:center; padding:2px 12px; border-bottom:2px solid currentColor;">χ²</td>
</tr>
<tr>
<td></td>
<td style="text-align:center; padding:2px 12px;">n · k</td>
</tr>
</table>
</center>

<div class="destaque">
<em>k</em> = menor entre (linhas − 1) e (colunas − 1). Aplicando ao exemplo acima: k = 1 → <em>V</em> = √(10 / 40) = <strong>0,50</strong> → associação grande.
</div>

---

## 🔢 O que significa V?

| Valor de V | Força |
|:-----------|:------|
| **≈ 0,10** | pequena |
| **≈ 0,30** | média |
| **≈ 0,50** | grande |

<div class="destaque">
<strong>Convenção de Cohen (1988).</strong> Sozinho, <em>p</em> &lt; .05 indica que a associação existe; V mostra se ela é relevante na prática.
</div>

---

## 📋 Quando usar

- ✅ Ambas as variáveis são <strong>categóricas nominais</strong>.
- ✅ Observações **independentes**: cada estudante conta uma única vez.
- ✅ Frequência esperada ≥ 5 em pelo menos 80% das células.
- ❌ Não use com variáveis ordinais; Spearman é mais adequado.
- ❌ Nunca interprete apenas o p-valor: sempre reporte V de Cramér.

--

## 📋 Exemplos em learning analytics

- Tipo de pergunta × perfil de uso do chatbot.
- Turno de uso × modalidade da disciplina.
- Categoria de erro mais comum × turma.
- Uso de um recurso opcional (sim/não) × aprovação (sim/não).

---

## 📐 Teste exato de Fisher

<p class="small">Alternativa ao χ² quando as frequências esperadas são baixas, comum em tabelas 2×2 pequenas.</p>

<div class="destaque">
<strong>H₀:</strong> as duas variáveis são independentes.<br>
<strong>H₁:</strong> as duas variáveis são associadas.
</div>

- **Frequência esperada ≥ 5 em ≥ 80% das células** → o χ² é uma boa aproximação.
- **Alguma célula com frequência esperada &lt; 5**, sobretudo em 2×2 → prefira `stats.fisher_exact`.

<p class="small">Fisher é exato em qualquer tamanho de amostra, mas fica caro em tabelas grandes; por isso é reservado para os casos em que o χ² não é confiável.</p>

---

## 🪜 Passo a passo na prática

1. **Visualize:** monte a tabela de contingência.
2. **Verifique pressupostos:** independência das observações e frequência esperada suficiente (ou use Fisher).
3. **Calcule:** `chi2_contingency(tabela)` para χ² e *p*, depois V a partir do χ².
4. **Interprete:** leia *p* (significância) e V (força), nunca apenas um dos dois.
5. **Reporte:** χ², gl, *p*, *n*, V e a tabela de contingência.

---

## 📖 Como ler o resultado

<p class="small">Suponha χ² = 18.203, gl = 4, p = 0.0011, V = 0.301, com n = 138 estudantes:</p>

- **χ² = 18,203, p = 0,0011** → rejeitamos H₀: é pouco provável essa tabela sob independência.
- **V = 0,301** → efeito <strong>médio a grande</strong>: a associação existe e tem magnitude relevante.
- O tipo de pergunta varia de forma perceptível conforme o perfil de uso.

<div class="destaque">
<strong>Associação ≠ causalidade.</strong> Um perfil de uso intensivo pode levar a perguntas mais elaboradas, ou o contrário: estudantes que já perguntam melhor podem se engajar mais.
</div>

---

## 🐍 Exemplo Python: Qui-quadrado e V de Cramér

```python
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Passo 1: montar a tabela de contingencia
tabela = pd.DataFrame(
    [[30,15,10],[20,25,18],[10,20,35]],
    index   = ['factual','conceitual','procedimental'],
    columns = ['passivo','ativo','intensivo']
)
print(tabela, "\n")

# Passo 2: calcular qui-quadrado, p-valor, graus de liberdade e esperadas
chi2, p, gl, esperadas = chi2_contingency(tabela)
print(f"χ² = {chi2:.3f}  gl = {gl}  p = {p:.4f}")

# Passo 3: calcular V de Cramer a partir do mesmo qui-quadrado
n = tabela.values.sum()
k = min(tabela.shape) - 1
V = np.sqrt(chi2 / (n * k))
efeito = 'pequeno' if V < .3 else 'médio' if V < .5 else 'grande'
print(f"V de Cramér = {V:.3f}  → efeito {efeito}")
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro, clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências

- **seminal:** Cramér, H. (1946). *Mathematical Methods of Statistics*. Princeton University Press.
- **didático:** Agresti, A. (2013). *Categorical Data Analysis* (3ª ed.). Wiley.
- **didático:** Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6ª ed.). SAGE. Cap. 19.
- **tamanho efeito:** Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Cap. 7.
- **teste exato:** Fisher, R. A. (1922). On the interpretation of χ² from contingency tables. *Journal of the Royal Statistical Society, 85*(1), 87 a 94.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../qui-quadrado.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
