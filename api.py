from fastapi import FastAPI

app = FastAPI(title="Model Deployment Training")


@app.get("/")
def health():
    return {"status": "Healthy"}
