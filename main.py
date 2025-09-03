from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}


class Cars(BaseModel):
    id: str
    brand: str
    model: str
    

Cars = []
@app.post("/cars/", response_model=Cars)
def creer_car(cars: Cars):
    Cars.append(cars)
    return cars 


@app.get("/cars/",  response_model=List[Cars])
def recuperation():
    return Cars



@app.get("/cars/{id}",  response_model=List[Cars])
def  recuperation(id:int):
    if id < len(Cars):
        return Cars[id]
    raise HTTPException(status_code=404 , detail="Le phone comportant l'id fourni n'existe pas!")


