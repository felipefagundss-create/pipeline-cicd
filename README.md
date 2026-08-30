# Pipeline CI/CD Demo

[![CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml)

Projeto 1 da Pós em Cloud Computing (módulo de Cultura DevOps e Integração Contínua). API bem simples em FastAPI, só pra ter algo real pra rodar pelo pipeline. O que importa aqui é o `.github/workflows/ci.yml`: toda vez que dou push, ele builda, testa e faz o deploy sozinho.

## Stack

- Python + FastAPI
- GitHub Actions
- Docker
- Deploy: Render

## Estrutura

```
.
├── app/
│   ├── __init__.py
│   └── main.py            # a API
├── tests/
│   └── test_main.py       # testes com pytest
├── docs/
│   └── pipeline-diagram.md
├── .github/workflows/
│   └── ci.yml              # o pipeline em si
├── Dockerfile
├── requirements.txt
└── requirements-dev.txt
```

## Rodando local

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Abre em `http://localhost:8000` (e `/docs` pra ver a documentação automática do Swagger).

## Rodando com Docker

```bash
docker build -t pipeline-cicd-demo .
docker run -p 8000:8000 pipeline-cicd-demo
```

## Testes

```bash
pytest -v
```

## Como funciona o pipeline

Diagrama completo em [docs/pipeline-diagram.md](docs/pipeline-diagram.md).

Em resumo:
1. Todo push ou PR dispara o job `build-and-test`: instala dependências, roda o `flake8` (lint) e o `pytest`, e builda a imagem Docker.
2. Se tudo passar E o push foi na `main`, roda o job `deploy`, que dispara o deploy hook do Render.

### Configurando o deploy no Render

1. Cria um Web Service no Render, conectado com Docker, apontando pra esse repo.
2. Nas configurações do serviço, copia a URL do "Deploy Hook".
3. No GitHub, vai em Settings > Secrets and variables > Actions e cria um secret `RENDER_DEPLOY_HOOK_URL` com essa URL.

## Próximos passos

Ainda vou adicionar:
- TruffleHog no pre-commit pra travar secret antes de virar commit
- Autenticação com AWS via OIDC (sem chave fixa)
- Semgrep como step de SAST
- Um step que manda o diff do PR pra um LLM (Groq + Llama 3) e comenta automaticamente se achar algo suspeito

## Licença

MIT
