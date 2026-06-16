---
layout: default
title: Correlação de Pearson
nav_order: 4
parent: Encontros
has_children: false
---

# Enc. 2 — Correlação de Pearson

`scipy.stats.pearsonr · pandas DataFrame.corr(method='pearson')`
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
> Pense em dois atletas correndo numa pista lado a lado. Quando um acelera, o outro também acelera na mesma proporção; quando um desacelera, o outro acompanha. Isso é **r = +1**: movem-se em perfeita sincronia na mesma direção. Se um acelera e o outro desacelera exatamente na mesma medida, temos **r = −1**. Se cada um faz o que quer, independentemente do outro, **r ≈ 0**.
>
> Pearson mede essa sincronia — mas *apenas quando a pista é reta*. Se a relação for curva (por exemplo, muito poucos turnos *e* muitos turnos levam a escores baixos), Pearson pode subestimar ou mascarar o padrão.

---

## 🎯 Para que serve

Mede a **força** e a **direção** de uma relação *linear* entre duas variáveis numéricas contínuas. O coeficiente *r* vai de −1 a +1.

Em termos de hipótese:

| | |
|:--|:--|
| **H₀** | Não há relação linear entre as variáveis (r = 0 na população). |
| **H₁** | Existe relação linear (r ≠ 0). |

Em dados conversacionais, a pergunta típica é: *quanto maior o número de turnos em uma sessão, maior o escore de compreensão do estudante?* Pearson responde se os pontos tendem a subir numa linha reta — não se um causa o outro.

---

## 🔢 O que significa r?

| Valor de *r* | Direção | Interpretação intuitiva |
|:-------------|:--------|:------------------------|
| **+1** | positiva | Quanto mais X, mais Y — em linha reta perfeita. |
| **0** | nenhuma | X e Y variam de forma independente (linearmente). |
| **−1** | negativa | Quanto mais X, menos Y — em linha reta perfeita. |
| **entre 0 e ±1** | parcial | Há tendência, mas com dispersão em torno da reta. |

O sinal (+ ou −) indica a **direção**; o valor absoluto \|r\| indica a **força** da relação linear.

{: .highlight }
> **Convenção de Cohen (1988) para o tamanho do efeito:** \|r\| < 0,10 negligível · 0,10–0,29 pequeno · 0,30–0,49 médio · ≥ 0,50 grande

---

## 📋 Quando usar

**Use Pearson quando:**

- ✅ Ambas as variáveis são **contínuas** e numéricas (turnos, escores, tempo em segundos).
- ✅ A relação esperada é **linear** — sempre confira com um scatter plot antes de calcular.
- ✅ Cada variável segue aproximadamente distribuição normal (teste de Shapiro-Wilk).

**Evite Pearson quando:**

- ❌ Os dados são **ordinais** (escala Likert) → use [Spearman](../03spearman/spearman.html).
- ❌ Há **outliers extremos** — um único ponto pode distorcer *r*.
- ❌ A nuvem de pontos é claramente **curvilínea** → Pearson não captura bem o padrão.
- ❌ Você quer afirmar **causalidade** — correlação só descreve associação.

---

## 🪜 Passo a passo na prática

1. **Visualize** — plote X × Y. A nuvem sobe, desce ou é um emaranhado?
2. **Verifique pressupostos** — normalidade univariada (Shapiro-Wilk) e ausência de outliers gritantes.
3. **Calcule** — `stats.pearsonr(x, y)` ou `df.corr(method='pearson')`.
4. **Interprete** — leia *r* (direção e força) e *p* (evidência contra H₀).
5. **Reporte** — informe *r*, *p*, *n* e, se possível, o scatter plot no artigo ou relatório.

---

## 📖 Como ler o resultado

Suponha que o código abaixo retorne `r = 0.87, p = 0.0003` com *n* = 10 sessões:

- **r = 0,87** → relação linear **forte e positiva**: sessões com mais turnos tendem a ter escores maiores.
- **p < .05** → rejeitamos H₀: a associação linear observada é improvável se não houvesse relação na população.
- **Cohen** → \|0,87\| ≥ 0,50 → tamanho de efeito **grande** (embora com *n* pequeno a estimativa seja instável).

{: .highlight }
> **Correlação ≠ causalidade.** Mais turnos podem acompanhar maior compreensão — ou estudantes mais engajados simplesmente conversam mais *e* aprendem mais. Outras variáveis (motivação, dificuldade da tarefa) podem explicar ambos.

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
| **artigo** | Mukaka, M. M. (2012). A guide to appropriate use of correlation coefficient in medical research. *Malawi Medical Journal, 24*(3), 69–71. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
