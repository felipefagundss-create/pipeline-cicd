# Pipeline CI/CD Demo

[![CI/CD Pipeline](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions/workflows/ci.yml)

A minimal FastAPI service used to demonstrate a complete CI/CD pipeline: automated build, automated tests, and automated deploy on every push to `main`. This is the anchor project of a broader DevSecOps portfolio — future projects will integrate with this pipeline.

## Stack

- **API:** Python + FastAPI
- **CI/CD:** GitHub Actions
- **Containerization:** Docker
- **Deploy target:** Railway or Render (see [.github/workflows/ci.yml](.github/workflows/ci.yml))

## Project structure

```
.
├── app/
│   ├── __init__.py
│   └── main.py            # FastAPI application
├── tests/
│   └── test_main.py       # Automated tests (pytest)
├── docs/
│   └── pipeline-diagram.md
├── .github/workflows/
│   └── ci.yml              # Build, test, deploy pipeline
├── Dockerfile
├── requirements.txt
└── requirements-dev.txt
```

## Running locally

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`. Interactive docs at `http://localhost:8000/docs`.

## Running with Docker

```bash
docker build -t pipeline-cicd-demo .
docker run -p 8000:8000 pipeline-cicd-demo
```

## Running tests

```bash
pytest -v
```

## CI/CD Pipeline

See [docs/pipeline-diagram.md](docs/pipeline-diagram.md) for the full flow diagram.

Every push and pull request runs:
1. Dependency install
2. Lint (`flake8`)
3. Tests (`pytest`)
4. Docker image build

On push to `main`, after all checks pass, the pipeline deploys automatically to Railway or Render.

### Setting up deploy

Pick one:

**Railway**
1. Create a project on [Railway](https://railway.app) and link this repo.
2. Generate a Railway token and add it as a GitHub secret named `RAILWAY_TOKEN`.
3. Uncomment the "Deploy to Railway" step in `.github/workflows/ci.yml`.

**Render**
1. Create a Web Service on [Render](https://render.com) connected to Docker.
2. Copy the service's Deploy Hook URL.
3. Add it as a GitHub secret named `RENDER_DEPLOY_HOOK_URL`.
4. Uncomment the "Deploy to Render" step in `.github/workflows/ci.yml`.

## Roadmap (next iterations)

- [ ] Pre-commit hook with TruffleHog for secret scanning
- [ ] OIDC federation for AWS authentication (no static credentials)
- [ ] Semgrep SAST step
- [ ] GitGuardian secret scanning
- [ ] AI-powered PR review step (Groq API + Llama 3) that comments on security issues in the diff

## License

MIT
