from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse

genrens_router = APIRouter()

#Funcion to check the router
@genrens_router.get('/genres', tags=['genres'], status_code=200)
def get_router():
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')

#funcion que trae todos los generos que esta en servicios 
@genrens_router.get('/genres', tags=['genres'], status_code=200)
def get_router():
    return JSONResponse(content={"message":"genre created successfully"})

#llamar una funcion que va a estar en el servicios 
@genrens_router.post('/genres', tags='genres', status_code=201)
def create_genres():
    return JSONResponse(content={"message":"genre created successfully"})

#creamos un get que trae un solo genero por id
@genrens_router.get('/genres/{genres_id}', tags=['genres'], status_code=200)
def get_genres(genres_id: int):
    genre = genrens_router.get_genre(genres_id)
    return genre

# para el genres delete debemos verificar que el id existe y despues ese genero lo eliminamos
@genrens_router.detele('/genres/{genres_id}', tags=['genres'], status_code=204)
def detele_genre_by_id(genres_id: int):
    return JSONResponse (content= {"message": f"Genero con ID {genres_id} Elimiado correctamente"})
