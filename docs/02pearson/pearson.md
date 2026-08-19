---
layout: default
title: Correlação de Pearson
nav_order: 2
parent: Associação
has_children: false
---

# Enc. 2: Correlação de Pearson

Relação linear entre variáveis contínuas · coeficiente *r*
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/02pearson/slides/index.html#/" title="Correlação de Pearson" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Dois atletas correm lado a lado numa pista. Quando um acelera, o outro acelera na mesma proporção; quando freia, o outro freia também. Isso é **r = +1**: movimento em perfeita sincronia, na mesma direção. Se um acelera enquanto o outro freia (na mesma medida), temos **r = −1**. Se cada um corre no seu ritmo, sem seguir o outro, **r ≈ 0**.
>
> Pearson quantifica essa sincronia, mas *só enquanto a pista for reta*.

{: .highlight }
> **E se a pista não for reta?** Imagine que os dois atletas correm num trecho plano, lado a lado, em perfeita sincronia — de repente, a pista encontra uma colina. Na subida, um deles tem mais força e mantém o ritmo; o outro cansa e desacelera, e a sincronia que existia no plano se desfaz. O padrão muda de comportamento ao longo do percurso (uma reta, depois uma subida): não existe uma única reta que descreva bem todo o trajeto. Dependendo do tamanho da subida em relação ao trecho plano, *r* pode cair bastante, chegando perto de 0 mesmo havendo um padrão bem claro no gráfico.

---

## 🎯 Para que serve

Mede a **força** e a **direção** de uma relação *linear* entre duas variáveis numéricas contínuas. O coeficiente *r* vai de −1 a +1.

{: .highlight }
> **O que é relação linear?** Ao plotar X × Y, os pontos tendem a se alinhar numa linha reta: cada aumento de X produz, em média, um acréscimo (ou decréscimo) **constante** em Y, como em Y = a + bX.
>
> **Por quê Pearson exige isso?** O *r* mede o quanto esses pontos se aproximam de uma reta. Em relações curvilíneas, trechos em que Y sobe e trechos em que Y desce se **cancelam**, e *r* pode ficar perto de zero mesmo quando o padrão é visível no gráfico. Por isso confira sempre o scatter plot antes de calcular.

{: .highlight }
> **Scatter plot (gráfico de dispersão):** cada par de valores (X, Y) vira um ponto no plano. Antes de calcular Pearson, plote sempre as duas variáveis juntas: a nuvem de pontos mostra se a relação é linear, curvilínea ou inexistente, o que o número *r* sozinho não revela.

Em termos de hipótese:

| | |
|:--|:--|
| **H₀** | Não há relação linear entre as variáveis (r = 0 na população). |
| **H₁** | Existe relação linear (r ≠ 0). |

Em dados conversacionais, um exemplo típico cruza duas fontes por estudante: o número de **mensagens trocadas** no chat, extraído dos logs de um chatbot baseado em LLM, e o **escore composto numa escala de metacognição** (ex.: Metacognitive Awareness Inventory — MAI), aplicada separadamente como questionário. A pergunta é: *quanto mais mensagens um estudante troca com o chatbot, maior o seu escore no MAI?* Pearson responde se os pontos tendem a subir numa linha reta, não se um causa o outro.

{: .highlight }
> **Por que usar o escore composto, e não um item isolado do MAI?** O MAI é respondido em itens de escala Likert, que são ordinais. Mas a soma (ou média) de muitos itens ordinais se aproxima de uma distribuição contínua, por isso é aceitável tratá-la como quase-contínua e usar Pearson nesse nível — diferente de correlacionar diretamente com um único item Likert.

---

## 🔢 O que significa r?

| Valor de *r* | Direção | Interpretação intuitiva |
|:-------------|:--------|:------------------------|
| **+1** | positiva | Quanto mais X, mais Y, em linha reta perfeita. |
| **0** | nenhuma | X e Y variam de forma independente (linearmente). |
| **−1** | negativa | Quanto mais X, menos Y, em linha reta perfeita. |
| **entre 0 e ±1** | parcial | Há tendência, mas com dispersão em torno da reta. |

O sinal (+ ou −) indica a **direção**; o valor absoluto \|r\| indica a **força** da relação linear.

{: .highlight }
> **Convenção de Cohen (1988) para o tamanho do efeito:** \|r\| < 0,10 negligível · 0,10 a 0,29 pequeno · 0,30 a 0,49 médio · ≥ 0,50 grande

---

## 📋 Quando usar

**Use Pearson quando:**

- ✅ Ambas as variáveis são **contínuas** e numéricas (mensagens, escores compostos, tempo em segundos).
- ✅ A relação esperada é **linear**: os pontos, ao serem plotados, tendem a formar uma reta (não uma curva). Confira sempre com um scatter plot antes de calcular.
- ✅ Cada variável, isoladamente, deve seguir uma distribuição aproximadamente normal (teste de Shapiro Wilk): a maioria dos estudantes fica perto de um valor "médio", e cada vez menos estudantes aparecem conforme os valores se afastam dessa média.

**Exemplos em logs educacionais (learning analytics):**

- *Número de mensagens × escore composto no MAI:* estudantes que trocam mais mensagens com o chatbot têm maior consciência metacognitiva?
- *Tempo ativo no chatbot × nota na avaliação:* quem permanece mais tempo na plataforma obtém notas mais altas?
- *Número de mensagens × acertos em exercícios:* mais mensagens trocadas se associam a mais respostas certas?
- *Latência média de resposta × tempo total de sessão:* respostas mais rápidas acompanham sessões mais longas?
- *Sessões concluídas por semana × desempenho acumulado:* frequência de uso se correlaciona com progresso ao longo do curso?

**Evite Pearson quando:**

- ❌ Os dados são **ordinais**, como um item isolado de escala Likert (1 a 5) → use [Spearman](../03spearman/spearman.html).
- ❌ Há **outliers extremos**: um único ponto pode distorcer *r*.
- ❌ A nuvem de pontos é claramente **curvilínea** → Pearson não captura bem o padrão.
- ❌ Você quer afirmar **causalidade**: correlação só descreve associação.

{: .highlight }
> **Por que evitar Pearson com um item Likert isolado?** Os números de 1 a 5 indicam apenas ordem (5 é mais concordância que 4), não uma régua com espaçamento igual entre eles. Pearson, porém, calcula a distância matemática entre os números como se 5 − 4 valesse exatamente o mesmo que 2 − 1. Na prática, para uma pessoa, sair de "discordo" (2) para "neutro" (3) pode ser um salto de opinião muito maior do que sair de "concordo" (4) para "concordo totalmente" (5) — mas Pearson trataria os dois saltos como idênticos. Spearman compara apenas o *ranking* das respostas, por isso não sofre com esse problema.

**Quando evitar em logs educacionais (learning analytics):**

- *Satisfação com o chatbot (Likert 1 a 5) × número de sessões:* variável ordinal → use [Spearman](../03spearman/spearman.html).
- *Turnos por sessão × escore com ponto ideal no meio:* sessões com **poucos turnos** (desengajamento, abandono rápido) e sessões com **muitos turnos** (confusão, divagação ou dificuldade excessiva) podem ter escores baixos; o melhor desempenho costuma ficar em um intervalo intermediário. No scatter plot, a nuvem forma uma curva (∩), não uma reta. Pearson pode retornar *r* ≈ 0 mesmo com padrão visível, porque trechos opostos se cancelam.
- *Um único estudante com centenas de mensagens × tempo de sessão:* outlier extremo pode inflar ou distorcer *r*.
- *Uso do chatbot × nota final para inferir causalidade:* mais tempo na plataforma não prova que o chatbot produziu o aprendizado.
- *Tempo de sessão com distribuição fortemente assimétrica (cauda longa):* normalidade comprometida → considere Spearman ou transformação dos dados.

---

## 🪜 Passo a passo na prática

1. **Visualize:** plote X × Y. A nuvem sobe, desce ou é um emaranhado?
2. **Verifique pressupostos:** normalidade univariada (Shapiro Wilk) e ausência de outliers gritantes.
3. **Calcule:** `stats.pearsonr(x, y)` ou `df.corr(method='pearson')`.
4. **Interprete:** leia *r* (direção e força) e *p* (evidência contra H₀).
5. **Reporte:** informe *r*, *p*, *n* e, se possível, o scatter plot no artigo ou relatório.

---

## 📖 Como ler o resultado

Suponha que o código abaixo retorne `r = 0.87, p = 0.0003` com *n* = 10 estudantes:

- **r = 0,87** → relação linear **forte e positiva**: estudantes que trocam mais mensagens tendem a ter escore composto maior no MAI.
- **p < .05** → rejeitamos H₀: a associação linear observada é improvável se não houvesse relação na população.
- **Cohen** → \|0,87\| ≥ 0,50 → tamanho de efeito **grande** (embora com *n* pequeno a estimativa seja instável).

{: .highlight }
> **Correlação ≠ causalidade.** Mais mensagens podem acompanhar maior consciência metacognitiva, ou estudantes mais metacognitivos simplesmente conversam mais *e* refletem mais sobre o próprio aprendizado. Outras variáveis (motivação, dificuldade da tarefa) podem explicar ambos.

---

## 🐍 Exemplo Python

**Contexto:** verificar se o número de mensagens trocadas com o chatbot se associa ao escore composto no MAI.

O código segue o passo a passo: primeiro o gráfico, depois o cálculo. Execute e compare o scatter plot com o valor de *r*.

<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZApmcm9tIHNjaXB5IGltcG9ydCBzdGF0cwppbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CgpkZiA9IHBkLkRhdGFGcmFtZSh7CiAgICAnbWVuc2FnZW5zJzogWzQsNywzLDksNSwxMSw2LDgsMiwxMF0sCiAgICAnbWFpX3Njb3JlJzogWzUyLDcxLDQ4LDgwLDYwLDg1LDY2LDc1LDQwLDgyXQp9KQoKIyBQYXNzbyAxOiBzZW1wcmUgdmlzdWFsaXplIGFudGVzCmRmLnBsb3Quc2NhdHRlcih4PSdtZW5zYWdlbnMnLCB5PSdtYWlfc2NvcmUnLCBjb2xvcj0nI2M3OTJlYScsCiAgICAgICAgICAgICAgIHRpdGxlPSdNZW5zYWdlbnMgw5cgRXNjb3JlIGNvbXBvc3RvIG5vIE1BSScpCnBsdC5zaG93KCkKCiMgUGFzc28gMjogY2FsY3VsYXIKciwgcCA9IHN0YXRzLnBlYXJzb25yKGRmWydtZW5zYWdlbnMnXSwgZGZbJ21haV9zY29yZSddKQpwcmludChmInIgPSB7cjouM2Z9LCBwID0ge3A6LjRmfSIp" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false"></textarea>
  <pre class="code-output"></pre>
</div>

---

## 📚 Referências

| | |
|:--|:--|
| **clássico** | Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Lawrence Erlbaum. |
| **didático** | Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6ª ed.). SAGE. Cap. 8. |
| **python** | McKinney, W. (2022). *Python for Data Analysis* (3ª ed.). O'Reilly. Cap. 13. |
| **artigo** | Mukaka, M. M. (2012). A guide to appropriate use of correlation coefficient in medical research. *Malawi Medical Journal, 24*(3), 69 a 71. |
| **web (PT)** | [Peixoto, *Introdução à Ciência de Dados*: Correlação](https://gcpeixoto.github.io/ICD/ipynb/12-correlacao.html). Scatter plots, interpretação de *r*, Pearson vs relações não lineares, `pearsonr()`. |
| **web (PT)** | [Matos, *Estatística + R*: Correlação entre variáveis](https://ana-mat-br.github.io/correla%C3%A7%C3%A3o-entre-vari%C3%A1veis.html). Gráficos de dispersão, matriz de correlação, quando usar Pearson e Spearman. |
| **web (EN)** | [OpenStax, *Introductory Statistics 2e*: cap. 12.2 e 12.3](https://openstax.org/books/introductory-statistics-2e/pages/12-2-scatter-plots). Scatter plots e coeficiente de correlação, gratuito, com exemplos educacionais. |
| **web (EN)** | [Khan Academy: Correlation coefficient review](https://www.khanacademy.org/math/statistics-probability/describing-relationships-quantitative-data/scatterplots-and-correlation/a/correlation-coefficient-review). Interpretação visual de *r* e exercícios de associação gráfico × coeficiente. |
| **simulador** | [R Psychologist: Understanding Correlations](https://rpsychologist.com/correlation/). Ajuste *r* com slider, arraste pontos e observe o efeito de outliers na nuvem. |
| **simulador** | [Art of Stat: Scatterplots & Correlation](https://istats.shinyapps.io/Association_Quantitative/). Mova ou remova pontos, sobreponha reta de tendência e teste a robustez de *r*. |
| **simulador** | [Art of Stat: Guess the Correlation](https://istats.shinyapps.io/guesscorr/). Treine estimar *r* a partir de scatter plots gerados aleatoriamente. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
