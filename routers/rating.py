from fastapi import APIRouter, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder 

from service.rating import RatingService
from schemas.rating import Rating
from config.database import Session

rating_router = APIRouter()



@rating_router.get('/rating', tags=['rating'], status_code=200)
def get_router():
    return JSONResponse(content={"message":"rating created successfully"})

@rating_router.post('/rating', tags=['rating'], status_code=201)
def create_rating(rating:Rating):
    db = Session()
    RatingService(db).create_rating(rating)
    return JSONResponse(content={"message":"rating created successfully", "status_code" : 201})

@rating_router.get('/rating_for_id', tags=['rating'], status_code=200)
def get_rating_id(rating:Rating):
    db = Session()
    RatingService(db).get_rating(rating)
    return JSONResponse(content={"message": "rating create successfully", "status_code": 201})

@rating_router.put('/rating{id}', tags=['rating'])
def update_rating(id:int,data:Rating):
    db = Session()
    result = RatingService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message" : "rating don´t found", "status code":404})
    RatingService(db).update_rating(data)
    return JSONResponse(content={"message": "rating update successfully", "status_code": 202}, status_code=202)

@rating_router.delete('/rating{id}', tags=['rating'])
def delete_rating(id:int):
    db = Session()
    result = RatingService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message" : "rating don´t found", "status code":404})
    RatingService(db).delete_rating(id)
    return JSONResponse(content={"message": "rating delete successfully", "status_code": 200}, status_code=200)