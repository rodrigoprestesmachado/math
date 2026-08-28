<!-- .slide: class="title-slide" -->

# Enc. 3

## Correlação de Spearman e Kendall

🔗 Bloco 1: Associação

<p class="small">scipy.stats.spearmanr · scipy.stats.kendalltau</p>

---

## 🍊 Metáfora

<p class="small">Em vez de medir a velocidade exata de cada atleta, você registra a posição deles na corrida.</p>

<p class="small">

- Spearman troca os valores originais pelos seus **postos** (rankings): 1º, 2º, 3º...
- Kendall compara **pares de atletas** e conta em quantos pares a ordem se mantém igual entre as duas corridas.

</p>

--

<div class="destaque">
Postos preservam apenas a <strong>ordem</strong> dos dados, não a distância exata entre eles. Isso é útil quando a relação entre X e Y é monotônica (sempre sobe, ou sempre desce, mas não necessariamente em linha reta) e quando a escala dos dados é ordinal, como uma escala Likert.
</div>

---

## 🎯 Para que serve

Alternativas **não paramétricas** a Pearson: não exigem normalidade nem relação linear. Medem relações **monotônicas**.

Exemplo: *a satisfação do estudante com o chatbot (escala 1 a 5) está associada à quantidade de sessões voluntárias?*

<div class="destaque">
<strong>Escala de satisfação:</strong> item único adaptado da EUCS (Doll &amp; Torkzadeh, 1988), ex.: "No geral, estou satisfeito(a) com o chatbot" (1 = discordo totalmente, 5 = concordo totalmente).<br><br>
<strong>Sessão voluntária:</strong> sessão iniciada por decisão própria do estudante, sem exigência da disciplina.<br><br>
<strong>H₀:</strong> não há relação monotônica (ρ = 0) · <strong>H₁:</strong> existe relação monotônica (ρ ≠ 0).
</div>

---

# 📐 Correlação de Spearman

## 🧮 Fórmula

<p class="small">Aplicada aos postos de X e de Y, não aos valores originais.</p>

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.3em; margin:8px auto;">
<tr>
<td rowspan="2" style="padding-right:12px; vertical-align:middle;"><em>ρ</em> = 1 −</td>
<td style="text-align:center; padding:2px 12px; border-bottom:2px solid currentColor;">6 · Σ dᵢ²</td>
</tr>
<tr>
<td style="text-align:center; padding:2px 12px;">n · (n² − 1)</td>
</tr>
</table>
</center>

<div class="destaque">
<em>dᵢ</em>: diferença entre o posto de X e o posto de Y de cada estudante · <em>n</em>: número de estudantes.<br><br>
Quanto mais parecidos os dois rankings, menores as diferenças <em>dᵢ</em>, e mais perto de 1 fica ρ.
</div>

--

## 🪜 Passo a passo do cálculo

1. Converta X e Y em postos, separadamente.
2. Para cada estudante, calcule dᵢ = posto de Xᵢ − posto de Yᵢ.
3. Eleve cada dᵢ ao quadrado e some tudo → Σ dᵢ².
4. Aplique a fórmula usando *n*, o número de estudantes.

<p class="small">Empates recebem posto médio da posição que ocupariam.</p>

--

## 🧩 Aplicação simples: ρ na mão

<p class="small">5 estudantes fictícios · X = satisfação · Y = sessões voluntárias</p>

| Est. | xᵢ | yᵢ | posto X | posto Y | dᵢ | dᵢ² |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | 2 | 3 | 2 | 2 | 0 | 0 |
| B | 4 | 8 | 4 | 4 | 0 | 0 |
| C | 1 | 1 | 1 | 1 | 0 | 0 |
| D | 5 | 12 | 5 | 5 | 0 | 0 |
| E | 3 | 5 | 3 | 3 | 0 | 0 |

<div class="destaque">
Σ dᵢ² = 0 · n = 5<br><br>
<em>ρ</em> = 1 − (6 × 0) / (5 × 24) = <strong>1,00</strong> → correlação monotônica perfeita nesses 5 estudantes.
</div>

---

## 📋 Quando usar Spearman

- ✅ Uma ou ambas variáveis são <strong>ordinais</strong> (Likert).
- ✅ Dados violam normalidade (Shapiro-Wilk: p &lt; .05).
- ✅ Há outliers que não devem ser removidos.
- ❌ Amostra pequena (n &lt; 30) ou muitos empates → considere Kendall.

---

## 🐍 Exemplo Python: Spearman

```python
import pandas as pd
import numpy as np
from scipy import stats

df = pd.DataFrame({
    'satisfacao': [2, 4, 1, 5, 3, 5, 4, 2, 3, 5],
    'sessoes':    [3, 8, 1, 12, 5, 11, 9, 2, 4, 13]
})

# Passo 1: converter em postos
df['posto_sat'] = df['satisfacao'].rank()
df['posto_ses'] = df['sessoes'].rank()

# Passo 2: calcular rho de Spearman
rho, p = stats.spearmanr(df['satisfacao'], df['sessoes'])
print(f"Spearman rho = {rho:.3f}, p = {p:.4f}")

# Intervalo de confianca de 95% via transformacao de Fisher
n = len(df)
z = np.arctanh(rho)
se = 1.0 / np.sqrt(n - 3)
ci_lo, ci_hi = np.tanh(z - 1.96*se), np.tanh(z + 1.96*se)
print(f"n = {n}, IC 95% = [{ci_lo:.2f}, {ci_hi:.2f}]")
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro, clique em <strong>▶ Executar</strong>.
</div>

---

# 📐 Correlação de Kendall

## 🎯 Conceito

<p class="small">Kendall compara pares de estudantes, não postos diretamente.</p>

- **Par concordante:** quem tem X maior também tem Y maior.
- **Par discordante:** quem tem X maior tem Y menor.

<div class="destaque">
τ (tau) é, essencialmente, a proporção de pares concordantes menos a proporção de pares discordantes.<br><br>
Prefira Kendall com amostras pequenas (n &lt; 30) ou muitos empates: sua interpretação permanece estável nesses casos.
</div>

---

## 🧮 Fórmula

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.3em; margin:8px auto;">
<tr>
<td rowspan="2" style="padding-right:12px; vertical-align:middle;"><em>τ</em> =</td>
<td style="text-align:center; padding:2px 12px; border-bottom:2px solid currentColor;">C − D</td>
</tr>
<tr>
<td style="text-align:center; padding:2px 12px;">n · (n − 1) / 2</td>
</tr>
</table>
</center>

<div class="destaque">
<em>C</em>: pares concordantes · <em>D</em>: pares discordantes · o denominador é o total de pares possíveis entre os <em>n</em> estudantes.
</div>

--

## 🪜 Passo a passo do cálculo

1. Liste todos os pares possíveis de estudantes.
2. Para cada par, compare a ordem em X e em Y: concordante ou discordante?
3. Conte C (concordantes) e D (discordantes).
4. τ = (C − D) / [n · (n − 1) / 2].

--

## 🧩 Aplicação simples: τ na mão

<p class="small">4 estudantes fictícios · X = satisfação · Y = sessões</p>

| Par | Comparação em X | Comparação em Y | Tipo |
|:-:|:-:|:-:|:-:|
| A, B | A &lt; B | A &lt; B | Concordante |
| A, C | A &gt; C | A &gt; C | Concordante |
| A, D | A &lt; D | A &lt; D | Concordante |
| B, C | B &gt; C | B &gt; C | Concordante |
| B, D | B &lt; D | B &lt; D | Concordante |
| C, D | C &lt; D | C &lt; D | Concordante |

<div class="destaque">
6 pares possíveis, todos concordantes → C = 6, D = 0<br><br>
<em>τ</em> = (6 − 0) / 6 = <strong>1,00</strong> → todo par concorda, sem exceções.
</div>

---

## 📋 Quando usar Kendall em vez de Spearman

- ✅ Amostra pequena, n &lt; 30.
- ✅ Muitos <strong>empates</strong> nos dados.
- ✅ Interpretação mais robusta a valores extremos nos postos.
- ❌ Amostra grande e sem muitos empates → Spearman costuma bastar.

---

## 🐍 Exemplo Python: Kendall

```python
import pandas as pd
from scipy import stats

df = pd.DataFrame({
    'satisfacao': [2, 4, 1, 5, 3, 5, 4, 2, 3, 5],
    'sessoes':    [3, 8, 1, 12, 5, 11, 9, 2, 4, 13]
})

# Kendall tau: proporcao de pares concordantes menos discordantes
tau, p = stats.kendalltau(df['satisfacao'], df['sessoes'])
print(f"Kendall tau = {tau:.3f}, p = {p:.4f}")

n = len(df)
pares = n * (n - 1) // 2
print(f"n = {n} estudantes, {pares} pares possiveis")
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro, clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências · Biblioteca Digital IFRS

<p class="small">Disponíveis para consulta/e-book em <a href="https://ifrs.pergamum.com.br" target="_blank">ifrs.pergamum.com.br</a></p>

- Siegel, S. & Castellan Jr., N. J. (2006). *Estatística não-paramétrica para ciências do comportamento* (2ª ed.). Porto Alegre: Artmed/Penso. [e-book] — capítulos sobre postos, Spearman e Kendall.
- Dancey, C. P. & Reidy, J. (2019). *Estatística sem matemática para psicologia* (7ª ed.). Porto Alegre: Penso.
- Costa, G. G. de O. (2012). *Curso de Estatística inferencial e probabilidades: teoria e prática*. Rio de Janeiro: Atlas. [e-book]

--

## 🌐 Referências · Recursos na Web

- Estatística Fácil. [O que é: Teste de Correlação de Spearman](https://estatisticafacil.org/glossario/o-que-e-teste-de-correlacao-de-spearman/).
- Psicometria Online. [Correlação tau de Kendall: o que é e como interpretar?](https://www.blog.psicometriaonline.com.br/o-que-e-correlacao-tau-de-kendall).
- SciELO. [Análise de correlação em estudos clínicos e experimentais](https://www.scielo.br/j/jvb/a/YwjG3GsXpBFrZLQhFQG45Rb/?format=html&lang=pt).

<div class="destaque">
Busque outros títulos por "estatística não paramétrica", "correlação" ou "análise de dados categóricos" no catálogo do IFRS.
</div>

---

## 🔗 Materiais

[Conteúdo completo + código executável](../spearman.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
