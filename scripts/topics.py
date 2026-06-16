# Dados dos encontros — Análise de Dados Conversacionais

BLOCOS = {
    1: {"id": "bloco1", "emoji": "🔗", "name": "Associação", "range": "Enc. 2–5", "class": "b1"},
    2: {"id": "bloco2", "emoji": "⚖️", "name": "Comparação", "range": "Enc. 6–10", "class": "b2"},
    3: {"id": "bloco3", "emoji": "📈", "name": "Predição", "range": "Enc. 11–13", "class": "b3"},
}

TOPICS = [
    {
        "dir": "02pearson",
        "num": 2,
        "nav_order": 4,
        "bloco": 1,
        "title": "Correlação de Pearson",
        "subtitle": "scipy.stats.pearsonr · pandas DataFrame.corr(method='pearson')",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Pense em dois atletas correndo numa pista lado a lado. Quando um acelera, o outro também '
            'acelera na mesma proporção; quando um desacelera, o outro acompanha. Isso é <strong>r = +1</strong>: '
            'movem-se em perfeita sincronia na mesma direção. Se um acelera e o outro desacelera exatamente na '
            'mesma medida, temos <strong>r = −1</strong>. Se cada um faz o que quer, independentemente do outro, '
            '<strong>r ≈ 0</strong>. Pearson mede essa sincronia — mas <em>apenas quando a pista é reta</em>.'
        ),
        "serve": [
            'Mede a <strong>força</strong> e a <strong>direção</strong> de uma relação <em>linear</em> entre duas variáveis numéricas contínuas. O coeficiente <em>r</em> vai de −1 a +1.',
            'Em dados conversacionais: <em>quanto maior o número de turnos em uma sessão, maior o escore de compreensão do estudante?</em>',
        ],
        "quando": [
            '✅ Ambas as variáveis são contínuas e numéricas.',
            '✅ A relação esperada é <strong>linear</strong> — verificar com scatter plot antes de calcular.',
            '✅ Cada variável segue aproximadamente distribuição normal (Shapiro-Wilk).',
            '❌ Não usar com dados ordinais (Likert) — use Spearman.',
            '❌ Não usar se houver outliers extremos — eles puxam r para si sozinhos.',
            '❌ Correlação não implica causalidade.',
        ],
        "tip": '<strong>Convenção de Cohen (1988):</strong> |r| &lt; 0.10 negligível · 0.10–0.29 pequeno · 0.30–0.49 médio · ≥ 0.50 grande',
        "python_context": 'Contexto: verificar se o número de turnos por sessão se associa ao escore de compreensão.',
        "python_code": '''import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'turnos':      [4,7,3,9,5,11,6,8,2,10],
    'escore_comp': [52,71,48,80,60,85,66,75,40,82]
})

# Passo 1: sempre visualize antes
df.plot.scatter(x='turnos', y='escore_comp', color='#c792ea',
               title='Turnos × Escore de Compreensão')
plt.show()

# Passo 2: calcular
r, p = stats.pearsonr(df['turnos'], df['escore_comp'])
print(f"r = {r:.3f}, p = {p:.4f}")''',
        "refs": [
            ("clássico", 'Cohen, J. (1988). <em>Statistical Power Analysis for the Behavioral Sciences</em> (2ª ed.). Lawrence Erlbaum.'),
            ("didático", 'Field, A. (2024). <em>Discovering Statistics Using IBM SPSS Statistics</em> (6ª ed.). SAGE. Cap. 8.'),
            ("python", "McKinney, W. (2022). <em>Python for Data Analysis</em> (3ª ed.). O'Reilly. Cap. 13."),
            ("artigo", 'Mukaka, M. M. (2012). A guide to appropriate use of correlation coefficient in medical research. <em>Malawi Medical Journal, 24</em>(3), 69–71.'),
        ],
    },
    {
        "dir": "03spearman",
        "num": 3,
        "nav_order": 5,
        "bloco": 1,
        "title": "Correlação de Spearman e Kendall",
        "subtitle": "scipy.stats.spearmanr · scipy.stats.kendalltau · pingouin.corr()",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Em vez de medir a velocidade exata de cada atleta, você registra a <strong>posição deles na corrida</strong>: '
            '1º, 2º, 3º… Spearman e Kendall trocam os valores originais pelos seus <em>postos</em> (rankings). '
            '<strong>Kendall</strong> é mais conservador: conta quantos pares estão na ordem certa versus errada — '
            'útil quando há muitos empates.'
        ),
        "serve": [
            'Alternativas <strong>não-paramétricas</strong> a Pearson. Medem relações <em>monotônicas</em>. Ideais para dados ordinais como escalas Likert.',
            'Exemplo: <em>a satisfação do estudante com o chatbot (escala 1–5) está associada à quantidade de sessões voluntárias?</em>',
        ],
        "quando": [
            '✅ Uma ou ambas as variáveis são <strong>ordinais</strong> (Likert).',
            '✅ Os dados violam normalidade (Shapiro-Wilk: p &lt; .05).',
            '✅ Há outliers que não devem ser removidos.',
            '✅ Use <strong>Kendall</strong> com n &lt; 30 ou muitos empates.',
            '❌ Não diferencia relações lineares de curvilíneas — só detecta monotonicidade.',
        ],
        "python_code": '''import pandas as pd
from scipy import stats
import pingouin as pg

df = pd.DataFrame({
    'satisfacao': [2,4,1,5,3,5,4,2,3,5],
    'sessoes':    [3,8,1,12,5,11,9,2,4,13]
})

rho, p_s = stats.spearmanr(df['satisfacao'], df['sessoes'])
print(f"Spearman ρ = {rho:.3f}, p = {p_s:.4f}")

tau, p_k = stats.kendalltau(df['satisfacao'], df['sessoes'])
print(f"Kendall  τ = {tau:.3f}, p = {p_k:.4f}")

res = pg.corr(df['satisfacao'], df['sessoes'], method='spearman')
print(res[['n', 'r', 'CI95%', 'p-val', 'power']])''',
        "refs": [
            ("seminal", 'Spearman, C. (1904). The proof and measurement of association between two things. <em>American Journal of Psychology, 15</em>(1), 72–101.'),
            ("didático", 'Field, A. (2024). <em>Discovering Statistics Using IBM SPSS Statistics</em> (6ª ed.). SAGE. Cap. 8.'),
            ("python", 'Vallat, R. (2018). Pingouin: statistics in Python. <em>Journal of Open Source Software, 3</em>(31), 1026.'),
            ("aplicado", 'Norman, G. (2010). Likert scales, levels of measurement and the "laws" of statistics. <em>Advances in Health Sciences Education, 15</em>, 625–632.'),
        ],
    },
    {
        "dir": "04qui-quadrado",
        "num": 4,
        "nav_order": 6,
        "bloco": 1,
        "title": "Qui-quadrado e V de Cramér",
        "subtitle": "scipy.stats.chi2_contingency · cálculo manual de V",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Imagine um cardápio com três pratos (factual, conceitual, procedimental) e três tipos de clientes. '
            'O qui-quadrado compara o <em>observado</em> com o <em>esperado</em> se não houvesse relação. '
            'O <strong>V de Cramér</strong> quantifica a força dessa associação, livre do tamanho amostral.'
        ),
        "serve": [
            'Testa se duas variáveis <strong>categóricas</strong> são independentes. O <strong>p-valor do χ²</strong> indica significância; o <strong>V de Cramér</strong> quantifica a força.',
            'Exemplo: <em>o tipo de pergunta ao chatbot varia conforme o perfil de uso do estudante?</em>',
        ],
        "quando": [
            '✅ Ambas as variáveis são <strong>categóricas nominais</strong>.',
            '✅ Frequência esperada ≥ 5 em pelo menos 80% das células (senão, Fisher exato).',
            '❌ Não use com variáveis ordinais — Spearman é mais adequado.',
            '❌ Nunca interpretar apenas o p-valor: sempre reporte V de Cramér.',
        ],
        "tip": '<strong>V de Cramér:</strong> pequeno ≈ 0.10 · médio ≈ 0.30 · grande ≈ 0.50',
        "python_code": '''import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

tabela = pd.DataFrame(
    [[30,15,10],[20,25,18],[10,20,35]],
    index   = ['factual','conceitual','procedimental'],
    columns = ['passivo','ativo','intensivo']
)
print(tabela, "\\n")

chi2, p, gl, esperadas = chi2_contingency(tabela)
print(f"χ² = {chi2:.3f}  gl = {gl}  p = {p:.4f}")

n = tabela.values.sum()
k = min(tabela.shape) - 1
V = np.sqrt(chi2 / (n * k))
efeito = 'pequeno' if V < .3 else 'médio' if V < .5 else 'grande'
print(f"V de Cramér = {V:.3f}  → efeito {efeito}")''',
        "refs": [
            ("seminal", "Cramér, H. (1946). <em>Mathematical Methods of Statistics</em>. Princeton University Press."),
            ("didático", "Agresti, A. (2013). <em>Categorical Data Analysis</em> (3ª ed.). Wiley."),
            ("tamanho efeito", "Cohen, J. (1988). <em>Statistical Power Analysis for the Behavioral Sciences</em> (2ª ed.). Cap. 7."),
            ("crítico", "Kim, H. Y. (2017). Chi-squared test and Fisher's exact test. <em>Restorative Dentistry & Endodontics, 42</em>(2), 152–155."),
        ],
    },
    {
        "dir": "05parcial-fatorial",
        "num": 5,
        "nav_order": 7,
        "bloco": 1,
        "title": "Correlação Parcial e Análise Fatorial",
        "subtitle": "pingouin.partial_corr() · factor_analyzer",
        "metaphor_label": "Duas metáforas, um encontro",
        "metaphor": (
            '<strong>Correlação parcial — o filtro de ruído:</strong> como usar um equalizador para '
            '<em>silenciar o baixo</em> e ouvir a guitarra — remove o efeito de uma variável de confusão.<br><br>'
            '<strong>Análise Fatorial — o organizador de gavetas:</strong> agrupa variáveis que se movem juntas '
            'em fatores latentes interpretáveis (ex.: "metacognição").'
        ),
        "serve": [
            '<strong>Correlação parcial:</strong> isola a relação entre X e Y removendo o efeito de uma terceira variável.',
            '<strong>EFA:</strong> reduz muitas variáveis correlacionadas a poucos fatores latentes. Valida instrumentos.',
        ],
        "quando": [
            '✅ <strong>Parcial:</strong> quando há variável de confusão (ex.: conhecimento prévio).',
            '✅ <strong>EFA:</strong> quando há ≥ 5 variáveis correlacionadas e suspeita-se de construtos latentes.',
            '✅ <strong>EFA:</strong> n ≥ 100; regra de 10 sujeitos por item.',
            '❌ EFA não é para predição — use regressão.',
        ],
        "python_code": '''import pingouin as pg
import pandas as pd

df = pd.DataFrame({
    'uso_chatbot':   [3,7,2,9,5,11,4,8],
    'aprendizagem':  [55,70,50,82,63,88,58,76],
    'conhec_previo': [40,55,35,70,50,75,45,60]
})

r_bruta = pg.corr(df['uso_chatbot'], df['aprendizagem'])
print("Pearson bruto:      r =", round(r_bruta['r'].values[0], 3))

r_parcial = pg.partial_corr(
    data=df, x='uso_chatbot', y='aprendizagem', covar='conhec_previo'
)
print("Pearson parcial:    r =", round(r_parcial['r'].values[0], 3))''',
        "refs": [
            ("didático", "Tabachnick, B. G., & Fidell, L. S. (2019). <em>Using Multivariate Statistics</em> (7ª ed.). Cap. 13."),
            ("aplicado", "Costello, A. B., & Osborne, J. W. (2005). Best practices in exploratory factor analysis. <em>Practical Assessment, Research & Evaluation, 10</em>(7)."),
            ("python", "Biggs, J. (2023). <em>factor_analyzer</em> package documentation."),
            ("conceitual", "MacCallum, R. C. (2009). Factor analysis. In <em>The SAGE Handbook of Quantitative Methods in Psychology</em>."),
        ],
    },
    {
        "dir": "06teste-t",
        "num": 6,
        "nav_order": 8,
        "bloco": 2,
        "title": "Teste t (independente e pareado)",
        "subtitle": "pingouin.ttest() · scipy.stats.ttest_ind · ttest_rel",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Duas balanças: escores com feedback vs. sem feedback. O teste t pergunta se a diferença é grande '
            'o suficiente para não ser mero acaso. O <strong>Cohen\'s d</strong> mede o quanto as distribuições se separam. '
            'O <strong>t pareado</strong> mede a mudança nas <em>mesmas</em> pessoas antes e depois.'
        ),
        "serve": [
            'Compara a <strong>média</strong> de uma variável numérica entre <strong>exatamente dois grupos</strong>.',
        ],
        "quando": [
            '✅ Variável dependente contínua e exatamente dois grupos.',
            '✅ Verificar normalidade (Shapiro-Wilk) e homocedasticidade (Levene).',
            '✅ Se Levene rejeitar → usar Welch (padrão no scipy).',
            '❌ Se normalidade violada com n pequeno → Mann-Whitney.',
            '⚠️ Sempre reporte Cohen\'s d além do p-valor.',
        ],
        "python_code": '''import pingouin as pg
from scipy.stats import shapiro, levene

feedback     = [72,85,78,90,68,82,76,88]
sem_feedback = [60,65,70,58,63,72,55,67]

_, p_n1 = shapiro(feedback);     print(f"Shapiro G1: p={p_n1:.3f}")
_, p_n2 = shapiro(sem_feedback);  print(f"Shapiro G2: p={p_n2:.3f}")
_, p_lv = levene(feedback, sem_feedback); print(f"Levene:     p={p_lv:.3f}")

res = pg.ttest(feedback, sem_feedback, paired=False, correction='auto')
print(res[['T', 'dof', 'p-val', 'cohen-d', 'power']])''',
        "refs": [
            ("seminal", 'Student [Gosset, W. S.] (1908). The probable error of a mean. <em>Biometrika, 6</em>(1), 1–25.'),
            ("tamanho efeito", "Cohen, J. (1988). <em>Statistical Power Analysis</em>. Cap. 2."),
            ("didático", "Field, A. (2024). <em>Discovering Statistics</em>. Cap. 10."),
            ("crítico", "Sullivan, G. M., & Feinn, R. (2012). Using effect size. <em>Journal of Graduate Medical Education, 4</em>(3), 279–282."),
        ],
    },
    {
        "dir": "07mann-whitney",
        "num": 7,
        "nav_order": 9,
        "bloco": 2,
        "title": "Mann-Whitney e Wilcoxon",
        "subtitle": "scipy.stats.mannwhitneyu · wilcoxon · pingouin.mwu()",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Em vez de comparar médias, junta todos numa fila ordenada e verifica se um grupo tende a ocupar '
            'posições mais altas. Não importa <em>quanto</em> mais alto — só <em>que é mais alto</em>.'
        ),
        "serve": [
            'Compara a <strong>distribuição de postos</strong> entre dois grupos sem assumir normalidade.',
            '<strong>Mann-Whitney U</strong>: independentes. <strong>Wilcoxon signed-rank</strong>: pareadas.',
        ],
        "quando": [
            '✅ Dados ordinais (Likert) ou numéricos que violam normalidade.',
            '✅ Amostras pequenas (n &lt; 30).',
            '✅ Outliers que não devem ser removidos.',
            '❌ Não testa diferença de médias — testa diferença de distribuições.',
        ],
        "tip": '<strong>Tamanho de efeito r:</strong> r = Z / √N. Pequeno ≥ 0.10 · médio ≥ 0.30 · grande ≥ 0.50.',
        "python_code": '''import pingouin as pg
from scipy.stats import wilcoxon

grupo_a = [3,5,4,6,7,4,5]
grupo_b = [2,3,1,4,3,2,3]

res_mw = pg.mwu(grupo_a, grupo_b, alternative='two-sided')
print("Mann-Whitney:")
print(res_mw[['U-val', 'p-val', 'RBC', 'CLES']])

pre  = [3,5,4,6,4,3]
pos  = [5,6,6,7,6,5]
stat, p_w = wilcoxon(pre, pos, alternative='two-sided')
print(f"\\nWilcoxon: W = {stat:.0f}, p = {p_w:.4f}")''',
        "refs": [
            ("seminal", "Mann, H. B., & Whitney, D. R. (1947). <em>Annals of Mathematical Statistics, 18</em>(1), 50–60."),
            ("seminal", "Wilcoxon, F. (1945). <em>Biometrics Bulletin, 1</em>(6), 80–83."),
            ("didático", "Field, A. (2024). <em>Discovering Statistics</em>. Cap. 7."),
            ("efeito", "Kerby, D. S. (2014). The simple difference formula. <em>Comprehensive Psychology, 3</em>."),
        ],
    },
    {
        "dir": "08anova",
        "num": 8,
        "nav_order": 10,
        "bloco": 2,
        "title": "ANOVA de uma via e Kruskal-Wallis",
        "subtitle": "pingouin.anova() · scipy.stats.kruskal · scikit_posthocs",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Vários testes t acumulam erro (quase 15% com 3 comparações). ANOVA faz uma só pergunta: '
            '<em>há pelo menos um grupo diferente?</em> Compara variação <em>entre</em> vs. <em>dentro</em> dos grupos. '
            'Se F for significativo, o <strong>pós-hoc de Tukey</strong> indica onde.'
        ),
        "serve": [
            'Compara médias (ANOVA) ou distribuições de postos (Kruskal-Wallis) entre <strong>três ou mais grupos</strong>.',
        ],
        "quando": [
            '✅ Comparar ≥ 3 grupos independentes.',
            '✅ <strong>ANOVA:</strong> dados normais e variâncias homogêneas. Reporte η².',
            '✅ <strong>Kruskal-Wallis:</strong> dados ordinais ou não-normais. Pós-hoc: Dunn.',
            '❌ ANOVA significativa sem pós-hoc não diz onde está a diferença.',
        ],
        "tip": '<strong>Eta-quadrado (η²):</strong> pequeno = 0.01 · médio = 0.06 · grande = 0.14',
        "python_code": '''import pingouin as pg
import pandas as pd
from scipy.stats import kruskal

df = pd.DataFrame({
    'perguntas': [3,4,2,5, 7,8,6,9, 12,14,11,13],
    'perfil':    ['passivo']*4 + ['ativo']*4 + ['intensivo']*4
})

aov = pg.anova(data=df, dv='perguntas', between='perfil', detailed=True)
print(aov[['Source','F','p-unc','np2']])

ph = pg.pairwise_tukey(data=df, dv='perguntas', between='perfil')
print(ph[['A','B','diff','p-tukey','hedges']])

H, p_k = kruskal(
    df[df.perfil=='passivo'].perguntas,
    df[df.perfil=='ativo'].perguntas,
    df[df.perfil=='intensivo'].perguntas
)
print(f"\\nKruskal-Wallis: H = {H:.3f}, p = {p_k:.4f}")''',
        "refs": [
            ("seminal", "Fisher, R. A. (1925). <em>Statistical Methods for Research Workers</em>."),
            ("seminal", "Kruskal, W. H., & Wallis, W. A. (1952). <em>Journal of the American Statistical Association, 47</em>(260), 583–621."),
            ("didático", "Field, A. (2024). <em>Discovering Statistics</em>. Caps. 12–13."),
            ("python", "Pohlert, T. (2014). PMCMR package — lógica do pós-hoc de Dunn."),
        ],
    },
    {
        "dir": "09anova-fatorial",
        "num": 9,
        "nav_order": 11,
        "bloco": 2,
        "title": "ANOVA Fatorial e Medidas Repetidas",
        "subtitle": "pingouin.anova() · pingouin.rm_anova() · statsmodels AnovaRM",
        "metaphor_label": "Duas variações do mesmo instrumento",
        "metaphor": (
            '<strong>Fatorial:</strong> verifica efeito de cada fator e a <em>interação</em> (ex.: café ajuda de manhã mas não à noite).<br><br>'
            '<strong>Medidas Repetidas:</strong> o mesmo estudante medido em pré, durante e pós — cada pessoa é seu próprio controle.'
        ),
        "serve": [
            '<strong>Fatorial:</strong> avalia múltiplos fatores e interações. <strong>MR:</strong> compara os mesmos sujeitos em ≥ 3 momentos.',
        ],
        "quando": [
            '✅ <strong>Fatorial:</strong> dois ou mais fatores categóricos com interesse na interação.',
            '✅ <strong>MR:</strong> mesmo sujeito em ≥ 3 momentos longitudinais.',
            '✅ Verificar esfericidade (Mauchly) — se violada, correção Greenhouse-Geisser.',
            '❌ Dropout sistemático → prefira LMM.',
        ],
        "python_code": '''import pingouin as pg
import pandas as pd

df_rm = pd.DataFrame({
    'sujeito': list(range(8)) * 3,
    'momento': ['pre']*8 + ['durante']*8 + ['pos']*8,
    'escore':  [50,55,48,60,52,58,45,53,
                62,68,59,72,65,70,57,64,
                75,80,70,85,78,83,68,76]
})

rm = pg.rm_anova(data=df_rm, dv='escore', within='momento',
                 subject='sujeito', correction=True)
print(rm[['Source','F','p-unc','p-GG-corr','ng2']])

ph = pg.pairwise_tests(data=df_rm, dv='escore', within='momento',
                       subject='sujeito', padjust='bonf')
print(ph[['A','B','T','p-corr','cohen-d']])''',
        "refs": [
            ("didático", "Field, A. (2024). <em>Discovering Statistics</em>. Caps. 14–15."),
            ("técnico", "Greenhouse, S. W., & Geisser, S. (1959). <em>Psychometrika, 24</em>(2), 95–112."),
            ("python", "Vallat, R. (2018). Pingouin: statistics in Python."),
            ("aplicado", "Girden, E. R. (1992). <em>ANOVA: Repeated Measures</em>. SAGE."),
        ],
    },
    {
        "dir": "10lmm",
        "num": 10,
        "nav_order": 12,
        "bloco": 2,
        "title": "Modelos Lineares Mistos (LMM)",
        "subtitle": "statsmodels.formula.api.mixedlm · pingouin.mixed_anova()",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Dados aninhados (mensagens em sessões, sessões em estudantes) violam independência. '
            'LMM tem <strong>efeitos fixos</strong> (o efeito na população) e <strong>efeitos aleatórios</strong> '
            '(variabilidade de cada estudante/turma). Cada sujeito ganha seu próprio ponto de partida.'
        ),
        "serve": [
            'Modelar dados com estrutura <strong>hierárquica</strong>: mensagens → sessões → estudantes → turmas.',
        ],
        "quando": [
            '✅ Observações aninhadas em grupos.',
            '✅ Dados longitudinais com faltantes ou grupos desiguais.',
            '✅ Quando ANOVA MR não converge.',
            '❌ Comece com modelos simples (só intercepto aleatório).',
        ],
        "python_code": '''import statsmodels.formula.api as smf
import pandas as pd
import numpy as np

np.random.seed(42)
n_est, n_ses = 20, 5

df = pd.DataFrame({
    'estudante': np.repeat(range(n_est), n_ses),
    'sessao':    list(range(n_ses)) * n_est,
    'turnos':    np.random.poisson(6, n_est*n_ses),
    'escore':    np.random.normal(70, 10, n_est*n_ses)
})
df['escore'] += df['turnos'] * 1.5

modelo = smf.mixedlm("escore ~ turnos", data=df, groups=df["estudante"]).fit(reml=True)
print(modelo.summary())''',
        "refs": [
            ("referência", "Gelman, A., & Hill, J. (2007). <em>Data Analysis Using Regression and Multilevel Models</em>."),
            ("acessível", "Winter, B. (2019). <em>Statistics for Linguists</em>. Routledge."),
            ("educação", "Raudenbush, S. W., & Bryk, A. S. (2002). <em>Hierarchical Linear Models</em> (2ª ed.)."),
            ("python", "Seabold, S., & Perktold, J. (2010). Statsmodels. <em>SciPy Proceedings</em>."),
        ],
    },
    {
        "dir": "11regressao-linear",
        "num": 11,
        "nav_order": 13,
        "bloco": 3,
        "title": "Regressão Linear (simples e múltipla)",
        "subtitle": "statsmodels.formula.api.ols() · sklearn LinearRegression",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'A regressão traça a <em>linha reta que erra menos</em> para todos os pontos. '
            'A múltipla adiciona dimensões: cada coeficiente é o efeito <em>único</em> da variável, '
            'mantendo as outras constantes.'
        ),
        "serve": [
            'Modelar e predizer um desfecho <strong>numérico contínuo</strong> a partir de preditores.',
        ],
        "quando": [
            '✅ Desfecho numérico contínuo.',
            '✅ Relação linear entre preditores e desfecho.',
            '✅ Resíduos normais e homocedásticos.',
            '✅ VIF &gt; 5 indica multicolinearidade.',
            '❌ Para inferência científica use statsmodels; para ML use sklearn.',
        ],
        "python_code": '''import statsmodels.formula.api as smf
import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.DataFrame({
    'escore_final':  [72,85,60,90,68,78,82,55,88,74],
    'uso_chatbot':   [5,9,3,12,4,7,10,2,11,6],
    'metacognicao':  [60,72,55,80,58,68,75,50,78,65],
    'letramento_ia': [40,55,35,65,42,52,60,30,62,48]
})

modelo = smf.ols('escore_final ~ uso_chatbot + metacognicao + letramento_ia', data=df).fit()
print(modelo.summary())

X = df[['uso_chatbot','metacognicao','letramento_ia']]
vif = pd.DataFrame({
    'variável': X.columns,
    'VIF': [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
})
print(vif)''',
        "refs": [
            ("referência", "Hair, J. F., et al. (2019). <em>Multivariate Data Analysis</em> (8ª ed.). Cap. 4."),
            ("didático", "James, G., et al. (2023). <em>An Introduction to Statistical Learning</em> (2ª ed.). Cap. 3."),
            ("VIF", "O'Brien, R. M. (2007). A caution regarding rules of thumb for VIF. <em>Quality & Quantity, 41</em>, 673–690."),
            ("python", "McKinney, W. (2022). <em>Python for Data Analysis</em>."),
        ],
    },
    {
        "dir": "12regressao-logistica",
        "num": 12,
        "nav_order": 14,
        "bloco": 3,
        "title": "Regressão Logística (binária e ordinal)",
        "subtitle": "statsmodels Logit() · mord · sklearn ROC/AUC",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Para prever <em>engajou ou não engajou</em>, a logística usa uma sigmoid que espreme valores em [0, 1] — '
            'probabilidade. Coeficientes como <strong>odds ratios</strong>: OR = 2 significa chances dobradas. '
            'A <strong>curva ROC</strong> mede a qualidade do modelo (AUC).'
        ),
        "serve": [
            'Modelar desfechos <strong>categóricos</strong>: binária (engajou/não) ou ordinal (baixo/médio/alto).',
        ],
        "quando": [
            '✅ <strong>Binária:</strong> duas categorias mutuamente exclusivas.',
            '✅ <strong>Ordinal:</strong> 3+ categorias ordenadas.',
            '✅ AUC &gt; 0.70 aceitável · &gt; 0.80 bom · &gt; 0.90 excelente.',
            '❌ Não use regressão linear para desfecho binário.',
        ],
        "python_code": '''import statsmodels.api as sm
import pandas as pd
import numpy as np
from sklearn.metrics import roc_auc_score

df = pd.DataFrame({
    'engajou':     [1,0,1,1,0,1,0,1,0,1,0,1],
    'uso_chatbot': [8,2,9,7,3,10,1,8,4,9,2,11],
    'metacognicao':[65,40,70,68,38,75,35,72,42,78,33,80]
})

X = sm.add_constant(df[['uso_chatbot', 'metacognicao']])
modelo = sm.Logit(df['engajou'], X).fit(disp=0)
print(modelo.summary())

OR = np.exp(modelo.params)
print("\\nOdds Ratios:")
print(OR.round(3))

y_pred = modelo.predict(X)
auc = roc_auc_score(df['engajou'], y_pred)
print(f"\\nAUC = {auc:.3f}")''',
        "refs": [
            ("referência", "Hosmer, D. W., Lemeshow, S., & Sturdivant, R. X. (2013). <em>Applied Logistic Regression</em> (3ª ed.)."),
            ("didático", "Field, A. (2024). <em>Discovering Statistics</em>. Cap. 20."),
            ("ROC", "Fawcett, T. (2006). An introduction to ROC analysis. <em>Pattern Recognition Letters, 27</em>(8), 861–874."),
            ("ordinal", "McCullagh, P. (1980). Regression models for ordinal data. <em>JRSS B, 42</em>(2), 109–142."),
        ],
    },
    {
        "dir": "13poisson",
        "num": 13,
        "nav_order": 15,
        "bloco": 3,
        "title": "Regressão de Poisson e Binomial Negativa",
        "subtitle": "statsmodels poisson() · negativebinomial()",
        "metaphor_label": "Imagine isso…",
        "metaphor": (
            'Contagens (perguntas ao chatbot) são inteiras e nunca negativas. Poisson modela a taxa de eventos. '
            'Se a variância explode (superdispersão), a <strong>Binomial Negativa</strong> adiciona folga extra.'
        ),
        "serve": [
            'Modelar desfechos de <strong>contagem</strong>: turnos, perguntas, mensagens. Poisson para equidispersão; BN para superdispersão.',
        ],
        "quando": [
            '✅ Desfecho são contagens inteiras não-negativas.',
            '✅ <strong>Poisson:</strong> variância/média ≈ 1.',
            '✅ <strong>BN:</strong> índice de dispersão &gt; 1.5.',
            '✅ Comparar via AIC: menor = melhor.',
            '❌ Não use regressão linear para contagens.',
        ],
        "tip": '<strong>Interpretar coeficientes:</strong> exp(coef) = Risk Ratio. RR = 1.3 → 30% mais eventos por unidade.',
        "python_code": '''import statsmodels.formula.api as smf
import pandas as pd
import numpy as np

np.random.seed(7)
n = 80
df = pd.DataFrame({
    'perguntas':    np.random.negative_binomial(2, 0.3, n),
    'metacognicao': np.random.normal(60, 10, n),
    'tempo_sessao': np.random.normal(20, 5, n)
})

media, var = df.perguntas.mean(), df.perguntas.var()
print(f"Média={media:.2f}  Variância={var:.2f}  Índice={var/media:.2f}")

mod_p  = smf.poisson('perguntas ~ metacognicao + tempo_sessao', data=df).fit(disp=0)
mod_nb = smf.negativebinomial('perguntas ~ metacognicao + tempo_sessao', data=df).fit(disp=0)

print(f"AIC Poisson = {mod_p.aic:.1f}")
print(f"AIC BN      = {mod_nb.aic:.1f}")

print("\\nRisk Ratios (BN):")
print(np.exp(mod_nb.params).round(3))''',
        "refs": [
            ("referência", "Cameron, A. C., & Trivedi, P. K. (2013). <em>Regression Analysis of Count Data</em> (2ª ed.)."),
            ("didático", "Hilbe, J. M. (2011). <em>Negative Binomial Regression</em> (2ª ed.)."),
            ("comparação", "Ver Hoef, J. M., & Boveng, P. L. (2007). Quasi-Poisson vs. negative binomial. <em>Ecology, 88</em>(11), 2766–2772."),
            ("educação", "Coxe, S., West, S. G., & Aiken, L. S. (2009). The analysis of count data. <em>Journal of Personality Assessment, 91</em>(2), 121–136."),
        ],
    },
]
