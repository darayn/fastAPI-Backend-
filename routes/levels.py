from datetime import datetime
import random
from fastapi import APIRouter
from pymongo import InsertOne

from models.level import Level
import datetime 
from configs.db import conn
import dateutil.parser as parser

from schemas.levels import levelsEntity, levelEntity
from bson.objectid import ObjectId


fastAPILevel = APIRouter()

@fastAPILevel.post('/')
async def insertData(level : Level):
    conn.local.fastAPI.insert_one(dict(level),{"ts": datetime.datetime.utcnow()})
    
    return {

        "task" : "Levels added "
    }


@fastAPILevel.get('/rangeLevels')
async def getLevels(t1 : str, t2: str):
    # dateNow = datetime.datetime.now()
    date1 = parser.parse(t1)
    date2 = parser.parse(t2)
    ts1 = date1.isoformat();
    ts2 = date2.isoformat();
    print(ts1, ts2)
    res =  levelsEntity(conn.local.user.find({"ts": {"$gte" : ts1, "$lte" : ts2}}))
    if len(res):
        return res
    return{
        "message" : "notfound"
    }
    


@fastAPILevel.get('/bulkInsert')
async def insertBulkData():
    # dateNow = datetime.datetime.now()
    area_list = ["Pune", "Mumbai", "Bangalore", "Delhi", "Us"]
    for i in range(100):
        conn.local.fastAPI.insert_one({
            
            "freshWaterLevel": random.randint(200, 1009),
            "batteryLevel": random.randint(20, 109),
            "robotLinearVelocity": random.randint(2500, 5668),
            "robotAngularVelocity": random.randint(200, 1009),
            "areaName": random.choice(area_list),
            "ts": (datetime.datetime.utcnow())

        })
    
    return {

        "task" : "Levels added 100"
    }
