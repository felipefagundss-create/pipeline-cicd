# Pipeline CI/CD Demo

[![CI/CD Pipeline](https://github.com/felipefagundss-create/pipeline-cicd/actions/workflows/ci.yml/badge.svg)](https://github.com/felipefagundss-create/pipeline-cicd/actions/workflows/ci.yml)

Projeto 1 da Pós em Cloud Computing (módulo de Cultura DevOps e Integração Contínua). A API em si é bem simples, só existe pra ter algo real rodando — o que importa mesmo é o pipeline: toda vez que dou push, ele builda, testa e deploya sozinho.

Stack: Python + FastAPI, GitHub Actions, Docker, deploy no Render.

## Rodando

Local:
```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```
Abre em `localhost:8000` (`/docs` pra ver a documentação do Swagger). Pra rodar os testes: `pytest -v`.

Com Docker:
```bash
docker build -t pipeline-cicd-demo .
docker run -p 8000:8000 pipeline-cicd-demo
```

## O pipeline

Todo push dispara o `.github/workflows/ci.yml`: instala dependências, roda lint e pytest, builda a imagem Docker. Se passar tudo e o push foi na `main`, ele chama o deploy hook do Render e a API atualiza sozinha. Diagrama em [docs/pipeline-diagram.md](docs/pipeline-diagram.md).

Levei um tempo pra entender o motivo do job de Deploy falhar no início — é porque ele precisa do secret `RENDER_DEPLOY_HOOK_URL` configurado no repositório (Settings > Secrets and variables > Actions), copiado da tela de Settings do serviço no Render. Sem isso o curl do deploy não tem pra onde mandar a requisição.

## Próximos passos

Ainda quero adicionar TruffleHog no pre-commit (bloquear secret antes de virar commit), autenticação com AWS via OIDC, Semgrep como step de SAST, e um step que manda o diff do PR pra um LLM (Groq + Llama 3) pra comentar automaticamente se achar algo suspeito no código.

## Licença

MIT
