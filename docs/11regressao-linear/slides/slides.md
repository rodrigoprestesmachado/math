<!-- .slide: class="title-slide" -->

# Enc. 11

## Regressão Linear (simples e múltipla)

📈 Bloco 3 — Predição

<p class="small">Estimar a nota com uma reta · statsmodels.formula.api.ols()</p>

---

## 🍊 Metáfora

<p class="small">Uma professora quer saber, antes da prova, que nota esperar de cada estudante. A pista: o chatbot da disciplina registra quantas sessões cada estudante abriu.</p>

<p class="small">

- Ela olha uma turma do semestre anterior, que já fez a prova. Cada estudante vira um ponto: sessões na horizontal, nota na vertical.
- Os pontos sobem da esquerda para a direita. Ela apoia uma régua transparente sobre o gráfico.
- Entre cada ponto e a régua sobra uma distância vertical: o **vão**, o quanto a régua errou a nota daquele estudante.
- Ela inclina, sobe e desce a régua até os vãos, somados, ficarem os menores possíveis.
- A régua fica descrita por dois números: o **ponto de partida** (a nota para zero sessões) e os **pontos por sessão** (quanto ela sobe a cada sessão a mais).
- Na turma atual, que ainda não fez a prova, basta ler na régua a nota esperada.

</p>

<div class="destaque">
Essa régua é a <strong>regressão linear</strong>.
</div>

--

<center><img src="../../imgs/regua-regressao.png" alt="Cinco estudantes, a reta da régua e o vão vertical de cada um" width="62%"></center>

<p class="small">Turma fictícia de cinco estudantes, de A a E. Pontos roxos: estudantes. Linha azul: a régua. Traços laranja: os vãos.</p>

<div class="destaque">
A régua: <strong>nota esperada = 40 + 5 × sessões</strong>.<br>
A abriu 2 sessões: a régua marca 40 + 5 × 2 = 50 e A tirou 60, um vão de <strong>+10</strong>. C abriu 6: a régua marca 70 e C tirou 60, um vão de <strong>−10</strong>.<br>
O tracejado prolonga a régua até zero sessões (40). Ninguém tem zero sessões: o 40 é só a altura da régua.
</div>

--

## 🍊 Como somar os vãos?

<p class="small">Somados como estão, eles se cancelam: +10 − 5 − 10 − 5 + 10 = 0. Parece que a régua acertou todo mundo, mas ela não acertou a nota de ninguém.</p>

<div class="destaque">
<strong>Elevando cada vão ao quadrado</strong>, nada se cancela: 100 + 25 + 100 + 25 + 100 = <strong>350</strong>. A melhor régua deixa essa soma a menor possível. Daí o nome <strong>mínimos quadrados</strong>.<br><br>
O quadrado pesa mais os vãos grandes: um vão de 10 vira 100, e dois vãos de 5 viram 25 + 25 = 50. A régua evita deixar alguém muito longe dela.<br><br>
Em textos técnicos, o vão se chama <strong>resíduo</strong>: nota real − nota esperada.
</div>

--

## 🍊 Um passo além

<p class="small">Quem mais usa o chatbot também costuma ter mais <strong>metacognição</strong> (perceber o que já sabe e organizar o próprio estudo) e mais <strong>letramento em IA</strong> (saber usar ferramentas de IA). Parte dos pontos que a régua atribui às sessões pode vir dessas outras informações.</p>

<div class="destaque">
A pergunta muda. Em vez de "quantos pontos vale uma sessão a mais?":<br>
<strong>entre estudantes com a mesma metacognição e o mesmo letramento em IA, quantos pontos uma sessão a mais ainda acrescenta?</strong><br><br>
Com duas informações, a régua vira uma <strong>superfície</strong> (uma folha inclinada em 3D). Com três ou mais, a ideia é a mesma, mas o desenho não cabe no papel. É a <strong>regressão linear múltipla</strong>.
</div>

--

<center><img src="../../imgs/superficie-regressao.png" alt="A superfície no lugar da régua, e o corte com a metacognição parada em 66" width="88%"></center>

<p class="small">Outra turma, de 10 estudantes. <strong>À esquerda:</strong> a folha azul dá a nota esperada para cada combinação de sessões e metacognição; o letramento em IA fica fixo na média (51). A linha laranja fixa a metacognição em 66. <strong>À direita:</strong> a mesma linha de frente. De 6 para 7 sessões, a nota esperada sobe cerca de <strong>2,7 pontos</strong>.</p>

--

<iframe src="../plano-3d.html?tema=escuro" title="Superfície da regressão múltipla em 3D, com os 10 estudantes e os vãos" width="100%" height="700" style="border:none;"></iframe>

--

## 🍊 Régua × superfície

<p class="small">Se a metacognição fosse fixada em 50 ou 80, a linha laranja ficaria mais baixa ou mais alta, mas teria a <strong>mesma inclinação</strong>. Por isso um único número resume o papel das sessões.</p>

<div class="destaque">
Nessa turma de 10:<br>
• régua só com as sessões: cerca de <strong>3,3 pontos por sessão</strong>;<br>
• superfície (mesma metacognição e mesmo letramento em IA): cerca de <strong>2,7 pontos por sessão</strong>.<br><br>
A diferença, 3,3 − 2,7, é a parte que a régua simples atribuía às sessões, mas que se explica pela metacognição e, em menor parte, pelo letramento em IA.
</div>

---

## 🎯 Para que serve

<p class="small">Se um estudante fizer uma sessão a mais com o chatbot, quantos pontos a nota tende a subir? E que nota esperar de alguém que ainda não fez a prova?</p>

<center>nota esperada = ponto de partida + pontos por sessão × sessões</center>

<p class="small">

- **Ponto de partida:** a nota estimada para quem nunca abriu o chatbot (zero sessões).
- **Pontos por sessão:** quanto a nota esperada sobe a cada sessão a mais.

</p>

<div class="destaque">
Duas etapas:<br>
1. <strong>Ajustar</strong> a regra com estudantes que já têm sessões e nota.<br>
2. <strong>Usar</strong> a regra com quem ainda vai fazer a prova: o log mostra as sessões, e a regra dá a nota esperada.
</div>

--

## 🎯 Onde se encaixa no curso

<p class="small">

- **O que se estima:** um número numa escala (nota, minutos, acertos), o **desfecho numérico contínuo** (variável dependente). Cada informação usada para estimá-lo é um **preditor** (variável independente).
- **Correlação ou regressão:** Pearson (enc. 2) diz se duas coisas sobem juntas, e com que força. A regressão diz *quantos pontos* por sessão e estima a nota de quem ainda não está nos dados.
- **Simples ou múltipla:** uma informação só (sessões) é a simples. Várias ao mesmo tempo é a múltipla.
- **Outra resposta, outro método:** "engajou ou não" → regressão logística. "Quantas mensagens" → Poisson.

</p>

--

## 🎯 As hipóteses

<p class="small">Para cada informação colocada na regra, a regressão testa:</p>

<div class="destaque">
<strong>H₀:</strong> essa informação não ajuda a estimar a nota. Na população, os pontos que ela acrescenta são zero.<br>
<strong>H₁:</strong> essa informação ajuda a estimar a nota. Na população, os pontos são diferentes de zero, para mais ou para menos.
</div>

<p class="small">O teste devolve um <em>p</em> para cada informação: se H₀ fosse verdade, qual a chance de encontrar, só por acaso, um número tão longe de zero quanto o observado? Se <em>p</em> &lt; 0,05, rejeita-se H₀.</p>

--

## 🎯 Associação não é causa

<div class="destaque">
A regra descreve o que vem junto. <strong>Ela não prova causa.</strong><br><br>
Nestes dados, mais sessões vêm acompanhadas de notas mais altas. Mas um estudante que já domina o conteúdo pode abrir mais sessões e, ao mesmo tempo, tirar nota alta por causa do que já sabia.<br><br>
Para afirmar causa, é preciso outro desenho de pesquisa, como um experimento com grupos sorteados.
</div>

---

## 🧮 Fórmula

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
<strong>Lendo a fórmula:</strong> <em>xᵢ</em> = sessões do estudante <em>i</em>; <em>yᵢ</em> = nota dele.<br>
<em>x̄</em> e <em>ȳ</em> ("x barra", "y barra") = média das sessões e média das notas.<br>
<em>xᵢ − x̄</em> e <em>yᵢ − ȳ</em> = o quanto o estudante se afasta das médias.<br>
Σ (sigma) = "some o resultado de todos os estudantes".
</div>

--

## 🧮 Por que essa conta funciona?

<p class="small">Olhe o numerador, um estudante de cada vez:</p>

<p class="small">

- Mais sessões que a média **e** nota acima da média: positivo × positivo = **positivo**.
- Menos sessões que a média **e** nota abaixo da média: negativo × negativo = **positivo**.
- Acima numa coisa e abaixo na outra: produto **negativo**.

</p>

<p class="small">Soma positiva: a régua sobe. Negativa: a régua desce. O denominador mede o quanto as sessões variam e deixa o resultado em <strong>pontos de nota por sessão</strong>.</p>

<div class="destaque">
<strong>Ponto de partida:</strong> a melhor régua sempre passa pelo ponto médio da turma (x̄, ȳ). Na metáfora, ela passa por 6 sessões e nota 70. Voltando 6 sessões até o zero, desce 5 × 6 = 30 pontos: 70 − 30 = <strong>40</strong>.
</div>

--

## 🧮 R²: o quanto a régua ajuda a prever

<p class="small">Compare a régua inclinada com a régua mais simples possível: uma régua horizontal na nota média, que dá a mesma nota para todo mundo e ignora as sessões.</p>

<center>
<table style="border-collapse:collapse; font-family: Georgia, 'Times New Roman', serif; font-size:1.05em; margin:8px auto;">
<tr>
<td rowspan="2" style="padding-right:12px; vertical-align:middle;"><em>R²</em> = 1 −</td>
<td style="text-align:center; padding:2px 12px; border-bottom:2px solid currentColor;">Σ (vão de cada estudante)²</td>
</tr>
<tr>
<td style="text-align:center; padding:2px 12px;">Σ (yᵢ − ȳ)²</td>
</tr>
</table>
</center>

<p class="small">Em cima: vãos ao quadrado da régua inclinada. Embaixo: vãos ao quadrado da régua horizontal (distância de cada nota até a média).</p>

<div class="destaque">
<strong>Perto de 1:</strong> a régua inclinada acerta quase tudo o que a horizontal errava.<br>
<strong>Perto de 0:</strong> ela não é melhor do que dar a nota média para todo mundo.
</div>

---

## 🧩 Aplicação simples: a régua na mão

<p class="small"><strong>Passo 1. Médias.</strong> x̄ = (2 + 4 + 6 + 8 + 10) / 5 = <strong>6</strong> sessões. ȳ = (60 + 55 + 60 + 75 + 100) / 5 = <strong>70</strong> pontos.</p>

<p class="small"><strong>Passo 2. Afastamentos</strong> de cada estudante em relação às médias:</p>

<table style="font-size:0.9em; margin:8px auto;">
<tr><th>Est.</th><th>xᵢ</th><th>yᵢ</th><th>xᵢ − x̄</th><th>yᵢ − ȳ</th><th>(xᵢ−x̄)(yᵢ−ȳ)</th><th>(xᵢ−x̄)²</th><th>(yᵢ−ȳ)²</th></tr>
<tr><td>A</td><td>2</td><td>60</td><td>−4</td><td>−10</td><td>40</td><td>16</td><td>100</td></tr>
<tr><td>B</td><td>4</td><td>55</td><td>−2</td><td>−15</td><td>30</td><td>4</td><td>225</td></tr>
<tr><td>C</td><td>6</td><td>60</td><td>0</td><td>−10</td><td>0</td><td>0</td><td>100</td></tr>
<tr><td>D</td><td>8</td><td>75</td><td>2</td><td>5</td><td>10</td><td>4</td><td>25</td></tr>
<tr><td>E</td><td>10</td><td>100</td><td>4</td><td>30</td><td>120</td><td>16</td><td>900</td></tr>
<tr><td><strong>Soma</strong></td><td></td><td></td><td>0</td><td>0</td><td><strong>200</strong></td><td><strong>40</strong></td><td><strong>1350</strong></td></tr>
</table>

<p class="small">Lendo a linha de A: 2 − 6 = −4 sessões e 60 − 70 = −10 pontos. Os dois negativos dão produto positivo: (−4) × (−10) = 40.</p>

--

## 🧩 Passos 3 a 5: a regra

<div class="destaque">
<strong>Passo 3. Pontos por sessão</strong> = soma dos produtos / soma de (xᵢ−x̄)² = 200 / 40 = <strong>5</strong>.<br><br>
<strong>Passo 4. Ponto de partida</strong> = ȳ − 5 × x̄ = 70 − 5 × 6 = <strong>40</strong>.<br><br>
<strong>Passo 5. A regra:</strong> nota esperada = <strong>40 + 5 × sessões</strong>.
</div>

<p class="small">É exatamente a régua da metáfora.</p>

--

## 🧩 Passo 6: o vão de cada estudante

<p class="small">Vão = nota real − nota esperada.</p>

| Est. | Sessões | Nota real | Nota esperada | Vão |
|:-:|:-:|:-:|:-:|:-:|
| A | 2 | 60 | 40 + 5 × 2 = 50 | +10 |
| B | 4 | 55 | 40 + 5 × 4 = 60 | −5 |
| C | 6 | 60 | 40 + 5 × 6 = 70 | −10 |
| D | 8 | 75 | 40 + 5 × 8 = 80 | −5 |
| E | 10 | 100 | 40 + 5 × 10 = 90 | +10 |

--

## 🧩 Passo 7: o R²

<p class="small">

- Vãos ao quadrado da régua: 100 + 25 + 100 + 25 + 100 = **350**.
- Vãos ao quadrado da régua horizontal (nota 70 para todos): a última coluna do passo 2, **1350**.
- *R²* = 1 − 350 / 1350 = 1000 / 1350 ≈ **0,74**.

</p>

<div class="destaque">
A régua inclinada eliminou 1000 dos 1350, cerca de <strong>74%</strong>. Diz-se que as sessões "explicam" 74% da variação das notas. "Explicar" aqui quer dizer <strong>prever, não causar</strong>. Os outros 26% continuam nos vãos.
</div>

--

## 🧩 Um estudante novo

<p class="small">Um estudante da turma atual abriu 7 sessões e ainda não fez a prova.</p>

<div class="destaque">
Nota esperada = 40 + 5 × 7 = <strong>75</strong>.<br><br>
É uma estimativa, não uma garantia: assim como A, B, C, D e E, ele pode ficar acima ou abaixo da régua.
</div>

--

## 🧩 E o *p*?

<p class="small">O <em>p</em> exige uma conta mais longa, que o computador faz. Com 5 estudantes, o <em>p</em> dos pontos por sessão é <strong>0,061</strong>.</p>

<div class="destaque">
A régua sobe de forma clara e o <em>R²</em> é alto, mas cinco estudantes são poucos. Como 0,061 &gt; 0,05, <strong>não dá para rejeitar H₀</strong>: com tão poucos dados, uma inclinação assim ainda poderia aparecer por acaso, mesmo que, na população, as sessões não tivessem relação com a nota.
</div>

---

## 🔢 O que significam os números da régua

- **40**, o ponto de partida (*b₀*): a nota esperada para zero sessões. Ninguém teve zero sessões (o mínimo é 2): o 40 vem da régua prolongada.
- **5**, os pontos por sessão (*b₁*): a cada sessão a mais, a nota esperada sobe 5 pontos.
- **0,74**, o *R²*: a régua reduz em cerca de 74% os vãos ao quadrado, comparada a dar 70 para todo mundo.
- **0,061**, o *p*: acima de 0,05, cinco estudantes não bastam para generalizar a inclinação.

<div class="destaque">
O <strong>sinal</strong> dos pontos por sessão dá a direção: positivo, a régua sobe; negativo, desceria; zero, a régua fica horizontal e as sessões não ajudam a estimar a nota.
</div>

---

## 📐 Várias informações ao mesmo tempo

<p class="small">A turma da superfície: 10 estudantes fictícios, com <strong>metacognição</strong> e <strong>letramento em IA</strong> além das sessões.</p>

<table style="font-size:0.72em; margin:6px auto;">
<tr><th>Est.</th><th>Nota</th><th>Sessões</th><th>Metacognição</th><th>Letramento em IA</th></tr>
<tr><td>A</td><td>57</td><td>2</td><td>48</td><td>30</td></tr>
<tr><td>B</td><td>63</td><td>3</td><td>70</td><td>42</td></tr>
<tr><td>C</td><td>64</td><td>4</td><td>55</td><td>38</td></tr>
<tr><td>D</td><td>68</td><td>5</td><td>62</td><td>55</td></tr>
<tr><td>E</td><td>81</td><td>6</td><td>80</td><td>48</td></tr>
<tr><td>F</td><td>75</td><td>7</td><td>58</td><td>70</td></tr>
<tr><td>G</td><td>79</td><td>8</td><td>74</td><td>44</td></tr>
<tr><td>H</td><td>84</td><td>9</td><td>66</td><td>60</td></tr>
<tr><td>I</td><td>88</td><td>10</td><td>85</td><td>52</td></tr>
<tr><td>J</td><td>88</td><td>12</td><td>60</td><td>75</td></tr>
</table>

--

## 📐 Primeiro, só as sessões

<div class="destaque">
A régua só com as sessões dá cerca de <strong>3,3 pontos por sessão</strong>, com <em>R²</em> ≈ <strong>0,90</strong>.<br><br>
Mas essa conta não enxerga a metacognição nem o letramento em IA. E aqui quem abre mais sessões também tende a ter as duas mais altas. Parte desses 3,3 pontos pode pertencer, na verdade, às outras informações.
</div>

--

## 📐 Depois, as três juntas

<center>nota esperada ≈ 35 + 2,7 × sessões + 0,29 × metacognição + 0,06 × letramento em IA</center>

<p class="small">Cada número compara estudantes que diferem só naquela informação e são iguais nas outras duas.</p>

<p class="small">

- **Sessões: ≈ 2,7 pontos por sessão** (*p* = 0,001). É a inclinação da linha laranja. Caiu de 3,3 para 2,7 porque a conta separa o que acompanha as sessões do que acompanha as outras duas.
- **Metacognição: ≈ 0,29 ponto por ponto de escore** (*p* = 0,016). 10 pontos a mais de metacognição ≈ 2,9 pontos a mais na nota.
- **Letramento em IA: ≈ 0,06** (*p* = 0,58). Quase não muda a nota; o *p* alto indica que pode ser acaso.
- ***R²* ≈ 0,97.** Típico de exemplo de aula com dados inventados; numa turma real de 10, os números oscilariam bastante.

</p>

--

## 📐 Usando a regra

<p class="small">Um estudante com 7 sessões, metacognição 60 e letramento em IA 50:</p>

<div class="destaque">
35 + 2,7 × 7 + 0,29 × 60 + 0,06 × 50<br>
= 35 + 18,9 + 17,4 + 3,0 ≈ <strong>74</strong>
</div>

<p class="small">Em textos técnicos, o número de cada informação na regra se chama <strong>coeficiente</strong>.</p>

--

## 📐 VIF: as informações andam juntas demais?

<p class="small">Se todo estudante com muitas sessões também tivesse metacognição alta (e vice-versa), a conta não teria como saber qual das duas acompanha a nota. O <strong>VIF</strong> (fator de inflação da variância) mede esse problema, uma informação de cada vez.</p>

<p class="small">

- **VIF perto de 1:** a informação traz algo que as outras não trazem.
- **VIF acima de 5** (regra prática): ela se repete demais nas outras; o número dela fica instável.

</p>

<div class="destaque">
Nesta turma: sessões ≈ <strong>3,5</strong>, metacognição ≈ <strong>1,5</strong>, letramento em IA ≈ <strong>2,9</strong>. Todos abaixo de 5. O maior é o das sessões, que andam bastante junto com o letramento em IA.<br>
O excesso de sobreposição se chama <strong>multicolinearidade</strong>.
</div>

---

## 📋 Quando usar

- ✅ A resposta é um número numa escala: nota, minutos, acertos, um escore composto.
- ✅ No gráfico, a nuvem de pontos segue uma reta: cada sessão a mais vem com um acréscimo parecido, tanto de 2 para 3 quanto de 9 para 10.
- ✅ Os vãos têm tamanho parecido ao longo de toda a régua, sem se abrir em leque (**homocedasticidade**).

--

## 📋 Evite quando

<p class="small">

- ❌ A resposta é "sim ou não" (engajou ou não): **regressão logística**.
- ❌ A resposta é uma contagem, como quantas mensagens a pessoa enviou: **Poisson**. O que define o método é a *resposta*: as sessões também são contagem, mas aqui são a informação de entrada.
- ❌ A nuvem faz uma curva. Ex.: poucas mensagens = abandono, muitas = confusão, notas altas no meio. Uma régua reta passa por cima do arco.
- ❌ Duas informações andam juntas demais (VIF acima de 5).
- ❌ Você quer concluir que o chatbot *causou* a nota.

</p>

---

## 🔍 Perguntas de pesquisa em Informática na Educação

- Mais sessões com o chatbot vêm acompanhadas de nota final mais alta? Quantos pontos por sessão?
- O tempo total no chatbot ajuda a estimar quantos exercícios a pessoa acerta na semana?
- Entre estudantes com a mesma metacognição, uma sessão a mais ainda vem com pontos a mais?
- O tamanho médio das mensagens ajuda a estimar a nota da atividade da semana?

<div class="destaque">
<strong>Antes de ajustar a régua:</strong> confirme que a resposta é um número numa escala, faça o gráfico e veja se a nuvem segue uma reta.
</div>

---

## 🪜 Passo a passo na prática

<p class="small">

1. **Faça o gráfico** de sessões × nota. Reta, curva ou nenhum padrão?
2. **Ajuste a régua com uma informação só:** `nota ~ sessoes` (nota em função das sessões).
3. **Se outras informações também podem estar ligadas à nota,** coloque-as na mesma conta: `nota ~ sessoes + metacognicao + letramento_ia`.
4. **Confira o VIF.** Acima de 5, duas informações andam juntas demais para separar o papel de cada uma.
5. **Leia os pontos e o *p* de cada informação.** *p* < 0,05: um número tão longe de zero seria improvável se a informação não tivesse relação com a nota.
6. **Reporte** a regra, o *R²*, os *p*, o número de estudantes e o gráfico. Use linguagem de associação ("mais sessões vêm acompanhadas de notas mais altas"), não de causa.

</p>

---

## 📖 Como ler o resultado

- **5 estudantes:** 40 + 5 × sessões, *R²* = 0,74, *p* = 0,061. Descreve bem a turma, mas cinco pessoas não bastam para generalizar.
- **10, só sessões:** 3,29 pontos por sessão, *R²* = 0,90, *p* < 0,001.
- **10, três informações:** 2,67 por sessão (*p* = 0,001), 0,29 por ponto de metacognição (*p* = 0,016), 0,06 por ponto de letramento em IA (*p* = 0,58). *R²* = 0,97. VIF: 3,49, 1,45 e 2,93.

--

## 📖 Traduzindo o `summary()`

<p class="small">Leia primeiro as frases em português que o código imprime; depois, a tabela em inglês.</p>

<div class="destaque">
<code>Intercept</code> = ponto de partida<br>
<code>coef</code> = o número de cada informação (na linha <code>sessoes</code>, os pontos por sessão)<br>
<code>P&gt;|t|</code> = o <em>p</em> de cada informação<br>
<code>R-squared</code> = o <em>R²</em><br>
<code>No. Observations</code> = número de estudantes
</div>

<p class="small">O letramento em IA (<em>p</em> = 0,58) continua na conta: quase não muda a nota, mas, por estar nela, os pontos por sessão e por metacognição já descontam o papel dele.</p>

---

## 🐍 Exemplo Python: uma informação só

<p class="small">Os mesmos 5 estudantes da conta à mão.</p>

```python
modelo = smf.ols('nota ~ sessoes', data=df).fit()
print(f"Ponto de partida = {modelo.params['Intercept']:.1f}")
print(f"Pontos por sessão = {modelo.params['sessoes']:.1f}")
print(f"R² = {modelo.rsquared:.3f}")
print(f"p = {modelo.pvalues['sessoes']:.3f}")
```

<div class="destaque">
Saída esperada: ponto de partida = 40, pontos por sessão = 5, <em>R²</em> = 0,741, <em>p</em> = 0,061. Os mesmos valores da conta à mão.<br>
Código <strong>executável</strong> na página do encontro, com o gráfico da régua por cima dos pontos.
</div>

--

## 🐍 Exemplo Python: várias informações

<p class="small">A turma de 10. O código ajusta a régua só com as sessões, depois com as três informações (com o <code>summary()</code> completo), e calcula o VIF.</p>

```python
modelo = smf.ols(
    'nota ~ sessoes + metacognicao + letramento_ia', data=df
).fit()

X = sm.add_constant(df[['sessoes', 'metacognicao', 'letramento_ia']])
vif = [variance_inflation_factor(X.values, i)
       for i in range(1, X.shape[1])]
```

<div class="destaque">
Compare: ≈ 3,29 pontos por sessão sozinha, ≈ 2,67 com as outras duas. A mesma diferença entre a régua e a superfície.<br>
O <code>add_constant</code> faz o papel do ponto de partida; sem ele, o VIF sai inflado no navegador (acima de 12).
</div>

---

## 📚 Referências

- **referência:** Hair et al. (2019). *Multivariate Data Analysis* (8ª ed.). Cap. 4.
- **didático:** James et al. (2023). *An Introduction to Statistical Learning* (2ª ed.). Cap. 3. PDF gratuito em [statlearning.com](https://www.statlearning.com/).
- **VIF:** O'Brien (2007). A caution regarding rules of thumb for VIF. *Quality & Quantity, 41*, 673–690.
- **python:** McKinney (2022). *Python for Data Analysis*.
- **web (EN):** [OpenStax, 12.3 The Regression Equation](https://openstax.org/books/introductory-statistics-2e/pages/12-3-the-regression-equation).
- **documentação:** [statsmodels `ols`](https://www.statsmodels.org/stable/generated/statsmodels.formula.api.ols.html).

---

## 🔗 Materiais

[Conteúdo completo + código executável](../regressao-linear.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
