from fastapi import FastAPI
from routes import SystemRouter


app = FastAPI()
app.include_router(SystemRouter)
