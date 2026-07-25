from fastapi import FastAPI
from routes import SystemRouter, AIRouter

app = FastAPI()
app.include_router(SystemRouter)
app.include_router(AIRouter)
