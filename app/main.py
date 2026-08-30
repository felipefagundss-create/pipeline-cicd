# API simples pra testar o pipeline de CI/CD.
# O foco aqui não é a API em si, é o build -> test -> deploy automatizado.
from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Pipeline CI/CD Demo API",
    version="0.1.0",
)


class HealthResponse(BaseModel):
    status: str
    timestamp: str


class Item(BaseModel):
    name: str
    description: str | None = None


@app.get("/", tags=["root"])
def read_root() -> dict:
    return {"message": "Pipeline CI/CD Demo API is running"}


@app.get("/health", response_model=HealthResponse, tags=["health"])
def health_check() -> HealthResponse:
    # o Render bate nessa rota pra saber se o serviço está de pé
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.post("/items", response_model=Item, tags=["items"])
def create_item(item: Item) -> Item:
    # só devolve o mesmo item, é pra ter algo pra testar no pytest mesmo
    return item
