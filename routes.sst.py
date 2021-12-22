from fastapi import APIRouter
from config.db import db
from schemas.sst import sstEntity, sstsEntity
from models.sst import SST
from bson import ObjectId


sst = APIRouter()

@sst.get('/ssts')
def find_all_sst():
    return sstsEntity(db.SST.sst85.find())

@sst.get('/ssts/{id}')
def find_sst(id: str):
    return sstEntity(db.SST.sst85.find_one({'_id': ObjectId(id)}))