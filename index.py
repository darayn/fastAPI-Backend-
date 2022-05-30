from fastapi import FastAPI

app = FastAPI()

from routes.levels import  fastAPILevel

app.include_router(fastAPILevel)