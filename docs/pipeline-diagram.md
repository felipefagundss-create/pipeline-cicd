# Pipeline Diagram

```mermaid
flowchart LR
    A[Push / Pull Request] --> B[Checkout code]
    B --> C[Install dependencies]
    C --> D[Lint - flake8]
    D --> E[Run tests - pytest]
    E --> F[Build Docker image]
    F --> G{Branch = main?}
    G -- yes --> H[Deploy to Railway/Render]
    G -- no --> I[Stop - PR feedback only]
    H --> J[Live API]
```

**Flow summary:**
1. Every push or pull request triggers the `build-and-test` job.
2. Dependencies are installed, code is linted, and the test suite runs.
3. A Docker image is built to confirm the container is production-ready.
4. Only pushes to `main` that pass all checks trigger the `deploy` job.
5. The deploy job publishes the app to Railway or Render.
