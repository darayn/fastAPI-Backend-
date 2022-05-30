
def levelEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "freshWaterLevel" : item["freshWaterLevel"],
        "batteryLevel" : item["batteryLevel"],
        "robotLinearVelocity" : item["robotLinearVelocity"],
        "robotAngularVelocity" : item["robotAngularVelocity"],
        "areaName" : item["areaName"],
        "timestamp" : item["ts"]

    }

def levelsEntity(entity) -> list:
    return [levelEntity(item) for item in entity]