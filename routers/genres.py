from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse

genrens_router = APIRouter()

@genrens_router.get('/genres', tags=['genres'], status_code=200)
def get_router():
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')

@genrens_router.get('/genres', tags=['genres'], status_code=200)
def get_router():
    return JSONResponse(content={"message":"genre created successfully"})

@genrens_router.post('/genres', tags='genres', status_code=201)
def create_genres():
    return JSONResponse(content={"message":"genre created successfully"})