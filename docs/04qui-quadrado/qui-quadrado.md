---
layout: default
title: Qui-quadrado e V de Cramér
nav_order: 4
parent: Associação
has_children: false
---

# Enc. 4: Qui-quadrado e V de Cramér

`scipy.stats.chi2_contingency · cálculo manual de V`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/04qui-quadrado/slides/index.html#/" title="Qui-quadrado e V de Cramér" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Um restaurante serve três pratos, factual, conceitual e procedimental, para três tipos de clientes, conforme o quanto cada um já usa o chatbot: passivo, ativo e intensivo. Se o tipo de cliente não tivesse nenhuma relação com o prato escolhido, esperaríamos que os pratos se distribuíssem na mesma proporção em cada grupo de clientes, refletindo apenas o quão popular cada prato é no geral. O qui-quadrado (χ²) compara essa distribuição *esperada* (sem relação alguma) com o que foi de fato *observado* nas mesas do restaurante.
>
> Quanto maior a diferença entre o observado e o esperado, maior o χ², e mais evidência de que o tipo de cliente influencia o prato escolhido. O **V de Cramér** entra depois, para dizer o quão forte é essa influência, de um jeito que não depende de quantas mesas foram servidas.

{: .highlight }
> **Por que não basta olhar o χ²?** O valor de χ² cresce junto com o tamanho da amostra: com muitas observações, até uma associação fraquíssima pode gerar um χ² grande e um *p* pequeno. Por isso χ² responde apenas *existe associação?* (significância), enquanto o V de Cramér responde *quão forte é essa associação?* (tamanho do efeito), de forma comparável entre estudos com amostras diferentes.

---

## 🎯 Para que serve

Testa se duas variáveis **categóricas nominais** (categorias sem ordem natural, como o tipo de pergunta ou o perfil de uso) são **independentes** uma da outra. O resultado é organizado numa **tabela de contingência**: cada linha é uma categoria da primeira variável, cada coluna é uma categoria da segunda, e cada célula conta quantos estudantes caem naquela combinação.

{: .highlight }
> **O que é uma variável categórica nominal?** É uma variável cujos valores são rótulos, sem ordem ou distância numérica entre eles: "factual", "conceitual" e "procedimental" não têm um "maior que" natural entre si, ao contrário de uma escala Likert (ordinal) ou de uma contagem de mensagens (contínua). Qui-quadrado foi feito exatamente para esse tipo de dado.

Em termos de hipótese:

| | |
|:--|:--|
| **H₀** | As duas variáveis são independentes (não há associação na população). |
| **H₁** | As duas variáveis são associadas (a distribuição de uma varia conforme a categoria da outra). |

Em dados conversacionais, um exemplo típico cruza o **tipo de pergunta** feita ao chatbot (factual, conceitual, procedimental), extraído dos logs de um chatbot baseado em LLM, com o **perfil de uso** do estudante (passivo, ativo, intensivo), também derivado da frequência de interação. A pergunta é: *o tipo de pergunta que o estudante faz varia conforme o quanto ele usa o chatbot?* O qui-quadrado responde se essas duas categorias estão associadas, não qual delas "causa" a outra.

{: .highlight }
> **Por que agrupar em perfis, e não usar o número de mensagens direto?** Quando o objetivo é comparar categorias (por exemplo, "quem usa pouco" versus "quem usa muito"), é comum transformar uma variável contínua em faixas nominais ou ordinais. Isso simplifica a leitura da tabela de contingência, mas descarta informação: sempre que a variável original for contínua e a pergunta permitir, prefira Pearson ou Spearman, que aproveitam melhor essa informação.

---

## 🧮 Fórmula

O χ² soma, célula a célula da tabela de contingência, o quanto o valor **observado** (O) se afasta do valor **esperado** (E) caso as duas variáveis fossem realmente independentes, como no exemplo do restaurante: quanto mais as mesas reais se afastam do que seria esperado sem nenhuma relação entre cliente e prato, maior o χ².

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

{: .highlight }
> **Lendo a fórmula:** *Oᵢ* é a frequência **observada** em cada célula da tabela de contingência; *Eᵢ* é a frequência **esperada** naquela mesma célula, caso as variáveis fossem independentes; Σ soma o resultado para todas as células. A frequência esperada de uma célula é calculada por *Eᵢ* = (total da linha × total da coluna) / total geral.

**Como χ² é calculado, passo a passo:**

1. Monte a tabela de contingência com as frequências **observadas** (O) em cada célula.
2. Calcule os totais de cada linha, de cada coluna, e o total geral (n).
3. Para cada célula, calcule a frequência **esperada**: E = (total da linha × total da coluna) / n.
4. Para cada célula, calcule (O − E)² / E.
5. Some o resultado de todas as células → **χ²**.

**Aplicação simples: aplicando os passos a 40 estudantes**

Para ver os passos acima em ação, seguem 40 estudantes fictícios, cruzando o **tipo de pergunta** (factual ou conceitual) com o **nível do estudante** (iniciante ou avançado), o mesmo tipo de cruzamento usado no exemplo Python mais abaixo, só que numa tabela 2×2 menor, para facilitar a conta à mão:

| | Factual (O) | Conceitual (O) | Total da linha |
|:--|:-:|:-:|:-:|
| **Iniciante** | 15 | 5 | 20 |
| **Avançado** | 5 | 15 | 20 |
| **Total da coluna** | 20 | 20 | **n = 40** |

1. **Totais** (passos 1–2): linhas = 20 e 20; colunas = 20 e 20; n = 40.
2. **Esperadas** (passo 3): como as duas linhas e as duas colunas têm o mesmo total, todas as células esperam E = (20 × 20) / 40 = **10**.
3. **(O − E)² / E** (passo 4): (15−10)²/10 = 2,5 · (5−10)²/10 = 2,5 · (5−10)²/10 = 2,5 · (15−10)²/10 = 2,5.
4. **Resultado** (passo 5): χ² = 2,5 + 2,5 + 2,5 + 2,5 = **10,00**, com 1 grau de liberdade.

{: .highlight }
> **Interpretação:** χ² = 10,00 nesses 40 estudantes fictícios é grande o suficiente para rejeitar H₀ (para 1 grau de liberdade, valores de χ² acima de 3,84 já levam a *p* < .05): iniciantes e avançados parecem, sim, preferir tipos diferentes de pergunta. No exemplo Python mais abaixo, `scipy.stats.chi2_contingency` faz exatamente essa conta, só que para uma tabela 3×3 com os 3 perfis de uso do conjunto de dados completo.

---

## 📐 V de Cramér

O χ² diz apenas se a associação existe (significância). Para saber **quão forte** ela é, de um jeito que não infla sozinho conforme n cresce, usamos o V de Cramér, que reescala o χ² pelo tamanho da amostra e pelo formato da tabela:

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

{: .highlight }
> **Lendo a fórmula:** *n* é o total de estudantes na tabela; *k* é o menor entre (número de linhas − 1) e (número de colunas − 1). Dividir χ² por n remove o efeito do tamanho da amostra; dividir por k ajusta para tabelas maiores que 2×2, onde χ² tende naturalmente a crescer com mais categorias. O resultado, √, fica sempre entre 0 (nenhuma associação) e 1 (associação perfeita).

**Aplicando aos 40 estudantes do exemplo acima:** a tabela é 2×2, logo k = min(2−1, 2−1) = 1. V = √(10 / (40 × 1)) = √0,25 = **0,50**.

{: .highlight }
> **Interpretação:** V = 0,50 indica uma associação **grande** entre o nível do estudante e o tipo de pergunta feito, segundo a convenção de Cohen abaixo. Sozinho, χ² = 10,00 e *p* < .05 já indicam que a associação existe; V = 0,50 mostra que, além de existir, ela é forte.

---

## 🔢 O que significa V?

| Valor de V | Força da associação |
|:-----------|:---------------------|
| **≈ 0,10** | pequena |
| **≈ 0,30** | média |
| **≈ 0,50** | grande |

{: .highlight }
> **Convenção de Cohen (1988) para o tamanho do efeito:** essas referências valem para tabelas com k = 1 (ex.: 2×2). Para tabelas maiores, os limiares de Cohen são um pouco diferentes por linha de k, mas a leitura prática, quanto maior o V, mais forte a associação, permanece a mesma.

---

## 📋 Quando usar

**Use qui-quadrado e V de Cramér quando:**

- ✅ Ambas as variáveis são **categóricas nominais** (sem ordem natural entre as categorias).
- ✅ As observações são **independentes** entre si: cada estudante contribui para uma única célula da tabela.
- ✅ A frequência **esperada** é maior ou igual a 5 em pelo menos 80% das células, e nenhuma célula tem frequência esperada abaixo de 1.

{: .highlight }
> **Por que a frequência esperada importa?** O χ² é uma aproximação estatística que só funciona bem quando as células têm frequência esperada suficiente. Com células muito pequenas, essa aproximação fica pouco confiável, e o teste tende a errar tanto para mais quanto para menos. Nesses casos, prefira o teste exato de Fisher, explicado na próxima seção.

**Exemplos em logs educacionais (learning analytics):**

- *Tipo de pergunta (factual, conceitual, procedimental) × perfil de uso (passivo, ativo, intensivo):* o tipo de pergunta que o estudante faz varia conforme o quanto ele usa o chatbot?
- *Turno do dia em que o estudante mais usa o chatbot (manhã, tarde, noite) × modalidade da disciplina (presencial, híbrida, remota):* o horário de uso está associado à modalidade do curso?
- *Categoria do erro mais comum (sintaxe, lógica, interpretação) × turma:* turmas diferentes cometem tipos diferentes de erro com mais frequência?
- *Uso ou não de um recurso opcional do chatbot (sim/não) × aprovação na disciplina (sim/não):* estudantes que usam o recurso têm uma proporção de aprovação diferente?

**Evite qui-quadrado quando:**

- ❌ Uma das variáveis é **ordinal**, como uma escala Likert → use [Spearman](../03spearman/spearman.html), que aproveita a ordem das categorias.
- ❌ As observações **não são independentes**, como o mesmo estudante contribuindo várias vezes para a mesma célula.
- ❌ Muitas células têm frequência esperada abaixo de 5, especialmente em tabelas pequenas (tipicamente 2×2) → use o teste exato de Fisher.
- ❌ Você quer afirmar **causalidade**: associação entre categorias não prova que uma categoria causa a outra.

**Quando evitar em logs educacionais (learning analytics):**

- *Satisfação com o chatbot (Likert 1 a 5) × perfil de uso:* a satisfação é ordinal → considere [Spearman](../03spearman/spearman.html) em vez de agrupá-la em categorias nominais.
- *Um mesmo estudante contando várias vezes na mesma célula*, por exemplo, uma linha por mensagem enviada em vez de uma linha por estudante: viola a independência das observações e infla artificialmente o χ².
- *Tabela 2×2 com poucos estudantes em um grupo raro* (ex.: apenas 3 estudantes usam uma modalidade pouco comum): frequência esperada baixa → prefira o teste exato de Fisher.
- *Tipo de pergunta × nota final para inferir causalidade:* uma associação entre o tipo de pergunta e o desempenho não prova que perguntar de um certo jeito melhora (ou piora) a nota.

---

## 📐 Teste exato de Fisher

O teste exato de Fisher é uma alternativa ao qui-quadrado quando as frequências esperadas são baixas, o cenário mais comum em tabelas 2×2 com amostras pequenas ou com grupos bem desbalanceados. Em vez de uma aproximação estatística, ele calcula exatamente a probabilidade de observar uma tabela tão ou mais extrema que a observada, assumindo H₀ verdadeira.

Em termos de hipótese, as mesmas do qui-quadrado:

| | |
|:--|:--|
| **H₀** | As duas variáveis são independentes (não há associação na população). |
| **H₁** | As duas variáveis são associadas. |

**Como decidir entre χ² e Fisher:**

- **Frequência esperada ≥ 5 em pelo menos 80% das células** → o qui-quadrado é uma boa aproximação, use `chi2_contingency`.
- **Alguma célula com frequência esperada abaixo de 5**, sobretudo em tabelas 2×2 → prefira o teste exato de Fisher, `scipy.stats.fisher_exact`, que não depende dessa aproximação.

{: .highlight }
> **Fisher também funciona com frequências altas.** A exigência de frequência esperada ≥ 5 é um requisito do qui-quadrado, não do teste de Fisher. Fisher é exato em qualquer tamanho de amostra, mas seu cálculo fica computacionalmente mais caro em tabelas grandes, por isso, na prática, ele é reservado para os casos em que o χ² não é confiável.

---

## 🪜 Passo a passo na prática

1. **Visualize:** monte a tabela de contingência entre as duas variáveis categóricas.
2. **Verifique pressupostos:** as observações são independentes? A frequência esperada é suficiente em cada célula (ou é hora de usar Fisher)?
3. **Calcule:** `stats.chi2_contingency(tabela)` para χ², *p* e as frequências esperadas; depois `V = np.sqrt(chi2 / (n * k))` para o tamanho do efeito.
4. **Interprete:** leia *p* (evidência contra H₀) e V (força da associação), nunca apenas um dos dois.
5. **Reporte:** informe χ², graus de liberdade, *p*, *n*, V de Cramér e, se possível, a tabela de contingência no artigo ou relatório.

---

## 📖 Como ler o resultado

Suponha que o código abaixo retorne `χ² = 18.203, gl = 4, p = 0.0011` e `V = 0.301` com *n* = 138 estudantes:

- **χ² = 18,203, p = 0,0011** → rejeitamos H₀: é pouco provável observar uma tabela tão desigual quanto essa se o tipo de pergunta e o perfil de uso fossem realmente independentes.
- **V = 0,301** → segundo Cohen, um efeito **médio a grande** (perto do limiar de 0,30): a associação existe e tem magnitude relevante, não é apenas um resultado estatisticamente significativo por causa do tamanho da amostra.
- **Conjunto** → o tipo de pergunta que o estudante faz ao chatbot varia de forma perceptível conforme o seu perfil de uso.

{: .highlight }
> **Associação ≠ causalidade.** Um perfil de uso mais intensivo pode levar o estudante a fazer perguntas mais elaboradas, ou estudantes que já fazem perguntas mais elaboradas podem se engajar mais e, por isso, usar mais o chatbot. Outras variáveis (interesse pela disciplina, familiaridade prévia com o tema) podem explicar ambos.

---

## 🐍 Exemplo Python: Qui-quadrado e V de Cramér

**Contexto:** verificar se o tipo de pergunta feito ao chatbot (factual, conceitual, procedimental) varia conforme o perfil de uso do estudante (passivo, ativo, intensivo).

O código monta a tabela de contingência, calcula χ² e *p*, e em seguida calcula o V de Cramér a partir do mesmo χ².

<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZAppbXBvcnQgbnVtcHkgYXMgbnAKZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgY2hpMl9jb250aW5nZW5jeQoKIyBQYXNzbyAxOiBtb250YXIgYSB0YWJlbGEgZGUgY29udGluZ2VuY2lhCnRhYmVsYSA9IHBkLkRhdGFGcmFtZSgKICAgIFtbMzAsMTUsMTBdLFsyMCwyNSwxOF0sWzEwLDIwLDM1XV0sCiAgICBpbmRleCAgID0gWydmYWN0dWFsJywnY29uY2VpdHVhbCcsJ3Byb2NlZGltZW50YWwnXSwKICAgIGNvbHVtbnMgPSBbJ3Bhc3Npdm8nLCdhdGl2bycsJ2ludGVuc2l2byddCikKcHJpbnQodGFiZWxhLCAiXG4iKQoKIyBQYXNzbyAyOiBjYWxjdWxhciBxdWktcXVhZHJhZG8sIHAtdmFsb3IsIGdyYXVzIGRlIGxpYmVyZGFkZSBlIGVzcGVyYWRhcwpjaGkyLCBwLCBnbCwgZXNwZXJhZGFzID0gY2hpMl9jb250aW5nZW5jeSh0YWJlbGEpCnByaW50KGYiz4fCsiA9IHtjaGkyOi4zZn0gIGdsID0ge2dsfSAgcCA9IHtwOi40Zn0iKQoKIyBQYXNzbyAzOiBjYWxjdWxhciBWIGRlIENyYW1lciBhIHBhcnRpciBkbyBtZXNtbyBxdWktcXVhZHJhZG8KbiA9IHRhYmVsYS52YWx1ZXMuc3VtKCkKayA9IG1pbih0YWJlbGEuc2hhcGUpIC0gMQpWID0gbnAuc3FydChjaGkyIC8gKG4gKiBrKSkKZWZlaXRvID0gJ3BlcXVlbm8nIGlmIFYgPCAuMyBlbHNlICdtw6lkaW8nIGlmIFYgPCAuNSBlbHNlICdncmFuZGUnCnByaW50KGYiViBkZSBDcmFtw6lyID0ge1Y6LjNmfSAg4oaSIGVmZWl0byB7ZWZlaXRvfSIp" markdown="0">
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
| **seminal** | Cramér, H. (1946). *Mathematical Methods of Statistics*. Princeton University Press. |
| **didático** | Agresti, A. (2013). *Categorical Data Analysis* (3ª ed.). Wiley. |
| **didático** | Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6ª ed.). SAGE. Cap. 19. |
| **tamanho efeito** | Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Lawrence Erlbaum. Cap. 7. |
| **crítico** | Kim, H. Y. (2017). Chi-squared test and Fisher's exact test. *Restorative Dentistry & Endodontics, 42*(2), 152 a 155. |
| **teste exato** | Fisher, R. A. (1922). On the interpretation of χ² from contingency tables, and the calculation of P. *Journal of the Royal Statistical Society, 85*(1), 87 a 94. |
| **web (EN)** | [OpenStax, *Introductory Statistics 2e*: cap. 11.3](https://openstax.org/books/introductory-statistics-2e/pages/11-3-test-of-independence). Teste de independência qui-quadrado, gratuito, com exemplos passo a passo. |
| **simulador** | [Art of Stat: Chi-Square Test for Association](https://istats.shinyapps.io/ChisqTest/). Monte tabelas de contingência, ajuste frequências e observe o efeito no χ² e no p-valor. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
