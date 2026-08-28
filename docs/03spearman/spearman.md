---
layout: default
title: Correlação de Spearman e Kendall
nav_order: 3
parent: Associação
has_children: false
---

# Enc. 3: Correlação de Spearman e Kendall

`scipy.stats.spearmanr · scipy.stats.kendalltau`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/03spearman/slides/index.html#/" title="Correlação de Spearman e Kendall" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Em vez de medir a velocidade exata de cada atleta, você registra a **posição deles na corrida**: 1º, 2º, 3º e assim por diante. Spearman troca os valores originais pelos seus *postos* (rankings) e depois aplica, sobre esses postos, uma ideia parecida com a de Pearson. Kendall segue outro caminho: em vez de postos, compara **pares de atletas** e conta em quantos pares a ordem se mantém igual entre as duas corridas.

{: .highlight }
> **Por que usar postos em vez dos valores originais?** Postos preservam apenas a **ordem** dos dados, não a distância exata entre eles. Isso é útil quando a relação entre X e Y é *monotônica* (sempre sobe, ou sempre desce, mas não necessariamente em linha reta) e quando a escala dos dados é ordinal, como uma escala Likert, em que não faz sentido tratar a distância entre "concordo" e "concordo totalmente" como idêntica à distância entre "discordo" e "neutro".

---

## 🎯 Para que serve

Spearman e Kendall são alternativas **não paramétricas** a Pearson: não exigem que os dados sigam distribuição normal e não assumem que a relação entre as variáveis seja uma linha reta. Ambas medem relações **monotônicas**: o padrão em que, à medida que X aumenta, Y tende a aumentar (ou tende a diminuir) de forma consistente, mesmo que não seja numa proporção constante.

Exemplo em learning analytics: *a satisfação do estudante com o chatbot (escala Likert de 1 a 5) está associada à quantidade de sessões voluntárias realizadas?*

{: .highlight }
> **Qual escala de satisfação usar?** Em vez de perguntar "você está satisfeito?" de forma genérica, é melhor aplicar um item validado. Um exemplo simples e amplamente usado é adaptar um item da escala **End-User Computing Satisfaction** (EUCS, Doll & Torkzadeh, 1988): *"No geral, estou satisfeito(a) com o chatbot"*, com resposta em escala Likert de 1 (discordo totalmente) a 5 (concordo totalmente). Como é um único item ordinal, e não um escore composto de vários itens, ele permanece ordinal, e por isso Spearman (não Pearson) é a escolha adequada aqui.

{: .highlight }
> **O que é uma sessão voluntária?** É uma sessão de uso do chatbot iniciada por decisão própria do estudante, sem que a disciplina exija aquele número mínimo de interações. Ela mede engajamento espontâneo: quanto mais satisfeito o estudante estiver com a ferramenta, maior a tendência de procurá-la por conta própria, fora de qualquer tarefa obrigatória.

Em termos de hipótese, para Spearman:

| | |
|:--|:--|
| **H₀** | Não há relação monotônica entre as variáveis (ρ = 0 na população). |
| **H₁** | Existe relação monotônica (ρ ≠ 0). |

{: .highlight }
> **Correlação não implica causalidade.** Assim como em Pearson, um ρ ou τ significativo mostra associação, não prova que uma variável causa a outra. Um estudante mais satisfeito pode participar de mais sessões, ou um estudante que já participa de mais sessões pode acabar mais satisfeito por dominar melhor a ferramenta.

---

# 📐 Correlação de Spearman

## 🧮 Fórmula

O ρ (rho) de Spearman é calculado da mesma forma que o *r* de Pearson, mas aplicado aos **postos** (rankings) de X e de Y, em vez dos valores originais. Quando não há empates entre os valores, existe um atalho que simplifica bastante a conta:

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

{: .highlight }
> **Lendo a fórmula:** primeiro converta os valores de X e de Y em postos (1º, 2º, 3º...); *dᵢ* é a diferença entre o posto de X e o posto de Y para cada estudante; Σ dᵢ² soma o quadrado dessas diferenças para todos os estudantes; *n* é o número de estudantes. Quanto mais parecidos forem os dois rankings, menores as diferenças *dᵢ*, e mais perto de 1 fica ρ.

**Como ρ é calculado, passo a passo:**

1. Converta os valores de X em postos, e os valores de Y em postos, separadamente.
2. Para cada estudante, calcule a diferença entre os dois postos: dᵢ = posto de Xᵢ − posto de Yᵢ.
3. Eleve cada diferença ao quadrado e some todos os resultados → Σ dᵢ².
4. Aplique a fórmula acima usando *n*, o número de estudantes.

{: .highlight }
> **E quando há empates?** Se dois ou mais estudantes têm o mesmo valor numa variável, cada um recebe o **posto médio** da posição que ocupariam. Por exemplo, se dois estudantes empatam em 2º e 3º lugar, ambos recebem posto 2,5. Com muitos empates, a fórmula simplificada acima perde precisão, e a implementação do `scipy` já usa por padrão o cálculo completo (equivalente ao *r* de Pearson sobre os postos), o que a torna confiável mesmo nesses casos.

**Aplicação simples: aplicando os passos a 5 estudantes**

Usando os mesmos 5 estudantes fictícios do exemplo Python mais abaixo, com a **satisfação** com o chatbot (escala 1 a 5) em X e o número de **sessões voluntárias** em Y:

| Estudante | xᵢ (satisfação) | yᵢ (sessões) | posto Xᵢ | posto Yᵢ | dᵢ | dᵢ² |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | 2 | 3 | 2 | 2 | 0 | 0 |
| B | 4 | 8 | 4 | 4 | 0 | 0 |
| C | 1 | 1 | 1 | 1 | 0 | 0 |
| D | 5 | 12 | 5 | 5 | 0 | 0 |
| E | 3 | 5 | 3 | 3 | 0 | 0 |
| **Soma** | | | | | | **0** |

1. **Postos** (passo 1): como não há empates entre os 5 estudantes, cada valor recebe um posto único de 1 a 5.
2. **Diferenças** (passo 2): dᵢ = posto Xᵢ − posto Yᵢ = 0 para todos, porque a ordem de satisfação é idêntica à ordem de sessões nesse grupo reduzido.
3. **Soma dos quadrados** (passo 3): Σ dᵢ² = 0.
4. **Resultado** (passo 4): ρ = 1 − (6 × 0) / (5 × 24) = 1 − 0 = **1,00**.

{: .highlight }
> **Interpretação:** ρ = 1,00 é uma correlação monotônica **perfeita**: nesses 5 estudantes fictícios, quem tem posto mais alto em satisfação tem exatamente o mesmo posto em número de sessões. No exemplo Python mais abaixo, `scipy.stats.spearmanr` faz esse mesmo cálculo, mas para os 10 estudantes do conjunto de dados completo, onde o resultado não é mais perfeito.

---

## 🔢 O que significa ρ (rho)?

| Valor de ρ | Direção | Interpretação intuitiva |
|:-------------|:--------|:------------------------|
| **+1** | positiva | Quanto maior o posto em X, maior o posto em Y, sempre. |
| **0** | nenhuma | Os postos de X e de Y variam de forma independente. |
| **−1** | negativa | Quanto maior o posto em X, menor o posto em Y, sempre. |
| **entre 0 e ±1** | parcial | Há tendência monotônica, mas com exceções na ordem. |

{: .highlight }
> **Convenção de Cohen (1988) para o tamanho do efeito**, também usada para ρ: \|ρ\| < 0,10 negligível · 0,10 a 0,29 pequeno · 0,30 a 0,49 médio · ≥ 0,50 grande.

---

## 📋 Quando usar Spearman

**Use Spearman quando:**

- ✅ Uma ou ambas as variáveis são **ordinais**, como uma escala Likert (1 a 5).
- ✅ As variáveis são contínuas, mas os dados violam normalidade (teste de Shapiro-Wilk: p < .05). Veja a seção sobre [Shapiro-Wilk em Pearson](../02pearson/pearson.html) para entender esse teste em detalhe.
- ✅ Há **outliers** que não devem ser removidos, pois trabalhar com postos reduz bastante a influência de valores extremos.
- ✅ A relação esperada é monotônica, mas não necessariamente em linha reta.

**Exemplos em logs educacionais (learning analytics):**

- *Satisfação com o chatbot (Likert 1 a 5) × número de sessões voluntárias:* variável ordinal, não faz sentido tratar a distância entre os pontos da escala como igual.
- *Ranking de engajamento na turma × nota final:* estudantes mais bem posicionados no ranking de participação tendem a tirar notas mais altas?
- *Tempo de sessão com distribuição fortemente assimétrica (cauda longa) × desempenho:* normalidade comprometida, Spearman é mais robusto nesse cenário.

**Evite Spearman quando:**

- ❌ Ambas as variáveis são contínuas, aproximadamente normais e a relação é claramente linear: nesse caso, Pearson aproveita melhor a informação disponível.
- ❌ Você precisa distinguir uma relação linear de uma relação curvilínea: Spearman só detecta monotonicidade, não diferencia os dois formatos.
- ❌ A amostra é muito pequena (n < 30) ou há muitos empates: considere usar Kendall, explicado na seção seguinte.

---

## 🔍 Perguntas de pesquisa em Informática na Educação

Em pesquisas de Informática na Educação que analisam **conversas de estudantes com chatbots**, Spearman (e Kendall) servem para responder perguntas em que ao menos uma das variáveis é **ordinal**, ou em que a relação esperada é **monotônica**, mas não necessariamente linear:

- A **satisfação do estudante com o chatbot** (Likert 1 a 5) está associada ao **número de sessões voluntárias** realizadas?
- O **grau de complexidade linguística** das perguntas do estudante (escala ordinal: baixa/média/alta) está associado ao **ranking de desempenho** na turma?
- A **posição no ranking de engajamento** (por número de interações) está associada à **posição no ranking de notas**?
- O **grau de autonomia da pergunta** (escala ordinal: pede a resposta pronta → pede uma dica → tenta resolver e só confirma) está associado ao **tempo total de uso do chatbot**, que costuma ter distribuição assimétrica?
- A **percepção de utilidade do chatbot** (Likert 1 a 5) está associada ao **número de mensagens enviadas por sessão**?

{: .highlight }
> **Por que não usar Pearson nessas perguntas?** Escalas Likert isoladas são ordinais, não intervalares, e variáveis como tempo de uso costumam ter distribuição assimétrica (cauda longa), violando a normalidade exigida por [Pearson](../02pearson/pearson.html). Spearman aproveita apenas a ordem dos valores, o que se ajusta melhor a esses casos; prefira Kendall quando a amostra for pequena (n < 30) ou houver muitos empates.

---

## 🪜 Passo a passo na prática

1. **Visualize:** plote X × Y (ou os postos de X × Y). A nuvem sobe, desce ou é um emaranhado sem padrão?
2. **Verifique pressupostos:** as variáveis são ordinais, ou violam normalidade, ou têm outliers relevantes?
3. **Calcule:** `stats.spearmanr(x, y)` ou `df.corr(method='spearman')`.
4. **Interprete:** leia ρ (direção e força) e *p* (evidência contra H₀).
5. **Reporte:** informe ρ, *p*, *n* e, se possível, o gráfico dos postos no artigo ou relatório.

---

## 📖 Como ler o resultado

Suponha que o código abaixo retorne `rho = 0.85, p = 0.002` com *n* = 10 estudantes:

- **ρ = 0,85** → relação monotônica **forte e positiva**: estudantes mais satisfeitos tendem a participar de mais sessões voluntárias.
- **p < .05** → rejeitamos H₀: a associação observada é improvável se não houvesse relação monotônica na população.
- **Cohen** → \|0,85\| ≥ 0,50 → tamanho de efeito **grande** (com *n* pequeno, essa estimativa ainda é instável).

---

## 🐍 Exemplo Python: Spearman

**Contexto:** verificar se a satisfação do estudante com o chatbot (Likert 1 a 5) se associa ao número de sessões voluntárias.

O código converte os valores em postos, plota o gráfico de postos e calcula ρ com o intervalo de confiança de 95%.

<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZAppbXBvcnQgbnVtcHkgYXMgbnAKZnJvbSBzY2lweSBpbXBvcnQgc3RhdHMKaW1wb3J0IG1hdHBsb3RsaWIucHlwbG90IGFzIHBsdAoKZGYgPSBwZC5EYXRhRnJhbWUoewogICAgJ3NhdGlzZmFjYW8nOiBbMiwgNCwgMSwgNSwgMywgNSwgNCwgMiwgMywgNV0sCiAgICAnc2Vzc29lcyc6ICAgIFszLCA4LCAxLCAxMiwgNSwgMTEsIDksIDIsIDQsIDEzXQp9KQoKIyBQYXNzbyAxOiBjb252ZXJ0ZXIgZW0gcG9zdG9zIGUgdmlzdWFsaXphcgpkZlsncG9zdG9fc2F0J10gPSBkZlsnc2F0aXNmYWNhbyddLnJhbmsoKQpkZlsncG9zdG9fc2VzJ10gPSBkZlsnc2Vzc29lcyddLnJhbmsoKQpkZi5wbG90LnNjYXR0ZXIoeD0ncG9zdG9fc2F0JywgeT0ncG9zdG9fc2VzJywgY29sb3I9JyNjNzkyZWEnLAogICAgICAgICAgICAgICAgdGl0bGU9J1Bvc3Rvczogc2F0aXNmYWNhbyB4IHNlc3NvZXMnKQpwbHQueGxhYmVsKCdQb3N0byBkYSBzYXRpc2ZhY2FvJykKcGx0LnlsYWJlbCgnUG9zdG8gZGFzIHNlc3NvZXMnKQpwbHQuc2hvdygpCgojIFBhc3NvIDI6IGNhbGN1bGFyIHJobyBkZSBTcGVhcm1hbgpyaG8sIHAgPSBzdGF0cy5zcGVhcm1hbnIoZGZbJ3NhdGlzZmFjYW8nXSwgZGZbJ3Nlc3NvZXMnXSkKcHJpbnQoZiJTcGVhcm1hbiByaG8gPSB7cmhvOi4zZn0sIHAgPSB7cDouNGZ9IikKCiMgSW50ZXJ2YWxvIGRlIGNvbmZpYW5jYSBkZSA5NSUgcGFyYSByaG8gdmlhIHRyYW5zZm9ybWFjYW8gZGUgRmlzaGVyCm4gPSBsZW4oZGYpCnogPSBucC5hcmN0YW5oKHJobykKc2UgPSAxLjAgLyBucC5zcXJ0KG4gLSAzKQpjaV9sbywgY2lfaGkgPSBucC50YW5oKHogLSAxLjk2KnNlKSwgbnAudGFuaCh6ICsgMS45NipzZSkKcHJpbnQoZiJuID0ge259LCBJQyA5NSUgPSBbe2NpX2xvOi4yZn0sIHtjaV9oaTouMmZ9XSIpCg==" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false"></textarea>
  <pre class="code-output"></pre>
</div>

---

# 📐 Correlação de Kendall

## 🎯 Conceito

Kendall mede associação de outra forma: em vez de comparar postos diretamente, ela olha para **pares de estudantes** e verifica se a ordem se mantém igual nas duas variáveis. Dados dois estudantes quaisquer, o par é:

- **Concordante:** se o estudante com valor maior de X também tem valor maior de Y (os dois "sobem juntos").
- **Discordante:** se o estudante com valor maior de X tem valor menor de Y (um sobe, o outro desce).

O τ (tau) de Kendall é, essencialmente, a proporção de pares concordantes menos a proporção de pares discordantes.

{: .highlight }
> **Quando preferir Kendall a Spearman?** Kendall costuma ser recomendada com amostras pequenas (n < 30) ou quando há muitos empates nos dados, situações em que sua interpretação como "diferença entre pares concordantes e discordantes" permanece estável e fácil de justificar. Seus valores tendem a ser menores, em módulo, do que os de Spearman para o mesmo conjunto de dados, mas isso é esperado: as duas medidas usam escalas diferentes, não significa que a associação seja mais fraca.

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

{: .highlight }
> **Lendo a fórmula:** *C* é o número de pares concordantes; *D* é o número de pares discordantes; o denominador, n · (n − 1) / 2, é o número **total** de pares possíveis entre os *n* estudantes. Se todos os pares forem concordantes, τ = 1; se todos forem discordantes, τ = −1.

**Como τ é calculado, passo a passo:**

1. Liste todos os pares possíveis de estudantes (sem repetir e sem comparar um estudante com ele mesmo).
2. Para cada par, compare a ordem em X e a ordem em Y: o par é concordante ou discordante?
3. Conte quantos pares são concordantes (C) e quantos são discordantes (D).
4. Aplique a fórmula acima usando o total de pares possíveis, n · (n − 1) / 2.

**Aplicação simples: aplicando os passos a 4 estudantes**

Usando 4 estudantes fictícios, com **satisfação** (X) e **sessões** (Y):

| Estudante | xᵢ (satisfação) | yᵢ (sessões) |
|:-:|:-:|:-:|
| A | 2 | 3 |
| B | 4 | 8 |
| C | 1 | 1 |
| D | 5 | 12 |

Com 4 estudantes há 4 · 3 / 2 = **6 pares possíveis**:

| Par | Comparação em X | Comparação em Y | Tipo |
|:-:|:-:|:-:|:-:|
| A, B | A < B | A < B | Concordante |
| A, C | A > C | A > C | Concordante |
| A, D | A < D | A < D | Concordante |
| B, C | B > C | B > C | Concordante |
| B, D | B < D | B < D | Concordante |
| C, D | C < D | C < D | Concordante |

1. **Contagem** (passos 1–3): todos os 6 pares são concordantes → C = 6, D = 0.
2. **Resultado** (passo 4): τ = (6 − 0) / 6 = **1,00**.

{: .highlight }
> **Interpretação:** τ = 1,00 indica que, para **todo par** desses 4 estudantes, quem tem maior satisfação também tem mais sessões, sem exceções. No exemplo Python mais abaixo, `scipy.stats.kendalltau` faz essa mesma conta de forma automática, para os 10 estudantes do conjunto de dados completo, onde nem todos os pares concordam perfeitamente.

---

## 🔢 O que significa τ (tau)?

| Valor de τ | Direção | Interpretação intuitiva |
|:-------------|:--------|:------------------------|
| **+1** | positiva | Todos os pares são concordantes: a ordem em X sempre acompanha a ordem em Y. |
| **0** | nenhuma | Metade dos pares é concordante, metade é discordante: nenhuma tendência clara. |
| **−1** | negativa | Todos os pares são discordantes: a ordem em X sempre se inverte em relação a Y. |

---

## 📋 Quando usar Kendall em vez de Spearman

- ✅ A amostra é pequena, com n < 30 estudantes.
- ✅ Há muitos **empates** nos dados, o que torna a interpretação de τ mais direta que a de ρ nesses casos.
- ✅ Você quer uma interpretação mais robusta a valores extremos nos postos, já que τ depende apenas da direção de cada par, não da magnitude das diferenças.
- ❌ Se a amostra é grande e sem muitos empates, Spearman costuma ser suficiente e é mais usada na literatura, o que facilita a comparação com outros estudos.

---

## 🐍 Exemplo Python: Kendall

**Contexto:** o mesmo conjunto de dados de satisfação e sessões, agora usando `kendalltau`, útil para comparar com o resultado de Spearman obtido acima.

<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZApmcm9tIHNjaXB5IGltcG9ydCBzdGF0cwoKZGYgPSBwZC5EYXRhRnJhbWUoewogICAgJ3NhdGlzZmFjYW8nOiBbMiwgNCwgMSwgNSwgMywgNSwgNCwgMiwgMywgNV0sCiAgICAnc2Vzc29lcyc6ICAgIFszLCA4LCAxLCAxMiwgNSwgMTEsIDksIDIsIDQsIDEzXQp9KQoKIyBLZW5kYWxsIHRhdTogcHJvcG9yY2FvIGRlIHBhcmVzIGNvbmNvcmRhbnRlcyBtZW5vcyBkaXNjb3JkYW50ZXMKdGF1LCBwID0gc3RhdHMua2VuZGFsbHRhdShkZlsnc2F0aXNmYWNhbyddLCBkZlsnc2Vzc29lcyddKQpwcmludChmIktlbmRhbGwgdGF1ID0ge3RhdTouM2Z9LCBwID0ge3A6LjRmfSIpCgpuID0gbGVuKGRmKQpwYXJlcyA9IG4gKiAobiAtIDEpIC8vIDIKcHJpbnQoZiJuID0ge259IGVzdHVkYW50ZXMsIHtwYXJlc30gcGFyZXMgcG9zc2l2ZWlzIikK" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false"></textarea>
  <pre class="code-output"></pre>
</div>

---

## 📚 Referências · Biblioteca Digital IFRS

Disponíveis para consulta/e-book em [ifrs.pergamum.com.br](https://ifrs.pergamum.com.br).

| | |
|:--|:--|
| **e-book** | Siegel, S., & Castellan Jr., N. J. (2006). *Estatística não-paramétrica para ciências do comportamento* (2ª ed.). Porto Alegre: Artmed/Penso. Capítulos sobre postos, Spearman e Kendall. |
| **acervo** | Dancey, C. P., & Reidy, J. (2019). *Estatística sem matemática para psicologia* (7ª ed.). Porto Alegre: Penso. |
| **e-book** | Costa, G. G. de O. (2012). *Curso de Estatística inferencial e probabilidades: teoria e prática*. Rio de Janeiro: Atlas. |

## 🌐 Referências · Recursos na Web

| | |
|:--|:--|
| **web (PT)** | Estatística Fácil. [O que é: Teste de Correlação de Spearman](https://estatisticafacil.org/glossario/o-que-e-teste-de-correlacao-de-spearman/). Definição, fórmula e cálculo passo a passo. |
| **web (PT)** | Psicometria Online. [Correlação tau de Kendall: o que é e como interpretar?](https://www.blog.psicometriaonline.com.br/o-que-e-correlacao-tau-de-kendall). Diferenças entre Kendall e Spearman, tamanho de efeito. |
| **web (PT)** | SciELO. [Análise de correlação em estudos clínicos e experimentais](https://www.scielo.br/j/jvb/a/YwjG3GsXpBFrZLQhFQG45Rb/?format=html&lang=pt). Comparação prática entre Spearman e Kendall Tau-b. |
| **web (PT)** | [Matos, *Estatística + R*: Correlação entre variáveis](https://ana-mat-br.github.io/correla%C3%A7%C3%A3o-entre-vari%C3%A1veis.html). Spearman e Kendall com exemplos em R. |
| **escala de satisfação** | Doll, W. J., & Torkzadeh, G. (1988). The measurement of end-user computing satisfaction. *MIS Quarterly, 12*(2), 259 a 274. Base do item usado na metáfora de satisfação com o chatbot. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
