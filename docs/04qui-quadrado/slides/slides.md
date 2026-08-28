<!-- .slide: class="title-slide" -->

# Enc. 4

## Qui-quadrado e V de Cramér

🔗 Bloco 1: Associação

<p class="small">scipy.stats.chi2_contingency · cálculo manual de V</p>

---

## 🍊 Metáfora

<p class="small">Um professor de programação separa os estudantes conforme o quanto usam o chatbot (pouco, médio, muito) e classifica as perguntas em três tipos (conceitual, depuração, trecho de código).</p>

<p class="small">

- Se o quanto o estudante usa o chatbot não influenciasse o tipo de pergunta, esperaríamos a mesma proporção de tipos em cada grupo.
- O qui-quadrado (χ²) compara essa distribuição **esperada** (sem relação) com o que foi **observado** de fato nos registros de conversa.
- Quanto maior a diferença, maior o χ², e mais evidência de associação.

</p>

--

<div class="destaque">
O χ² cresce junto com o tamanho da amostra: com muitas observações, até uma associação fraca pode gerar um χ² grande e um <em>p</em> pequeno. Por isso χ² responde <strong>existe associação?</strong> (significância), e o <strong>V de Cramér</strong> responde <strong>quão forte é?</strong> (tamanho do efeito).
</div>

---

## 🎯 Para que serve

Testa se duas variáveis **categóricas nominais** são **independentes**, organizadas numa **tabela de contingência**: linhas e colunas são categorias, cada célula conta quantos estudantes caem naquela combinação.

Exemplo: *o tipo de pergunta ao chatbot varia conforme o quanto o estudante usa a ferramenta?*

<div class="destaque">
<strong>H₀:</strong> as duas variáveis são independentes (não há associação na população).<br>
<strong>H₁:</strong> as duas variáveis são associadas.
</div>

---

# 📐 Qui-quadrado (χ²)

## 🧮 Fórmula

<p class="small">Soma, célula a célula, o quanto o observado se afasta do esperado sob independência.</p>

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

<div class="destaque">
<em>Oᵢ</em>: frequência observada em cada célula · <em>Eᵢ</em>: frequência esperada sob independência, calculada por (total da linha × total da coluna) / n.
</div>

--

## 🪜 Passo a passo do cálculo

1. Monte a tabela de contingência com as frequências **observadas**.
2. Calcule os totais de linha, de coluna, e o total geral (n).
3. Para cada célula: E = (total da linha × total da coluna) / n.
4. Para cada célula: (O − E)² / E.
5. Some tudo → **χ²**.

--

## 🧩 Aplicação simples: χ² na mão

<p class="small">40 estudantes fictícios · nível (iniciante/avançado) × tipo de pergunta (conceitual/depuração)</p>

| | Conceitual (O) | Depuração (O) | Total |
|:--|:-:|:-:|:-:|
| **Iniciante** | 15 | 5 | 20 |
| **Avançado** | 5 | 15 | 20 |
| **Total** | 20 | 20 | **n = 40** |

<div class="destaque">
Todas as células esperam E = (20 × 20) / 40 = 10.<br><br>
(O − E)²/E = 2,5 em cada célula → <em>χ²</em> = 2,5 × 4 = <strong>10,00</strong> (gl = 1) → suficiente para rejeitar H₀.
</div>

--

## 🎥 Sugestão de vídeo

[Vídeo sugerido sobre qui-quadrado](https://www.youtube.com/watch?v=4QfHVbpAoSg)

---

# 📐 V de Cramér

## 🧮 Fórmula

<p class="small">χ² sozinho não diz o quão forte é a associação; V reescala pelo tamanho da amostra.</p>

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

<div class="destaque">
<em>k</em> = menor entre (linhas − 1) e (colunas − 1). Aplicando ao exemplo acima: k = 1 → <em>V</em> = √(10 / 40) = <strong>0,50</strong> → associação grande.
</div>

---

## 🔢 O que significa V?

| Valor de V | Força |
|:-----------|:------|
| **≈ 0,10** | pequena |
| **≈ 0,30** | média |
| **≈ 0,50** | grande |

<div class="destaque">
<strong>Convenção de Cohen (1988).</strong> Sozinho, <em>p</em> &lt; .05 indica que a associação existe; V mostra se ela é relevante na prática.
</div>

---

## 📋 Quando usar

- ✅ Ambas as variáveis são <strong>categóricas nominais</strong>.
- ✅ Observações **independentes**: cada estudante conta uma única vez.
- ✅ Frequência esperada ≥ 5 em pelo menos 80% das células.
- ❌ Não use com variáveis ordinais; Spearman é mais adequado.
- ❌ Nunca interprete apenas o p-valor: sempre reporte V de Cramér.

--

## 📋 Exemplos em learning analytics

- Tipo de pergunta × quanto o estudante usa o chatbot.
- Turno de uso × modalidade da disciplina.
- Categoria de erro mais comum × turma.
- Uso de um recurso opcional (sim/não) × aprovação (sim/não).

---

# 💬 Pesquisa em Informática na Educação

## 🔍 Perguntas de pesquisa: conversas estudante-chatbot

<p class="small">Cada pergunta abaixo cruza duas variáveis categóricas extraídas de logs de conversa — exatamente o formato de tabela de contingência que χ² e V de Cramér exigem.</p>

- A **intenção da mensagem** (pedir explicação, pedir código pronto, pedir depuração) está associada à **disciplina** (Programação I, Estruturas de Dados, Banco de Dados)?
- O **nível de dependência do chatbot** (baixo/médio/alto, medido pela frequência de uso) está associado ao **desempenho final** (aprovado/reprovado)?
- O **tom da interação** (cordial, neutro, frustrado) varia conforme o **momento do semestre** (início, meio, período de provas)?

--

## 🔍 Mais perguntas de pesquisa

- Estudantes que **colam o código de erro literal** vs. os que **descrevem o problema com as próprias palavras** diferem quanto ao **curso/turma**?
- A **categoria da primeira pergunta numa sessão** (conceito, sintaxe, lógica do algoritmo) está associada ao **período do curso** (iniciante/intermediário/avançado)?
- O uso de **linguagem informal ou emojis** nas mensagens está associado à **faixa etária** ou ao **gênero** dos estudantes?
- A **aceitação da resposta do chatbot sem questionar** (sim/não) está associada ao **tipo de pergunta feita** (conceitual/depuração/trecho de código)?

<div class="destaque">
Em todos os casos: <strong>H₀</strong> = as duas variáveis são independentes na população de estudantes; <strong>H₁</strong> = existe associação. χ² diz se a associação é estatisticamente detectável; V de Cramér diz se ela é grande o suficiente para importar pedagogicamente.
</div>

--

## 🧩 Do dado bruto à tabela de contingência

<p class="small">Exemplo de fluxo de análise para "intenção da mensagem × disciplina":</p>

1. **Coletar** os logs de conversa (mensagem do estudante + metadados: disciplina, turma, timestamp).
2. **Codificar** cada mensagem numa categoria de intenção (manual, por rubrica, ou com apoio de um classificador).
3. **Cruzar** intenção × disciplina numa tabela de contingência (contagem de mensagens em cada célula).
4. **Testar** com `chi2_contingency` e calcular V de Cramér.
5. **Interpretar** à luz da prática: professores de disciplinas diferentes precisam ajustar como orientam o uso do chatbot?

---

## 📐 Teste exato de Fisher

<p class="small">Alternativa ao χ² quando as frequências esperadas são baixas, comum em tabelas 2×2 pequenas.</p>

<div class="destaque">
<strong>H₀:</strong> as duas variáveis são independentes.<br>
<strong>H₁:</strong> as duas variáveis são associadas.
</div>

- **Frequência esperada ≥ 5 em ≥ 80% das células** → o χ² é uma boa aproximação.
- **Alguma célula com frequência esperada &lt; 5**, sobretudo em 2×2 → prefira `stats.fisher_exact`.

<p class="small">Fisher é exato em qualquer tamanho de amostra, mas fica caro em tabelas grandes; por isso é reservado para os casos em que o χ² não é confiável.</p>

---

## 🪜 Passo a passo na prática

1. **Visualize:** monte a tabela de contingência.
2. **Verifique pressupostos:** independência das observações e frequência esperada suficiente (ou use Fisher).
3. **Calcule:** `chi2_contingency(tabela)` para χ² e *p*, depois V a partir do χ².
4. **Interprete:** leia *p* (significância) e V (força), nunca apenas um dos dois.
5. **Reporte:** χ², gl, *p*, *n*, V e a tabela de contingência.

---

## 📖 Como ler o resultado

<p class="small">Suponha χ² = 18.203, gl = 4, p = 0.0011, V = 0.301, com n = 138 estudantes:</p>

- **χ² = 18,203, p = 0,0011** → rejeitamos H₀: é pouco provável essa tabela sob independência.
- **V = 0,301** → efeito <strong>médio a grande</strong>: a associação existe e tem magnitude relevante.
- O tipo de pergunta varia de forma perceptível conforme o quanto o estudante usa o chatbot.

<div class="destaque">
<strong>Associação ≠ causalidade.</strong> Um uso mais intenso do chatbot pode levar a perguntas mais elaboradas, ou o contrário: estudantes que já perguntam melhor podem se engajar mais.
</div>

---

## 🐍 Exemplo Python: Qui-quadrado e V de Cramér

```python
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

# Passo 1: montar a tabela de contingencia
tabela = pd.DataFrame(
    [[30,15,10],[20,25,18],[10,20,35]],
    index   = ['conceitual','depuração','trecho de código'],
    columns = ['pouco','médio','muito']
)
print(tabela, "\n")

# Passo 2: calcular qui-quadrado, p-valor, graus de liberdade e esperadas
chi2, p, gl, esperadas = chi2_contingency(tabela)
print(f"χ² = {chi2:.3f}  gl = {gl}  p = {p:.4f}")

# Passo 3: calcular V de Cramer a partir do mesmo qui-quadrado
n = tabela.values.sum()
k = min(tabela.shape) - 1
V = np.sqrt(chi2 / (n * k))
efeito = 'pequeno' if V < .3 else 'médio' if V < .5 else 'grande'
print(f"V de Cramér = {V:.3f}  → efeito {efeito}")
```

<div class="destaque">
Código <strong>executável</strong> na página do encontro, clique em <strong>▶ Executar</strong>.
</div>

---

## 📚 Referências · Biblioteca Digital IFRS

<p class="small">Disponíveis para consulta/e-book em <a href="https://ifrs.pergamum.com.br" target="_blank">ifrs.pergamum.com.br</a></p>

- Giolo, S. R. (2017). *Introdução à análise de dados categóricos com aplicações*. São Paulo: Blucher. [e-book]
- Martinez, E. Z. (2023). *Bioestatística para os cursos de graduação da área da saúde* (2ª ed.). São Paulo: Blucher. [e-book]
- Costa, G. G. de O. (2012). *Curso de Estatística inferencial e probabilidades: teoria e prática*. Rio de Janeiro: Atlas. [e-book]
- Balbino, F. O. & Rosa, J. M. C. da. (2023). *Análise de dados categorizados e longitudinais*. Curitiba: InterSaberes. [e-book]

--

## 🌐 Referências · Recursos na Web

- Tesify. (2026). [Teste Qui-Quadrado no SPSS: Guia Completo e APA 7](https://tesify.pt/teste-qui-quadrado-spss-2026-quando-usar-passo-a-passo-apa7/).
- Estatística Fácil. [Tamanho de Efeito Para Qui-Quadrado (V de Cramér e Phi)](https://estatisticafacil.org/tamanho-de-efeito-para-qui-quadrado/).
- Estatística Fácil. [O que é: Coeficiente de Cramer - Entenda sua Importância](https://estatisticafacil.org/glossario/o-que-e-coeficiente-de-cramer-importancia/).
- [Vídeo sugerido sobre qui-quadrado](https://www.youtube.com/watch?v=4QfHVbpAoSg).

<div class="destaque">
Busque outros títulos por "qui-quadrado", "dados categóricos" ou "estatística aplicada" no catálogo do IFRS — vários têm capítulo dedicado a χ² e medidas de associação, incluindo dissertações do próprio Mestrado em Informática na Educação.
</div>

---

## 🔗 Materiais

[Conteúdo completo + código executável](../qui-quadrado.html)

[math.rpmhub.dev](https://math.rpmhub.dev)
