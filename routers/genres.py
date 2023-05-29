from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder


from service.genres import GenresService
from schemas.genres import Genres
from config.database import Session

genres_router = APIRouter()

#Funcion to check the router
@genres_router.get('/genres', tags=['genres'], status_code=200)
def get_router():
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')


#funcion que trae todos los generos que esta en servicios 
@genres_router.get('/genres', tags=['genres'], status_code=200)
def get_router(id:int):
    return JSONResponse(content={"message":"genre created successfully"})


#llamar una funcion que va a estar en el servicios 
# @genres_router.post('/genres', tags='genres', status_code=201)
# def create_genres():
#     return JSONResponse(content={"message":"genre created successfully"})

@genres_router.post('/genres', tags=['genres'], status_code=201)
def create_genres(genres:Genres):
    db = Session()
    GenresService(db).create_genre(genres)
    return JSONResponse(content={"message":"genre created successfully", "status_code" : 201})

#creamos un get que trae un solo genero por id
@genres_router.get('/genres_for_id', tags=['genres'], status_code=200)
def get_genres_id(genres:Genres):
    db = Session()
    
    GenresService(db).get_genres(genres)
    return JSONResponse(content={"message": "genre create successfully", "status_code": 201})


# para el genres delete debemos verificar que el id existe y despues ese genero lo eliminamos
# @genrens_router.detele('/genres/{genres_id}', tags=['genres'], status_code=204)
# def detele_genre_by_id(genres_id: int):
#     return JSONResponse (content= {"message": f"Genero con ID {genres_id} Elimiado correctamente"})
