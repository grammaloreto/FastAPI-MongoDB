from fastapi import FastAPI
from routes.sst import sst

app = FastAPI(
    title='Rest API (Python FastAPI) with MongoDB',
    description='This is a Rest API attached to a noSQL database'
)

app.include_router(sst)

