"""
Minimal FastAPI application used as the anchor project for the CI/CD pipeline.

It intentionally stays small: the point of this repo is to demonstrate a
complete build -> test -> deploy pipeline with GitHub Actions, not a complex
API. Add real endpoints here as the project grows.
"""
from datetime import datetime, timezone

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Pipeline CI/CD Demo API",
    description="Anchor project for the DevSecOps portfolio — build, test and deploy automation.",
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
    """Used by the deploy platform (Railway/Render) for health checks."""
    return HealthResponse(
        status="ok",
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.post("/items", response_model=Item, tags=["items"])
def create_item(item: Item) -> Item:
    """Simple echo endpoint just so there is something meaningful to test."""
    return item
