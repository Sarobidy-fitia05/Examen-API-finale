from fastapi import FastAPI , HTTPException
from pydantic import BaseModel
from typing import List
app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

class characteristic(BaseModel):
    max_speed: int
    max_fuel_capacity: int


class Cars(BaseModel):
    id: str
    brand: str
    model: str
    characteristic: characteristic
    

Cars = []
@app.post("/cars/", response_model=Cars)
def creer_car(cars: Cars):
    Cars.append(cars)
    return cars 


@app.get("/cars/",  response_model=List[Cars])
def recuperation():
    return Cars


@app.get("/phones/{car_id}", response_model=Cars)
async def get_phone(car_id: str):
    for Cars in Cars:
        if Cars.identifier == car_id:
            return Cars
    raise HTTPException(status_code=404, detail=f"Le phone comportant l'id {car_id}  n'existe pas")


@app.put("/phones/{car_id}/characteristics", response_model=Cars)
async def update_phone_characteristics(phone_id: str, characteristics: Characteristic):
    for cars in Cars:
        if cars.identifier == car_id:
            cars.characteristic = characteristic
            return cars
    raise HTTPException(status_code=404, detail=f"Le phone comportant l'id {car_id}  n'existe pas")

