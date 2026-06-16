# math.rpmhub.dev

Materiais didáticos de **Análise de Dados Conversacionais** — estatística aplicada a logs de chatbots e interações educacionais.

Site: [math.rpmhub.dev](https://math.rpmhub.dev)

## Estrutura

```
docs/
├── index.md              # Home (Jekyll + just-the-docs)
├── materiais.html        # Visão geral interativa de todos os encontros
├── encontros.md          # Índice navegável
├── assets/
│   ├── css/math.css      # Tema visual
│   └── js/py-runner.js   # Execução Python via Pyodide
└── NNtopico/
    ├── topico.md         # Página Jekyll (conteúdo didático + código executável)
    └── slides/
        ├── index.html    # Apresentação Reveal.js
        └── slides.md
```

## Regenerar páginas

Após editar `scripts/topics.py`:

```bash
python3 scripts/generate_site.py
```

## Deploy

GitHub Pages a partir da pasta `docs/`. O domínio `math.rpmhub.dev` está configurado em `CNAME`.
