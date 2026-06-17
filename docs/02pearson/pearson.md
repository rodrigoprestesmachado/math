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
> Pearson quantifica essa sincronia, mas *só enquanto a pista for reta*. Em relações curvas (por exemplo, poucos turnos *e* muitos turnos levam a escores baixos), o coeficiente pode subestimar ou ocultar o padrão.

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

Em dados conversacionais, um **turno** é cada intervenção no diálogo, por exemplo uma mensagem do estudante ou do chatbot. A pergunta típica é: *quanto maior o número de turnos em uma sessão, maior o escore de compreensão do estudante?* Pearson responde se os pontos tendem a subir numa linha reta, não se um causa o outro.

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

- ✅ Ambas as variáveis são **contínuas** e numéricas (turnos, escores, tempo em segundos).
- ✅ A relação esperada é **linear**; confira sempre com um scatter plot antes de calcular.
- ✅ Cada variável segue aproximadamente distribuição normal (teste de Shapiro Wilk).

**Exemplos em logs educacionais (learning analytics):**

- *Turnos por sessão × escore de compreensão:* sessões com mais interações tendem a ter escores maiores?
- *Tempo ativo no chatbot × nota na avaliação:* quem permanece mais tempo na plataforma obtém notas mais altas?
- *Número de mensagens × acertos em exercícios:* mais mensagens trocadas se associam a mais respostas certas?
- *Latência média de resposta × tempo total de sessão:* respostas mais rápidas acompanham sessões mais longas?
- *Sessões concluídas por semana × desempenho acumulado:* frequência de uso se correlaciona com progresso ao longo do curso?

**Evite Pearson quando:**

- ❌ Os dados são **ordinais** (escala Likert) → use [Spearman](../03spearman/spearman.html).
- ❌ Há **outliers extremos**: um único ponto pode distorcer *r*.
- ❌ A nuvem de pontos é claramente **curvilínea** → Pearson não captura bem o padrão.
- ❌ Você quer afirmar **causalidade**: correlação só descreve associação.

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

Suponha que o código abaixo retorne `r = 0.87, p = 0.0003` com *n* = 10 sessões:

- **r = 0,87** → relação linear **forte e positiva**: sessões com mais turnos tendem a ter escores maiores.
- **p < .05** → rejeitamos H₀: a associação linear observada é improvável se não houvesse relação na população.
- **Cohen** → \|0,87\| ≥ 0,50 → tamanho de efeito **grande** (embora com *n* pequeno a estimativa seja instável).

{: .highlight }
> **Correlação ≠ causalidade.** Mais turnos podem acompanhar maior compreensão, ou estudantes mais engajados simplesmente conversam mais *e* aprendem mais. Outras variáveis (motivação, dificuldade da tarefa) podem explicar ambos.

---

## 🐍 Exemplo Python

**Contexto:** verificar se o número de turnos por sessão se associa ao escore de compreensão.

O código segue o passo a passo: primeiro o gráfico, depois o cálculo. Execute e compare o scatter plot com o valor de *r*.

<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZApmcm9tIHNjaXB5IGltcG9ydCBzdGF0cwppbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CgpkZiA9IHBkLkRhdGFGcmFtZSh7CiAgICAndHVybm9zJzogICAgICBbNCw3LDMsOSw1LDExLDYsOCwyLDEwXSwKICAgICdlc2NvcmVfY29tcCc6IFs1Miw3MSw0OCw4MCw2MCw4NSw2Niw3NSw0MCw4Ml0KfSkKCiMgUGFzc28gMTogc2VtcHJlIHZpc3VhbGl6ZSBhbnRlcwpkZi5wbG90LnNjYXR0ZXIoeD0ndHVybm9zJywgeT0nZXNjb3JlX2NvbXAnLCBjb2xvcj0nI2M3OTJlYScsCiAgICAgICAgICAgICAgIHRpdGxlPSdUdXJub3Mgw5cgRXNjb3JlIGRlIENvbXByZWVuc8OjbycpCnBsdC5zaG93KCkKCiMgUGFzc28gMjogY2FsY3VsYXIKciwgcCA9IHN0YXRzLnBlYXJzb25yKGRmWyd0dXJub3MnXSwgZGZbJ2VzY29yZV9jb21wJ10pCnByaW50KGYiciA9IHtyOi4zZn0sIHAgPSB7cDouNGZ9Iik=" markdown="0">
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
