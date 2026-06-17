---
layout: default
title: Qui-quadrado e V de Cramér
nav_order: 4
parent: Associação
has_children: false
---

# Enc. 4 — Qui-quadrado e V de Cramér

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
> Imagine um cardápio com três pratos (factual, conceitual, procedimental) e três tipos de clientes. O qui-quadrado compara o *observado* com o *esperado* se não houvesse relação. O **V de Cramér** quantifica a força dessa associação, livre do tamanho amostral.

---

## 🎯 Para que serve

Testa se duas variáveis **categóricas** são independentes. O **p-valor do χ²** indica significância; o **V de Cramér** quantifica a força.

Exemplo: *o tipo de pergunta ao chatbot varia conforme o perfil de uso do estudante?*

---

## 📋 Quando usar

- ✅ Ambas as variáveis são **categóricas nominais**.
- ✅ Frequência esperada ≥ 5 em pelo menos 80% das células (senão, Fisher exato).
- ❌ Não use com variáveis ordinais — Spearman é mais adequado.
- ❌ Nunca interpretar apenas o p-valor: sempre reporte V de Cramér.

{: .highlight }
> **V de Cramér:** pequeno ≈ 0.10 · médio ≈ 0.30 · grande ≈ 0.50

---

## 🐍 Exemplo Python


<div class="python-runner" data-code="aW1wb3J0IHBhbmRhcyBhcyBwZAppbXBvcnQgbnVtcHkgYXMgbnAKZnJvbSBzY2lweS5zdGF0cyBpbXBvcnQgY2hpMl9jb250aW5nZW5jeQoKdGFiZWxhID0gcGQuRGF0YUZyYW1lKAogICAgW1szMCwxNSwxMF0sWzIwLDI1LDE4XSxbMTAsMjAsMzVdXSwKICAgIGluZGV4ICAgPSBbJ2ZhY3R1YWwnLCdjb25jZWl0dWFsJywncHJvY2VkaW1lbnRhbCddLAogICAgY29sdW1ucyA9IFsncGFzc2l2bycsJ2F0aXZvJywnaW50ZW5zaXZvJ10KKQpwcmludCh0YWJlbGEsICJcbiIpCgpjaGkyLCBwLCBnbCwgZXNwZXJhZGFzID0gY2hpMl9jb250aW5nZW5jeSh0YWJlbGEpCnByaW50KGYiz4fCsiA9IHtjaGkyOi4zZn0gIGdsID0ge2dsfSAgcCA9IHtwOi40Zn0iKQoKbiA9IHRhYmVsYS52YWx1ZXMuc3VtKCkKayA9IG1pbih0YWJlbGEuc2hhcGUpIC0gMQpWID0gbnAuc3FydChjaGkyIC8gKG4gKiBrKSkKZWZlaXRvID0gJ3BlcXVlbm8nIGlmIFYgPCAuMyBlbHNlICdtw6lkaW8nIGlmIFYgPCAuNSBlbHNlICdncmFuZGUnCnByaW50KGYiViBkZSBDcmFtw6lyID0ge1Y6LjNmfSAg4oaSIGVmZWl0byB7ZWZlaXRvfSIp" markdown="0">
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
| **tamanho efeito** | Cohen, J. (1988). *Statistical Power Analysis for the Behavioral Sciences* (2ª ed.). Cap. 7. |
| **crítico** | Kim, H. Y. (2017). Chi-squared test and Fisher's exact test. *Restorative Dentistry & Endodontics, 42*(2), 152–155. |

---

<center>
<a href="https://rpmhub.dev" target="_blank"><img src="../imgs/logo.png" alt="Rodrigo Prestes Machado" width="3%" border="0"></a><br/>
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/">CC BY 4.0 DEED</a>
</center>
