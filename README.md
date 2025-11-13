# 🧾 SISREL – Sistema de Relatórios de Vendas

Projeto didático em Python usado para demonstrar integração contínua (CI) com GitHub Actions.

---

## 🚀 Objetivos da Aula

- Entender o ciclo Commit → Teste → Feedback automático.
- Aprender o básico sobre workflows, jobs, steps e actions.
- Configurar um pipeline simples de execução de testes automáticos.

---

## 🧱 Estrutura do Projeto

```bash
.
├─ sisrel.py # Código principal do sistema
├─ requirements.txt # Dependências do projeto
├─ tests/ # Testes unitários com pytest
└─ .github/workflows/ # Workflows do GitHub Actions
```

---

## ⚙️ Como rodar localmente

python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v

---

## 💡 Integração Contínua

Cada push ou pull request executa automaticamente o workflow:

name: Python CI
on: [push, pull_request]

Status do build:

![HELLO_WORD](https://img.shields.io/github/actions/workflow/status/rodrigo-cloureiro/github-actions/hello_world.yaml?branch=main)

![BUILD](https://img.shields.io/github/actions/workflow/status/rodrigo-cloureiro/github-actions/build.yaml?branch=main)

![BUILD COM FALLBACK](https://img.shields.io/github/actions/workflow/status/rodrigo-cloureiro/github-actions/build_com_fallback.yaml?branch=main)

![EXEMPLO OUTPUT](https://img.shields.io/github/actions/workflow/status/rodrigo-cloureiro/github-actions/exemplo_output.yaml?branch=main)

---

## 🧪 Testes e Cobertura

pytest-cov para exibir porcentagem de cobertura de testes.

Badge de cobertura:

![Coverage](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/rodrigo-cloureiro/github-actions/main/coverage.json)

![Coverage](https://raw.githubusercontent.com/rodrigo-cloureiro/github-actions/master/coverage-badge.svg)

---

## 🧩 Próximos Passos

1. Adicionar cobertura de testes.
2. Configurar badge de versão automática via tag ou version.txt.
3. Publicar relatório do pytest como artifact.
4. Explorar actions externas (como SonarCloud ou Codecov).

---

Feito com ❤️ para as aulas de DevOps / Integração Contínua.
