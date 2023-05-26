from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse

genrens_router = APIRouter()

@genrens_router.get('/genres', tags=['genres'], status_code=200)
def get_router():
    return HTMLResponse('<h1>Hola desde la ruta de genres</h1>')