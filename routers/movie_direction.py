from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.encoders import jsonable_encoder
from service.movie_direction import MovieDirectionService 
from config.database import Session
from schemas.movie_direction import MovieDirection

movie_direction_router = APIRouter()

@movie_direction_router.get('/movie_direction',tags=['movie_direction'],status_code=200)
def get_moviedirection():
    db = Session()
    result = MovieDirectionService(db).get_moviedirection()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_direction_router.post('/movie_direction',tags=['movie_direction'],status_code=201)
def create_moviedirection(movie_direction:MovieDirection):
     db=Session()
     MovieDirectionService(db).create_(movie_direction)
     return JSONResponse(content={"message":"movie direction create successfully",'status_code':201})


@movie_direction_router.get('/movie_direction_for_id',tags=['movie_direction'],status_code=200)
def det_moviedirection_for_id(id:int):
     db = Session()
     result =MovieDirectionService(db).get_for_id(id)
     return JSONResponse(content=jsonable_encoder(result),status_code=200)

@movie_direction_router.put('/movie_direction{id}',tags=['movie_direction'])
def update_moviedirection(id:int,data:MovieDirection):
     db = Session()
     result = MovieDirectionService(db).get_for_id(id)
     if not result :
         return JSONResponse(content={"message":"movie direction don't found","status_code":404})    
     MovieDirectionService(db).update_moviedirection(data)
     return JSONResponse(content={"message":"movie direction update succesfully","satus_code":202},status_code=202)

@movie_direction_router.delete('/movie_direction{id}',tags=['movie_direction'])
def delete_moviedirection(id:int):
     db = Session()
     result = MovieDirectionService(db).get_for_id(id)
     if not result :
         return JSONResponse(content={"message":"movie direction don't found","status_code":404})
     MovieDirectionService(db).delete_director(id)
     return JSONResponse(content={"message":"movie direction delete succefully",'status_code':200},status_code=200)