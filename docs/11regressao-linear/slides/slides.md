<!-- .slide: class="title-slide" -->

# Enc. 11

## Regressão Linear (simples e múltipla)

📈 Bloco 3 — Predição

<p class="small">Estimar a nota com uma reta · statsmodels.formula.api.ols()</p>

---

## 🎯 Que problema ela resolve

<p class="small">Se o estudante fizer mais uma sessão com o chatbot, quantos pontos a nota tende a subir? E que nota esperar de alguém que ainda não fez a prova?</p>

<center>nota esperada = ponto de partida + pontos por sessão × sessões</center>

<div class="destaque">
O que se estima é um número que muda aos poucos: a nota, os minutos, os acertos. Pearson só diz se duas coisas sobem juntas. A regressão escreve a regra em pontos.
</div>

--

<div class="destaque">
<strong>H₀:</strong> essa informação não muda a nota.<br>
<strong>H₁:</strong> essa informação acrescenta pontos na nota.
</div>

<p class="small">

- Uma informação só (as sessões): regressão linear simples.
- Várias ao mesmo tempo: regressão linear múltipla. Cada número é o acréscimo que sobra entre estudantes parecidos nas outras.
- "Engajou ou não" → regressão logística. "Quantas mensagens" → Poisson.

</p>

---

## 🍊 Metáfora

<p class="small">Uma professora quer estimar a nota antes da prova, olhando os logs do chatbot educacional.</p>

<p class="small">

- Cada estudante é um ponto: na horizontal, as sessões; na vertical, a nota.
- A régua é reta e não passa por todos. Sobra um vão na vertical entre a nota real e a nota que a régua marca.
- Ela inclina a régua até esses vãos ficarem os menores possíveis no conjunto.
- Dois números ficam: o ponto de partida (quem nunca abriu o chatbot) e quantos pontos cada sessão a mais vale.

</p>

--

<center><img src="../../imgs/regua-regressao.png" alt="Cinco estudantes, a reta da régua e o erro vertical de cada um" width="72%"></center>

<div class="destaque">
A reta é a régua: 40 + 5 × sessões. O tracejado chega ao ponto de partida, 40. Cada traço vertical é o vão daquele estudante.<br><br>
O vão de A vale 10. Os de B e D valem 5 cada. 10² = 100 e 5² + 5² = 50, então o vão grande pesa mais. Essa conta se chama mínimos quadrados.
</div>

--

## 🍊 E se outras coisas também pesam?

<p class="small">Quem abre o chatbot mais vezes também costuma refletir mais sobre o próprio estudo. A régua de uma informação só entrega ao chatbot pontos que em parte já vinham dessa reflexão.</p>

<div class="destaque">
A conta com várias informações faz outra pergunta: entre estudantes com a mesma metacognição e o mesmo letramento em IA, quantos pontos uma sessão a mais ainda acrescenta?
</div>

---

## 🧮 Fórmula

<p class="small">Sessões (x) e nota (y), cada estudante afastado da própria média.</p>

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.05em; margin:8px auto;">
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

<div class="destaque">
<em>R²</em> é a fatia da diferença entre as notas que a régua consegue acompanhar. Perto de 1, a régua acompanha quase tudo. Perto de 0, a nota se espalha por outros motivos.
</div>

---

## 🧩 Cinco estudantes, na mão

<p class="small">Sessões com o chatbot educacional e nota final. Médias: x̄ = 6 e ȳ = 70.</p>

| Est. | Sessões | Nota | Produto | (xᵢ−x̄)² |
|:-:|:-:|:-:|:-:|:-:|
| A | 2 | 60 | 40 | 16 |
| B | 4 | 55 | 30 | 4 |
| C | 6 | 60 | 0 | 0 |
| D | 8 | 75 | 10 | 4 |
| E | 10 | 100 | 120 | 16 |
| **Soma** | | | **200** | **40** |

<div class="destaque">
Pontos por sessão = 200 / 40 = <strong>5</strong>. Ponto de partida = 70 − 5 × 6 = <strong>40</strong>.<br>
Nota esperada = 40 + 5 × sessões. Alguém com 7 sessões: <strong>75</strong>.
</div>

--

## 🧩 O que a régua erra

| Est. | Nota real | Nota prevista | Erro |
|:-:|:-:|:-:|:-:|
| A | 60 | 50 | +10 |
| B | 55 | 60 | −5 |
| C | 60 | 70 | −10 |
| D | 75 | 80 | −5 |
| E | 100 | 90 | +10 |

<div class="destaque">
<em>R²</em> = 1 − 350/1350 ≈ <strong>0,74</strong>. Cerca de 74% da diferença entre as notas acompanha as sessões.<br><br>
Com 5 estudantes, <em>p</em> = 0,061. A reta é visível, e o grupo é pequeno demais para cravar que, numa turma maior, cada sessão acrescentaria pontos.
</div>

---

## 🔢 Como ler 40, 5 e 0,74

- **40**, o ponto de partida: a nota esperada se as sessões fossem zero. Ninguém aqui teve zero sessões, então o 40 é a régua prolongada.
- **5**, os pontos por sessão: cada sessão a mais acompanha cerca de 5 pontos na nota.
- **0,74**, o *R²*: cerca de 74% da diferença entre as notas acompanha a régua.

<div class="destaque">
A reta descreve o quanto a nota acompanha as sessões. Ela não mostra que o chatbot produziu a nota.
</div>

---

## 📐 Várias informações, 10 estudantes

<p class="small">A mesma pergunta, agora com sessões, metacognição e letramento em IA.</p>

<div class="destaque">
Só as sessões: cada sessão parece valer cerca de <strong>3,3 pontos</strong> (<em>R²</em> ≈ 0,90).<br><br>
Com as três juntas: cerca de <strong>2,7</strong> pontos por sessão, <strong>0,29</strong> por ponto de metacognição, e <strong>0,06</strong> por ponto de letramento em IA (<em>p</em> ≈ 0,58).
</div>

<p class="small">O 3,3 cai para 2,7 porque a reflexão sobre o próprio estudo deixa de ser atribuída ao chatbot. É o acréscimo que sobra entre estudantes parecidos nas outras duas informações.</p>

--

## 📐 O aviso do VIF

<p class="small">VIF acima de 5: duas informações sobem juntas demais para separar o papel de cada uma. O "quantos pontos" fica misturado.</p>

- Sessões: cerca de **3,5**
- Metacognição: cerca de **1,5**
- Letramento em IA: cerca de **2,9**

<div class="destaque">
Os três ficam abaixo de 5. Nesta turma, dá para ler o papel de cada informação em separado. O nome técnico da mistura, quando o VIF passa de 5, é multicolinearidade.
</div>

---

## 📋 Quando usar

- ✅ A resposta é um número que muda aos poucos: nota, minutos, acertos.
- ✅ No gráfico, os pontos acompanham uma reta.
- ✅ Os erros da régua têm tamanho parecido ao longo da reta. Eles não abrem um leque.

--

## 📋 Evite quando

- ❌ A resposta é "sim ou não" (engajou ou não) → regressão logística.
- ❌ A resposta é uma contagem, como quantas mensagens a pessoa enviou → Poisson.
- ❌ A nuvem faz uma curva, em vez de uma reta.
- ❌ O VIF passa de 5: as informações estão grudadas.
- ❌ Alguém quer concluir que o chatbot causou a nota.

---

## 🔍 Perguntas com chatbot educacional

- Mais sessões acompanham uma nota mais alta? Quantos pontos por sessão?
- Os minutos no chatbot estimam quantos exercícios a pessoa acerta?
- Entre estudantes com a mesma metacognição, uma sessão a mais ainda acrescenta pontos?
- O tamanho médio das mensagens estima a nota da atividade da semana?

---

## 📖 Como ler o resultado

- **5 estudantes:** 40 + 5 × sessões, *R²* = 0,74, *p* = 0,061.
- **10, só sessões:** cerca de 3,3 pontos por sessão, *R²* = 0,90.
- **10, três informações:** 2,7 por sessão (*p* = 0,001), 0,29 por ponto de metacognição (*p* = 0,016), 0,06 para letramento em IA (*p* = 0,58).

<div class="destaque">
Na tabela em inglês do <code>summary()</code>: <code>Intercept</code> é o ponto de partida, <code>coef</code> é quantos pontos, <code>P&gt;|t|</code> é o <em>p</em>, <code>R-squared</code> é o <em>R²</em>.
</div>

---

## 🐍 Exemplo Python

```python
modelo = smf.ols('nota ~ sessoes', data=df).fit()
print(f"Ponto de partida = {modelo.params['Intercept']:.1f}")
print(f"Pontos por sessão = {modelo.params['sessoes']:.1f}")
print(f"R² = {modelo.rsquared:.3f}")
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro. O primeiro desenha a reta dos 5 estudantes. O segundo compara a conta só com sessões e a conta com as três informações, e imprime o VIF.
</div>

---

## 📚 Referências

- **referência:** Hair et al. (2019). *Multivariate Data Analysis* (8ª ed.). Cap. 4.
- **didático:** James et al. (2023). *An Introduction to Statistical Learning* (2ª ed.). Cap. 3. PDF gratuito em [statlearning.com](https://www.statlearning.com/).
- **VIF:** O'Brien (2007). *Quality & Quantity, 41*, 673–690.
- **aula aberta:** [OpenStax, 12.3 The Regression Equation](https://openstax.org/books/introductory-statistics-2e/pages/12-3-the-regression-equation).

---

## 🔗 Materiais

[Conteúdo completo + código executável](../regressao-linear.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
