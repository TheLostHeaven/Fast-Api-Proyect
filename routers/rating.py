from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponses, JSONResponses
from fastapi.encoders import jsonable_encoder 

from service.rating import ratingService
from schemas.rating import rating
from config.database import Session

rating_router = APIRouter()

@rating_router.get('/rating', tags=['rating'], status_code=200)
def get_router():
    return HTMLResponses('<h1>Hola desde la ruta de rating</h1>')

@rating_router.get('/rating', tags=['rating'], status_code=200)
def get_router(id:int):
    return JSONResponses(content={"message":"rating created successfully"})

@rating_router.post('/rating', tags=['rating'], status_code=201)
def create_rating(rating:rating):
    db = Session()
    ratingService(db).create_rating(rating)
    return JSONResponses(content={"message":"rating created successfully", "status_code" : 201})

@rating_router.get('/rating_for_id', tags=['rating'], status_code=200)
def get_rating_id(rating:rating):
    db = Session()
    ratingService(db).get_rating(rating)
    return JSONResponses(content={"message": "rating create successfully", "status_code": 201})

@rating_router.put('/rating{id}', tags=['rating'])
def update_rating(id:int,data:rating):
    db = Session()
    result = ratingService(db).get_for_id(id)
    if not result:
        return JSONResponses(content={"message" : "rating don´t found", "status code":404})
    ratingService(db).update_rating(data)
    return JSONResponses(content={"message": "rating update successfully", "status_code": 202}, status_code=202)

@rating_router.delete('/rating{id}', tags=['rating'])
def delete_rating(id:int):
    db = Session()
    result = ratingService(db).get_for_id(id)
    if not result:
        return JSONResponses(content={"message" : "rating don´t found", "status code":404})
    ratingService(db).delete_rating(id)
    return JSONResponses(content={"message": "rating delete successfully", "status_code": 200}, status_code=200)