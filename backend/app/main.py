from fastapi import FastAPI

app = FastAPI(
    title="Ecology ML Portfolio API",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {"status": "ok"}