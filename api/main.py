from fastapi import FastAPI
from api.routes import SystemRouter


app = FastAPI()
app.include_router(SystemRouter)
