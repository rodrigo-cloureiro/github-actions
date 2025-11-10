# 🧾 SISREL – Sistema de Relatórios de Vendas

Projeto didático em Python usado para demonstrar integração contínua (CI) com GitHub Actions.

------------------------------------------------------------
## 🚀 Objetivos da Aula

- Entender o ciclo Commit → Teste → Feedback automático.
- Aprender o básico sobre workflows, jobs, steps e actions.
- Configurar um pipeline simples de execução de testes automáticos.

------------------------------------------------------------
## 🧱 Estrutura do Projeto

.
├─ sisrel.py            # Código principal do sistema
├─ requirements.txt     # Dependências do projeto
├─ tests/               # Testes unitários com pytest
└─ .github/workflows/   # Workflows do GitHub Actions

------------------------------------------------------------
## ⚙️ Como rodar localmente

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -v

------------------------------------------------------------
## 💡 Integração Contínua

Cada push ou pull request executa automaticamente o workflow:

name: Python CI
on: [push, pull_request]

Status do build:

https://img.shields.io/github/actions/workflow/status/SEU_USUARIO/SEU_REPOSITORIO/ci.yml?branch=main&label=build

------------------------------------------------------------
## 🧪 Testes e Cobertura

(Em breve) adicionaremos pytest-cov para exibir porcentagem de cobertura de testes.

Badge de cobertura (futuro):

https://img.shields.io/badge/coverage-100%25-brightgreen

------------------------------------------------------------
## 🧩 Próximos Passos

1. Adicionar cobertura de testes.
2. Configurar badge de versão automática via tag ou version.txt.
3. Publicar relatório do pytest como artifact.
4. Explorar actions externas (como SonarCloud ou Codecov).

------------------------------------------------------------
Feito com ❤️ para as aulas de DevOps / Integração Contínua.
