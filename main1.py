from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    harry = "harry"
    neck = "neck"
    values = 10
    crono = "jems"
    carry = "carry"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.harry:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    elif model_name.value == "neck":
        return {"model_name": model_name, "message": "LeCNN all the images  "}
    
    elif model_name.value == "10":
        return {"model_name": model_name, "message": "you selected a this number "}
    
    elif model_name.value == "jems":
        return {"model_name": model_name, "message": "you selected a jems "}

    return {"model_name": model_name, "message": "Have some residuals"}
