---
layout: default
title: Regressão Linear (simples e múltipla)
nav_order: 1
parent: Predição
has_children: false
---

# Enc. 11 — Regressão Linear (simples e múltipla)

Estimar a nota com uma reta · `statsmodels.formula.api.ols()`
{: .fs-5 .fw-300 }

---

## 📊 Slides

<center>
<iframe src="https://math.rpmhub.dev/11regressao-linear/slides/index.html#/" title="Regressão Linear (simples e múltipla)" width="90%" height="500" style="border:none;"></iframe>
</center>

---

## 🍊 Metáfora

> **Imagine isso…**
>
> Uma professora quer estimar a nota final antes da prova. Ela olha os logs do chatbot educacional da disciplina. Cada estudante vira um ponto num gráfico: na horizontal, o número de sessões com o chatbot; na vertical, a nota.
>
> A régua é reta, e os pontos não ficam em fila. Para cada estudante sobra um vão na vertical: a nota real fica alguns pontos acima ou abaixo da nota que a régua marca naquela quantidade de sessões. A professora inclina a régua, e a sobe ou desce, até esses vãos ficarem os menores possíveis no conjunto. Na posição escolhida, a régua tem dois números. O ponto de partida é a nota esperada de quem nunca abriu o chatbot. O outro é quantos pontos cada sessão a mais vale.

<center>
<img src="../imgs/regua-regressao.png" alt="Cinco estudantes no gráfico de sessões com o chatbot pela nota. A reta sobe 5 pontos por sessão, parte de 40, e traços verticais marcam o vão entre a nota real e a nota da régua." width="88%">
</center>

Os cinco pontos são os mesmos estudantes da conta que vem a seguir. A reta é a régua: nota esperada = 40 + 5 × sessões. O trecho tracejado prolonga a régua até quem nunca abriu o chatbot, no ponto de partida 40. Os traços verticais são o vão de cada pessoa: +10 significa que a nota ficou 10 pontos acima da régua; −10, que ficou 10 pontos abaixo.

{: .highlight }
> **Por que o vão de 10 pesa mais?** No gráfico, A ficou 10 pontos acima da régua. B e D ficaram 5 pontos abaixo. 10² = 100, e 5² + 5² = 50: o vão grande pesa mais do que os dois vãos pequenos juntos. A professora soma os vãos depois de elevá-los ao quadrado, para a régua não deixar ninguém muito longe. Essa conta se chama mínimos quadrados. O vão (nota real menos a nota que a régua marcou) se chama resíduo.

A professora percebe um segundo fato. Quem abre o chatbot com mais frequência também costuma refletir mais sobre o próprio estudo. A régua de uma informação só entrega ao chatbot pontos que em parte já vinham dessa reflexão.

A regressão com várias informações troca a régua por uma superfície e faz outra pergunta: entre estudantes com a mesma metacognição e o mesmo letramento em IA, quantos pontos uma sessão a mais ainda acrescenta?

<center>
<img src="../imgs/superficie-regressao.png" alt="Dez estudantes sobre uma superfície de sessões e metacognição pela nota. Uma linha laranja marca o corte com a metacognição parada em 66. Ao lado, o mesmo corte sobe cerca de 2,7 pontos por sessão, com o letramento em IA parado na média." width="96%">
</center>

À esquerda, a régua virou uma superfície. A nota esperada sobe com as sessões e também com a metacognição. O letramento em IA fica parado na média da turma, para o desenho caber em três eixos. A linha laranja é um corte dessa superfície, com a metacognição também parada, em 66. À direita, o mesmo corte visto de frente. Cada sessão a mais ainda acompanha cerca de 2,7 pontos. Os dez pontos são os estudantes da conta com várias informações, mais adiante.

---

## 🎯 Para que serve

A régua da metáfora, e a superfície que entra no lugar dela, são a regressão linear. Ela responde a uma pergunta de sala de aula: *se o estudante fizer mais uma sessão com o chatbot, quantos pontos a nota tende a subir, e que nota esperar de alguém que ainda não fez a prova?*

A resposta é uma regra simples:

<center>nota esperada = ponto de partida + pontos por sessão × número de sessões</center>

O ponto de partida é a nota que a regra estima para quem nunca abriu o chatbot. Os pontos por sessão dizem quanto a nota acompanha cada sessão a mais. Esses dois números saem de quem já tem as duas coisas registradas, as sessões e a nota: a conta mede o quanto a nota acompanha as sessões nesse grupo e devolve a regra. Um estudante que ainda vai fazer a prova já tem as sessões no log do chatbot. Com esse número na regra, dá para estimar a nota dele.

{: .highlight }
> **O que a gente estima aqui é um número que muda aos poucos**, como a nota de uma prova, os minutos numa sessão ou os acertos numa lista de exercícios. Em textos técnicos, esse número aparece como desfecho numérico contínuo, e a informação usada para estimá-lo (as sessões, por exemplo) aparece como preditor.

Três recortes situam este encontro entre os vizinhos do curso:

- [Pearson](../02pearson/pearson.html) (encontro 2) mede se duas coisas sobem juntas. A regressão escreve a regra em pontos: quantos pontos a nota sobe a cada sessão a mais, e que nota esperar de alguém que ainda não apareceu nos dados.
- **Uma informação só** (as sessões) é a regressão linear simples. **Várias ao mesmo tempo** (sessões, metacognição, letramento em IA) é a regressão linear múltipla. Cada número, nessa conta conjunta, é o acréscimo que sobra entre estudantes parecidos nas outras informações.
- Quando a resposta deixa de ser um número como a nota, o método muda. "Engajou ou não engajou" é a [regressão logística](../12regressao-logistica/regressao-logistica.html). "Quantas mensagens a pessoa enviou" é a [regressão de Poisson](../13poisson/poisson.html).

Em termos de hipótese, para cada informação colocada na regra:

| | |
|:--|:--|
| **H₀** | Essa informação não muda a nota (os pontos que ela acrescenta são zero na turma toda). |
| **H₁** | Essa informação acrescenta pontos na nota. |

{: .highlight }
> **A reta descreve o quanto a nota acompanha as sessões.** Um estudante que já domina o conteúdo pode abrir o chatbot com mais frequência e, ao mesmo tempo, tirar uma nota mais alta. A regra registra essa companhia. Ela não mostra que o chatbot produziu a nota.

---

## 🧮 Fórmula

A conta da régua usa, estudante a estudante, o quanto as sessões e a nota se afastam das suas próprias médias. Quando os dois afastamentos vão na mesma direção, o numerador cresce e cada sessão vale mais pontos.

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.15em; margin:8px auto;">
<tr>
<td rowspan="2" style="padding-right:12px; vertical-align:middle;">pontos por sessão =</td>
<td style="text-align:center; padding:2px 12px; border-bottom:2px solid currentColor;">Σ (xᵢ − x̄)(yᵢ − ȳ)</td>
</tr>
<tr>
<td style="text-align:center; padding:2px 12px;">Σ (xᵢ − x̄)²</td>
</tr>
</table>
</center>

<center>ponto de partida = ȳ − (pontos por sessão) × x̄</center>

{: .highlight }
> **Lendo a fórmula:** *xᵢ* é o número de sessões daquele estudante; *yᵢ* é a nota dele; *x̄* e *ȳ* são as médias das sessões e das notas; Σ soma o resultado de todos os estudantes. O numerador junta o quanto sessões e nota andam juntas. O denominador mede o quanto as sessões variam, para que a resposta saia em pontos de nota por sessão.

A fatia da diferença entre as notas que a régua consegue acompanhar é o *R²*:

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.15em; margin:8px auto;">
<tr>
<td rowspan="2" style="padding-right:12px; vertical-align:middle;"><em>R²</em> = 1 −</td>
<td style="text-align:center; padding:2px 12px; border-bottom:2px solid currentColor;">Σ (erro de cada estudante)²</td>
</tr>
<tr>
<td style="text-align:center; padding:2px 12px;">Σ (yᵢ − ȳ)²</td>
</tr>
</table>
</center>

*R²* perto de 1 significa que a régua acompanha quase toda a diferença entre as notas. *R²* perto de 0 significa que a régua quase não ajuda: as notas se espalham por outros motivos.

---

## 🧩 Aplicação simples: a régua na mão

Cinco estudantes fictícios usaram o chatbot educacional da disciplina. *x* é o número de sessões. *y* é a nota final.

| Estudante | xᵢ (sessões) | yᵢ (nota) | xᵢ − x̄ | yᵢ − ȳ | (xᵢ−x̄)(yᵢ−ȳ) | (xᵢ−x̄)² | (yᵢ−ȳ)² |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | 2 | 60 | −4 | −10 | 40 | 16 | 100 |
| B | 4 | 55 | −2 | −15 | 30 | 4 | 225 |
| C | 6 | 60 | 0 | −10 | 0 | 0 | 100 |
| D | 8 | 75 | 2 | 5 | 10 | 4 | 25 |
| E | 10 | 100 | 4 | 30 | 120 | 16 | 900 |
| **Soma** | x̄ = 6 | ȳ = 70 | 0 | 0 | **200** | **40** | **1350** |

1. **Médias:** x̄ = (2+4+6+8+10) / 5 = 6. ȳ = (60+55+60+75+100) / 5 = 70.
2. **Pontos por sessão:** 200 / 40 = **5**.
3. **Ponto de partida:** 70 − 5 × 6 = **40**.
4. **A regra:** nota esperada = 40 + 5 × sessões.

A régua, estudante por estudante:

| Estudante | Sessões | Nota real | Nota prevista | Erro da régua |
|:-:|:-:|:-:|:-:|:-:|
| A | 2 | 60 | 50 | +10 |
| B | 4 | 55 | 60 | −5 |
| C | 6 | 60 | 70 | −10 |
| D | 8 | 75 | 80 | −5 |
| E | 10 | 100 | 90 | +10 |

A soma dos erros ao quadrado é 10² + (−5)² + (−10)² + (−5)² + 10² = 100 + 25 + 100 + 25 + 100 = **350**. A soma dos afastamentos da nota, ao quadrado, é **1350**. Então *R²* = 1 − 350/1350 = 1000/1350 ≈ **0,74**. Cerca de 74% da diferença entre essas notas acompanha a régua. O resto é o erro de cada pessoa.

{: .highlight }
> **Um estudante que ainda não fez a prova**, com 7 sessões no chatbot: nota esperada = 40 + 5 × 7 = **75**. A regra estima. Ela não garante a nota que vai sair no papel.

Com 5 estudantes, o *p* de "pontos por sessão" fica em **0,061**. A reta é visível e o *R²* é alto, mas o grupo é pequeno demais para cravar a decisão: no corte usual de 0,05, ainda não dá para afirmar que, numa turma maior, cada sessão acrescentaria pontos.

---

## 🔢 O que significam os números da régua

| Número | Nome na conta | Leitura nestes 5 estudantes |
|:--|:--|:--|
| **40** | ponto de partida (*b₀*, intercepto) | Nota esperada se as sessões fossem zero. Ninguém deste grupo teve zero sessões (o menor valor é 2), então o 40 é a régua prolongada, não um estudante observado. |
| **5** | pontos por sessão (*b₁*, inclinação) | Cada sessão a mais acompanha cerca de 5 pontos a mais na nota. |
| **0,74** | *R²* | Cerca de 74% da diferença entre as notas acompanha as sessões. Os outros 26% são o erro da régua. |

O sinal dos pontos por sessão diz a direção. Positivo: mais sessões acompanham nota mais alta. Negativo: mais sessões acompanhariam nota mais baixa. Zero: a régua fica na horizontal e as sessões não ajudam a estimar a nota.

---

## 📐 Várias informações ao mesmo tempo

A mesma pergunta, agora com uma turma de 10 estudantes e mais duas informações, além das sessões:

- **metacognição:** um escore de o quanto a pessoa percebe e organiza o próprio estudo;
- **letramento em IA:** um escore de o quanto a pessoa já sabe usar esse tipo de ferramenta.

| Estudante | Nota | Sessões | Metacognição | Letramento em IA |
|:-:|:-:|:-:|:-:|:-:|
| A | 57 | 2 | 48 | 30 |
| B | 63 | 3 | 70 | 42 |
| C | 64 | 4 | 55 | 38 |
| D | 68 | 5 | 62 | 55 |
| E | 81 | 6 | 80 | 48 |
| F | 75 | 7 | 58 | 70 |
| G | 79 | 8 | 74 | 44 |
| H | 84 | 9 | 66 | 60 |
| I | 88 | 10 | 85 | 52 |
| J | 88 | 12 | 60 | 75 |

Quando a conta usa **só as sessões**, cada sessão parece valer cerca de **3,3 pontos**, e o *R²* fica em cerca de **0,90**. Parte da metacognição entra nessa conta, porque quem faz mais sessões também tende a refletir mais sobre o próprio estudo.

Com as três informações juntas, a regra fica, em números arredondados:

<center>nota esperada ≈ 35 + 2,7 × sessões + 0,29 × metacognição + 0,06 × letramento em IA</center>

- **Sessões: cerca de 2,7 pontos** (*p* = 0,001). É o que sobra entre estudantes parecidos em metacognição e em letramento em IA, a inclinação da linha laranja no corte da metáfora. O 3,3 da conta simples caiu para 2,7 porque a reflexão sobre o próprio estudo deixou de ser atribuída ao chatbot.
- **Metacognição: cerca de 0,29 ponto** por ponto de escore (*p* = 0,016).
- **Letramento em IA: cerca de 0,06 ponto** (*p* = 0,58). Nesse grupo, saber usar a ferramenta quase não move a nota, uma vez que sessões e metacognição já estão na conta.
- ***R²* ≈ 0,97.** Cerca de 97% da diferença entre as notas acompanha as três informações juntas. Com 10 estudantes e três informações, um *R²* tão alto é típico de exemplo de aula. Numa turma real, e com um grupo pequeno, a estimativa ainda oscila bastante.

Um estudante com 7 sessões, metacognição 60 e letramento em IA 50 teria nota esperada em torno de **74**.

{: .highlight }
> **VIF, o aviso de informações grudadas.** O VIF (fator de inflação da variância) diz se duas informações sobem e descem juntas demais para separar o papel de cada uma. Abaixo de 5, a separação está tranquila. Acima de 5, o "quantos pontos por sessão" fica misturado com a outra informação, e o número deixa de merecer uma leitura direta. Nesta turma os três VIF ficam em cerca de **3,5** (sessões), **1,5** (metacognição) e **2,9** (letramento em IA).

O nome técnico dessa mistura é multicolinearidade. O nome técnico do número de cada informação, na regra, é coeficiente.

---

## 📋 Quando usar

**Use a regressão linear quando:**

- ✅ A resposta que você quer estimar é um número que muda aos poucos: nota, minutos, acertos, um escore composto.
- ✅ No gráfico, os pontos acompanham uma reta. Cada sessão a mais vem com um acréscimo parecido na nota, não com uma curva.
- ✅ Os erros da régua têm tamanho parecido ao longo de toda a reta. Eles não abrem um leque (erros pequenos de um lado e erros enormes do outro). Em textos técnicos, erros de tamanho parecido se chamam homocedásticos.

**Evite a regressão linear quando:**

- ❌ A resposta é "sim ou não", como engajou ou não engajou. Use a [regressão logística](../12regressao-logistica/regressao-logistica.html).
- ❌ A resposta é uma contagem de eventos, como quantas mensagens a pessoa enviou. Use a [regressão de Poisson](../13poisson/poisson.html). O número de sessões pode entrar na horizontal para estimar uma nota. O que muda o método é a resposta que se quer estimar, não o fato de a sessão ser uma contagem.
- ❌ A nuvem faz uma curva. Muitas mensagens podem marcar confusão, e poucas mensagens podem marcar abandono: a nota fica melhor no meio. A régua reta passa por cima desse arco.
- ❌ Duas informações sobem juntas demais (VIF acima de 5). Dá para ajustar a reta, mas o "quantos pontos" de cada uma fica sem uma leitura limpa.
- ❌ Você quer concluir que o chatbot causou a nota. A regra descreve companhia e serve para estimar. A causa pede outro desenho de pesquisa.

---

## 🔍 Perguntas de pesquisa em Informática na Educação

Em pesquisas que analisam conversas de estudantes com um chatbot educacional, a regressão linear serve quando a resposta é um número e a nuvem no gráfico acompanha uma reta:

- Mais sessões com o chatbot acompanham uma nota final mais alta? Quantos pontos por sessão?
- O tempo total, em minutos, no chatbot estima quantos exercícios a pessoa acerta na semana?
- Entre estudantes com o mesmo escore de metacognição, uma sessão a mais ainda acrescenta pontos na nota?
- O tamanho médio das mensagens do estudante estima a nota da atividade da semana?

{: .highlight }
> **Antes de ajustar a reta:** confirme que a resposta é um número que muda aos poucos, plote o gráfico e olhe se a nuvem é uma reta. Se a resposta for "sim ou não", ou uma contagem de mensagens, troque de encontro.

---

## 🪜 Passo a passo na prática

1. **Desenhe:** plote sessões × nota. A nuvem sobe em linha reta, faz uma curva ou é um emaranhado?
2. **Trace a régua com uma informação só:** `nota ~ sessoes`.
3. **Se outras informações também importam,** coloque-as na mesma conta: metacognição, letramento em IA.
4. **Olhe o VIF.** Acima de 5, duas informações sobem juntas demais para separar o papel de cada uma.
5. **Leia os pontos e o *p*.** *p* < 0,05: esse acréscimo seria improvável se a informação não mudasse a nota num grupo maior.
6. **Reporte:** a regra (ponto de partida e pontos por sessão), o *R²*, o *p*, o número de estudantes e o gráfico. Escreva que a reta acompanha a nota.

---

## 📖 Como ler o resultado

No exemplo de **5 estudantes**, a regra é nota esperada = 40 + 5 × sessões, com *R²* = 0,74 e *p* = 0,061. A régua descreve bem esse grupo. O *p* acima de 0,05 avisa que cinco pessoas não bastam para generalizar.

No exemplo de **10 estudantes**, leia primeiro as frases que o código imprime, e só depois a tabela em inglês do `summary()`:

- **Só as sessões: 3,29 pontos por sessão**, *R²* = 0,90, *p* < 0,001. Cada sessão a mais acompanha cerca de 3,3 pontos, enquanto a conta ignora o resto.
- **Com as três informações:** cerca de 2,67 pontos por sessão (*p* = 0,001), 0,29 ponto por ponto de metacognição (*p* = 0,016) e 0,06 ponto por ponto de letramento em IA (*p* = 0,58). *R²* = 0,97.
- **VIF** em 3,49, 1,45 e 2,93, todos abaixo de 5: dá para separar o papel de cada informação.

{: .highlight }
> **Traduzindo a tabela do `summary()`:** `Intercept` é o ponto de partida. `coef` na linha `sessoes` é quantos pontos a nota sobe por sessão. `P>|t|` é o *p*. `R-squared` é o *R²*. O letramento em IA, com *p* = 0,58, fica na conta e quase não move a nota deste grupo.

---

## 🐍 Exemplo Python: uma informação só

**Contexto:** os mesmos 5 estudantes da conta de mão. A função `ols` traça a régua (a conta dos erros ao quadrado) e o gráfico mostra os pontos com a reta por cima.

<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZAppbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CmltcG9ydCBzdGF0c21vZGVscy5mb3JtdWxhLmFwaSBhcyBzbWYKCmRmID0gcGQuRGF0YUZyYW1lKHsKICAgICdzZXNzb2VzJzogWzIsIDQsIDYsIDgsIDEwXSwKICAgICdub3RhJzogWzYwLCA1NSwgNjAsIDc1LCAxMDBdCn0pCgptb2RlbG8gPSBzbWYub2xzKCdub3RhIH4gc2Vzc29lcycsIGRhdGE9ZGYpLmZpdCgpCnByaW50KGYiUG9udG8gZGUgcGFydGlkYSA9IHttb2RlbG8ucGFyYW1zWydJbnRlcmNlcHQnXTouMWZ9IikKcHJpbnQoZiJQb250b3MgcG9yIHNlc3PDo28gPSB7bW9kZWxvLnBhcmFtc1snc2Vzc29lcyddOi4xZn0iKQpwcmludChmIlLCsiA9IHttb2RlbG8ucnNxdWFyZWQ6LjNmfSIpCnByaW50KGYicCAocG9udG9zIHBvciBzZXNzw6NvKSA9IHttb2RlbG8ucHZhbHVlc1snc2Vzc29lcyddOi4zZn0iKQoKYjAgPSBtb2RlbG8ucGFyYW1zWydJbnRlcmNlcHQnXQpiMSA9IG1vZGVsby5wYXJhbXNbJ3Nlc3NvZXMnXQpkZi5wbG90LnNjYXR0ZXIoeD0nc2Vzc29lcycsIHk9J25vdGEnLCBjb2xvcj0nI2M3OTJlYScsCiAgICAgICAgICAgICAgICB0aXRsZT0nU2Vzc8O1ZXMgY29tIG8gY2hhdGJvdCDDlyBOb3RhJykKeHMgPSBbMiwgMTBdCnBsdC5wbG90KHhzLCBbYjAgKyBiMSAqIHYgZm9yIHYgaW4geHNdLCBjb2xvcj0nIzgyYWFmZicpCnBsdC54bGFiZWwoJ1Nlc3PDtWVzIGNvbSBvIGNoYXRib3QnKQpwbHQueWxhYmVsKCdOb3RhJykKcGx0LnNob3coKQo=" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false"></textarea>
  <pre class="code-output"></pre>
</div>

A saída esperada começa com ponto de partida = 40, pontos por sessão = 5, *R²* = 0,741 e *p* = 0,061. O gráfico deve mostrar os cinco pontos e a reta subindo.

---

## 🐍 Exemplo Python: várias informações

**Contexto:** a turma de 10 estudantes. O código imprime primeiro a régua só com as sessões, depois a conta com sessões, metacognição e letramento em IA, e por fim o VIF.

<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZAppbXBvcnQgc3RhdHNtb2RlbHMuZm9ybXVsYS5hcGkgYXMgc21mCmZyb20gc3RhdHNtb2RlbHMuc3RhdHMub3V0bGllcnNfaW5mbHVlbmNlIGltcG9ydCB2YXJpYW5jZV9pbmZsYXRpb25fZmFjdG9yCgpkZiA9IHBkLkRhdGFGcmFtZSh7CiAgICAnbm90YSc6ICAgICAgICAgIFs1NywgNjMsIDY0LCA2OCwgODEsIDc1LCA3OSwgODQsIDg4LCA4OF0sCiAgICAnc2Vzc29lcyc6ICAgICAgIFsyLCAzLCA0LCA1LCA2LCA3LCA4LCA5LCAxMCwgMTJdLAogICAgJ21ldGFjb2duaWNhbyc6ICBbNDgsIDcwLCA1NSwgNjIsIDgwLCA1OCwgNzQsIDY2LCA4NSwgNjBdLAogICAgJ2xldHJhbWVudG9faWEnOiBbMzAsIDQyLCAzOCwgNTUsIDQ4LCA3MCwgNDQsIDYwLCA1MiwgNzVdCn0pCgpzaW1wbGVzID0gc21mLm9scygnbm90YSB+IHNlc3NvZXMnLCBkYXRhPWRmKS5maXQoKQpwcmludChmIlPDsyBhcyBzZXNzw7Vlczoge3NpbXBsZXMucGFyYW1zWydzZXNzb2VzJ106LjJmfSBwb250b3MgcG9yIHNlc3PDo28iKQpwcmludChmIlLCsiBzw7MgY29tIHNlc3PDtWVzID0ge3NpbXBsZXMucnNxdWFyZWQ6LjNmfSIpCgptb2RlbG8gPSBzbWYub2xzKAogICAgJ25vdGEgfiBzZXNzb2VzICsgbWV0YWNvZ25pY2FvICsgbGV0cmFtZW50b19pYScsIGRhdGE9ZGYKKS5maXQoKQpwcmludCgpCnByaW50KCJDb20gYXMgdHLDqnMgaW5mb3JtYcOnw7VlcyBqdW50YXM6IikKcHJpbnQoZiJQb250byBkZSBwYXJ0aWRhID0ge21vZGVsby5wYXJhbXNbJ0ludGVyY2VwdCddOi4yZn0iKQpwcmludChmIlBvbnRvcyBwb3Igc2Vzc8OjbyA9IHttb2RlbG8ucGFyYW1zWydzZXNzb2VzJ106LjJmfSIpCnByaW50KGYiUG9udG9zIHBvciBwb250byBkZSBtZXRhY29nbmnDp8OjbyA9IHttb2RlbG8ucGFyYW1zWydtZXRhY29nbmljYW8nXTouMmZ9IikKcHJpbnQoZiJQb250b3MgcG9yIHBvbnRvIGRlIGxldHJhbWVudG8gZW0gSUEgPSB7bW9kZWxvLnBhcmFtc1snbGV0cmFtZW50b19pYSddOi4yZn0iKQpwcmludChmIlLCsiA9IHttb2RlbG8ucnNxdWFyZWQ6LjNmfSIpCnByaW50KCkKcHJpbnQobW9kZWxvLnN1bW1hcnkoKSkKClggPSBkZltbJ3Nlc3NvZXMnLCAnbWV0YWNvZ25pY2FvJywgJ2xldHJhbWVudG9faWEnXV0KdmlmID0gcGQuRGF0YUZyYW1lKHsKICAgICdpbmZvcm1hw6fDo28nOiBYLmNvbHVtbnMsCiAgICAnVklGJzogW3JvdW5kKHZhcmlhbmNlX2luZmxhdGlvbl9mYWN0b3IoWC52YWx1ZXMsIGkpLCAyKQogICAgICAgICAgICBmb3IgaSBpbiByYW5nZShYLnNoYXBlWzFdKV0KfSkKcHJpbnQoKQpwcmludCh2aWYpCg==" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável no navegador via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false"></textarea>
  <pre class="code-output"></pre>
</div>

Compare as duas linhas de "pontos por sessão": cerca de 3,29 sozinha, cerca de 2,67 quando metacognição e letramento em IA entram na conta. Essa diferença é a cena da metáfora, agora em número.

---

## 📚 Referências

| | |
|:--|:--|
| **referência** | Hair, J. F., et al. (2019). *Multivariate Data Analysis* (8ª ed.). Cap. 4. |
| **didático** | James, G., et al. (2023). *An Introduction to Statistical Learning* (2ª ed.). Cap. 3. |
| **VIF** | O'Brien, R. M. (2007). A caution regarding rules of thumb for VIF. *Quality & Quantity, 41*, 673–690. |
| **python** | McKinney, W. (2022). *Python for Data Analysis*. |

## 🌐 Referências · Recursos na Web

| | |
|:--|:--|
| **livro aberto** | James, G., Witten, D., Hastie, T., & Tibshirani, R. [An Introduction to Statistical Learning](https://www.statlearning.com/). Cap. 3, PDF gratuito. A reta, o *R²* e a regressão com várias informações. |
| **web (EN)** | [OpenStax, *Introductory Statistics 2e*: 12.3 The Regression Equation](https://openstax.org/books/introductory-statistics-2e/pages/12-3-the-regression-equation). A equação da reta e a leitura do gráfico, com exemplos de sala de aula. |
| **documentação** | Statsmodels. [`ols`](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.ols.html). A função usada nos exemplos em Python. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
