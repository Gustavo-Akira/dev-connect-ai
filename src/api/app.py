from fastapi import FastAPI

from api.routes import router

app = FastAPI(title="Dev Connect AI", description="An API for querying a knowledge base using AI.", version="1.0.0")

app.include_router(router)