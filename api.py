from fastapi import APIRouter
from pydantic import BaseModel
from config import connect
from random import randint
router = APIRouter()

class Driver(BaseModel):
    rating_drive: float

class Passenger(BaseModel):
    rating: float

class Orders(BaseModel):
    id_car: int
    user_id: int
    driver_id: int
    point_from: str
    point_to: str
    time_of_order: str
    status: str

class Cars(BaseModel):
    model: str
    color: str
    car_number: str
    free_status: bool

@router.post("/driver/create")
async def add_driver(driver: Driver):
    cur = connect.cursor()
    id = randint(1,99999999)
    query = """INSERT INTO gashev_yaroshenko.driver (driver_id, rating_drive) VALUES (%s, %s);"""
    values = (id, driver.rating_drive)
    cur.execute(query, values)
    connect.commit()
    return "200"

@router.get("/cars/all")
async def get_all_cars():
    cur = connect.cursor()
    query = """SELECT * FROM gashev_yaroshenko.taxi_cars"""
    cur.execute(query)
    res = cur.fetchall()
    return res

@router.post("/cars/create")
async def add_car(car: Cars):
    cur = connect.cursor()
    id = randint(1,99999999)
    query = """INSERT INTO gashev_yaroshenko.taxi_cars(id_car, model, color, car_number, free_status) VALUES (%s, %s, %s, %s, %s);"""
    values = (id, car.model, car.color, car.car_number, car.free_status)
    cur.execute(query, values)
    connect.commit()
    return "200"

@router.get("/cars/{id}")
async def get_id_cars(id: int):
    cur = connect.cursor()
    query = """SELECT * FROM gashev_yaroshenko.taxi_cars WHERE id_car = %s;"""
    cur.execute(query, (id,))
    res = cur.fetchall()
    return res

@router.put("/cars/{id}")
async def change_cars(id: int, car: Cars):
    cur = connect.cursor()
    query = """UPDATE gashev_yaroshenko.taxi_cars SET model = %s, color = %s, car_number = %s, free_status = %s WHERE id_car = %s;"""
    values = (car.model, car.color, car.car_number, car.free_status, id)
    cur.execute(query, values)
    connect.commit()
    return "200"

@router.delete("/cars/{id}")
async def delete_cars(id: int):
    cur = connect.cursor()
    query = """DELETE FROM gashev_yaroshenko.taxi_cars WHERE id_car = %s;"""
    cur.execute(query, (id,))
    connect.commit()
    return "200"

@router.get("/driver/all")
async def get_all_driver():
    cur = connect.cursor()
    query = """SELECT * FROM gashev_yaroshenko.driver;"""
    cur.execute(query)
    res = cur.fetchall()
    return res

@router.get("/driver/{id}")
async def get_id_driver(id: int):
    cur = connect.cursor()
    query = """SELECT * FROM gashev_yaroshenko.driver WHERE driver_id = %s;"""
    cur.execute(query, (id,))
    res = cur.fetchall()
    return res

@router.put("/driver/{id}")
async def change_driver(id: int, driver: Driver):
    cur = connect.cursor()
    query = """UPDATE gashev_yaroshenko.driver SET rating_drive = %s WHERE driver_id = %s;"""
    values = (driver.rating_drive, id)
    cur.execute(query, values)
    connect.commit()
    return "200"

@router.delete("/driver/{id}")
async def delete_driver(id: int):
    cur = connect.cursor()
    query = """DELETE FROM gashev_yaroshenko.driver WHERE driver_id = %s;"""
    cur.execute(query, (id,))
    connect.commit()
    return "200"

@router.post("/passenger/create")
async def add_passenger(passag: Passenger):
    cur = connect.cursor()
    id = randint(1,99999999)
    query = """INSERT INTO gashev_yaroshenko.passag (user_id, rating) VALUES (%s, %s);"""
    values = (id, passag.rating)
    cur.execute(query, values)
    connect.commit()
    return "200"

@router.put("/passenger/{id}")
async def change_passenger(id: int, passag: Passenger):
    cur = connect.cursor()
    query = """UPDATE gashev_yaroshenko.passag SET rating = %s WHERE user_id = %s;"""
    values = (passag.rating, id)
    cur.execute(query, values)
    connect.commit()
    return "200"

@router.post("/order/create")
async def new_order(orders: Orders):
    cur = connect.cursor()
    id = randint(1,99999999)
    query = """INSERT INTO gashev_yaroshenko.orders (order_id, id_car, user_id, driver_id, point_from, point_to, time_of_order, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    values=(id, orders.id_car, orders.user_id, orders.driver_id, orders.point_from, orders.point_to, orders.time_of_order, orders.status)
    cur.execute(query, values)
    connect.commit()
    return "200"

@router.get("/order/all")
async def all_order():
    cur = connect.cursor()
    query = """SELECT * FROM gashev_yaroshenko.orders;"""
    cur.execute(query)
    res = cur.fetchall()
    return res