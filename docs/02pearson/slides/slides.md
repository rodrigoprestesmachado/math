<!-- .slide: class="title-slide" -->

# Enc. 2

## Correlação de Pearson

🔗 Bloco 1 — Associação

<p class="small">scipy.stats.pearsonr · pandas DataFrame.corr(method='pearson')</p>

---

## 🍊 Metáfora

<p class="small">Pense em dois atletas correndo numa pista lado a lado.</p>

<p class="small">

- Quando um acelera, o outro acelera na mesma proporção; quando desacelera, o outro acompanha → **r = +1**.
- Quando um acelera e o outro desacelera na mesma medida → **r = −1**.
- Quando cada um faz o que quer, independentemente do outro → **r ≈ 0**.
- Pearson mede essa sincronia, mas *apenas quando a pista é reta*.

</p>

---

## 📈 O que é uma "pista reta"?

- Ao plotar X × Y num scatter plot, os pontos formam uma **reta**: cada aumento de X gera um acréscimo **constante** em Y.
- Pearson mede o quanto os pontos se aproximam dessa reta.

--

<div class="destaque">

- Imagine agora que os dois atletas correm num trecho <strong>plano</strong>, lado a lado, em perfeita sincronia — A pista encontra uma <strong>colina</strong>. Na subida, um deles tem mais força e mantém o ritmo; o outro cansa e desacelera, e a sincronia que existia no plano se desfaz.
- Resultado: o padrão muda de comportamento ao longo do percurso (uma reta, depois uma subida), ou seja, não existe uma única reta que descreva bem todo o trajeto. Dependendo do tamanho da subida em relação ao trecho plano, <em>r</em> pode cair bastante, chegando perto de 0 mesmo havendo um padrão bem claro no gráfico.

</div>

<p class="small">Por isso: sempre olhe o scatter plot antes de confiar no valor de <em>r</em>.</p>

---

## 💬 Exemplo em dados conversacionais

Cruzamos duas fontes por estudante: o número de **mensagens trocadas** no chat, extraído dos logs de um chatbot baseado em LLM, e o **escore composto em uma escala de metacognição** (ex.: Metacognitive Awareness Inventory), aplicada separadamente como questionário.

- **Pergunta:** estudantes que trocam mais mensagens têm maior consciência metacognitiva?
- **X:** número de mensagens · **Y:** escore composto no MAI.
- Antes de calcular *r*, plote um scatter plot (cada estudante vira um ponto no gráfico) e observe: os pontos sobem formando algo parecido com uma reta?

<div class="destaque">
Outras variáveis conversacionais que também podem ser correlacionadas: tempo ativo no chat × nota final, número de mensagens × acertos em exercícios, latência média de resposta × duração da sessão.
</div>

---

## 🎯 Para que serve

Mede a **força** e a **direção** de uma relação *linear* entre duas variáveis numéricas contínuas. O coeficiente *r* vai de −1 a +1.

Em dados conversacionais: *quanto mais mensagens um estudante troca com o chatbot, maior o seu escore numa escala de metacognição?*

---

## 🧮 Fórmula

<p class="small">Como os atletas da metáfora: cada um se afasta da própria média, e <em>r</em> mede se isso acontece junto.</p>

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.3em; margin:8px auto;">
<tr>
<td rowspan="2" style="padding-right:12px; vertical-align:middle;"><em>r</em> =</td>
<td style="text-align:center; padding:2px 12px; border-bottom:2px solid currentColor;">Σ (xᵢ − x̄)(yᵢ − ȳ)</td>
</tr>
<tr>
<td style="text-align:center; padding:2px 12px;">√[ Σ(xᵢ − x̄)² × Σ(yᵢ − ȳ)² ]</td>
</tr>
</table>
</center>

<div class="destaque">
<em>xᵢ, yᵢ</em>: valores de X e Y de cada estudante · <em>x̄, ȳ</em>: médias de X e de Y · Σ: soma para todos os estudantes · √: raiz quadrada.<br><br>
O numerador soma o produto dos desvios (o quanto X e Y "andam juntos"); o denominador normaliza esse valor pela dispersão de cada variável — por isso <em>r</em> fica sempre entre −1 e +1.
</div>

--

## 🪜 Passo a passo do cálculo

<p class="small">Como chegar de X e Y até o valor de <em>r</em>:</p>

1. Calcule as médias x̄ e ȳ.
2. Para cada estudante, calcule os desvios (xᵢ−x̄) e (yᵢ−ȳ).
3. Multiplique os dois desvios e some tudo → **numerador**.
4. Some os desvios² de cada variável, multiplique os totais e tire a raiz → **denominador**.
5. **r** = numerador / denominador.

--

## 🧩 Aplicação simples: r na mão

<p class="small">Aplicando os passos acima a 5 estudantes fictícios · X = mensagens trocadas · Y = escore no MAI</p>

| Est. | xᵢ | yᵢ | xᵢ−x̄ | yᵢ−ȳ | produto |
|:-:|:-:|:-:|:-:|:-:|:-:|
| A | 2 | 40 | −4 | −20 | 80 |
| B | 4 | 50 | −2 | −10 | 20 |
| C | 6 | 70 | 0 | 10 | 0 |
| D | 8 | 60 | 2 | 0 | 0 |
| E | 10 | 80 | 4 | 20 | 80 |

<div class="destaque">
x̄ = 6 · ȳ = 60 · Σ produto = 180 · Σ(xᵢ−x̄)² = 40 · Σ(yᵢ−ȳ)² = 1000<br><br>
<em>r</em> = 180 / √(40 × 1000) = 180 / 200 = <strong>0,90</strong> → correlação positiva forte: quem trocou mais mensagens tendeu a ter maior escore no MAI.
</div>

---

## 📋 Quando usar

- ✅ Ambas as variáveis são contínuas e numéricas.
- ✅ A relação esperada é <strong>linear</strong> e os pontos, ao serem plotados, tendem a formar uma reta (não uma curva). Confira sempre com um scatter plot antes de calcular.
- ✅ Cada variável, isoladamente, deve seguir uma <strong>distribuição normal</strong>: a maioria dos estudantes envia um número "médio" de mensagens, e cada vez menos estudantes enviam quantidades bem abaixo ou bem acima dessa média. O teste de <strong>Shapiro-Wilk</strong> verifica isso.
- ❌ Não usar com dados <strong>ordinais</strong>, como uma escala Likert de 1 (discordo totalmente) a 5 (concordo totalmente). Nesses casos, use Spearman.

--

<div class="destaque">
Os números de 1 a 5 indicam apenas <strong>ordem</strong> (5 é mais concordância que 4), não uma régua com espaçamento igual entre eles. Pearson, porém, calcula a distância matemática entre os números como se 5 − 4 valesse exatamente o mesmo que 2 − 1.<br><br>
O problema: para uma pessoa, sair de "discordo" (2) para "neutro" (3) pode ser um salto de opinião muito maior do que sair de "concordo" (4) para "concordo totalmente" (5), mas, Pearson trataria os dois saltos como idênticos (ambos valem 1). Nesse caso, podemos usar <strong>Spearman</strong>, que veremos nas próximas seções.
</div>

---



## 🐍 Exemplo Python

<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZApmcm9tIHNjaXB5IGltcG9ydCBzdGF0cwppbXBvcnQgbWF0cGxvdGxpYi5weXBsb3QgYXMgcGx0CgpkZiA9IHBkLkRhdGFGcmFtZSh7CiAgICAnbWVuc2FnZW5zJzogWzQsNywzLDksNSwxMSw2LDgsMiwxMF0sCiAgICAnbWFpX3Njb3JlJzogWzUyLDcxLDQ4LDgwLDYwLDg1LDY2LDc1LDQwLDgyXQp9KQoKIyBQYXNzbyAxOiBzZW1wcmUgdmlzdWFsaXplIGFudGVzCmRmLnBsb3Quc2NhdHRlcih4PSdtZW5zYWdlbnMnLCB5PSdtYWlfc2NvcmUnLCBjb2xvcj0nI2M3OTJlYScsCiAgICAgICAgICAgICAgIHRpdGxlPSdNZW5zYWdlbnMgw5cgRXNjb3JlIGNvbXBvc3RvIG5vIE1BSScpCnBsdC5zaG93KCkKCiMgUGFzc28gMjogY2FsY3VsYXIKciwgcCA9IHN0YXRzLnBlYXJzb25yKGRmWydtZW5zYWdlbnMnXSwgZGZbJ21haV9zY29yZSddKQpwcmludChmInIgPSB7cjouM2Z9LCBwID0ge3A6LjRmfSIp" markdown="0">
  <div class="runner-toolbar">
    <span class="runner-label">🐍 Python executável via <a href="https://pyodide.org" target="_blank">Pyodide</a></span>
    <button type="button" class="run-btn">▶ Executar</button>
  </div>
  <textarea class="code-input" spellcheck="false"></textarea>
  <pre class="code-output"></pre>
</div>

---

## 📚 Referências

- **clássico:** Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Lawrence Erlbaum.
- **didático:** Field, A. (2024). *Discovering Statistics Using IBM SPSS Statistics* (6ª ed.). SAGE. Cap. 8.
- **python:** McKinney, W. (2022). *Python for Data Analysis* (3ª ed.). O'Reilly. Cap. 13.

---

## 🔗 Materiais

[Conteúdo completo + código executável](../pearson.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
