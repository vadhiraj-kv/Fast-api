from fastapi import FastAPI #framework
from pydantic import BaseModel #validation
from typing import List


app = FastAPI()

#structure definition
class car(BaseModel):
    id: int
    name: str
    origin: str


cars:List[car] = []

# decorator to give super power

@app.get("/") #decorator
def read_root():
    return{"message":"Welcome to python"}


#returns the cars
@app.get("/cars")
def get_teas():
    return cars

#add the cars
@app.post("/cars")
def add_tea(car:car):
    cars.append(car)
    return car


#update the cars
@app.put("/cars/{car_id}")
def update_tea(car_id:int,update_car: car):
    for index,car in enumerate(cars):
        if car.id == car_id:
            cars[index] = update_car
            return update_car
        
    return{"error":"car not found"}

#delets the cars
@app.delete("/cars/{car_id}")
def delete_tea(car_id: int):
    for index,car in enumerate(cars):
        if car.id == car_id:
            deleted = cars.pop(index)
            return deleted
    return{"error":"car not found"}