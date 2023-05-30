from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse



from service.reviewer import ReviewerService
from schemas.reviewers import Reviewers
from config.database import Session

reviewer_router = APIRouter()

@reviewer_router.get("/reviewer",tags=["genres"],status_code=200)
def reviewer_router():
    return HTMLResponse("<h1>Hola desde la ruta reviewer</h1>")


@reviewer_router.get("/reviewer",tags=["reviewer"],status_code=200)
def reviewer_router(id:int):
    return JSONResponse(content={"message":"genre created successfully"})


@reviewer_router.post("/reviewer",tags=["reviewer"], status_code=201)
def create_reviewer(reviewer:Reviewers):
    db = Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(content={"message":"reviewer create successfully","status_code":201})


@reviewer_router.get("/reviewer_for_id", tags=["reviewer"],status_code=200)
def get_reviewer_id(reviewer:Reviewers):
    db = Session()
    ReviewerService(db).get_reviewer(reviewer)
    return JSONResponse(content={"message":"reviewer create successfully","status_code":201})


@reviewer_router.put("/reviewer{id}",tags = ["genres"])
def update_reviewer(id:int,data:Reviewers):
    db = Session()
    result = ReviewerService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message" : "reviewer don´t found","status_code":404})
    ReviewerService(db).update_reviewer(data)
    return JSONResponse(content={"message": "reviewer update successfully","status_code":202},status_code=202)


@reviewer_router.delete("/reviewer{id}",tags = ["reviewer"])
def delete_reviewer(id:int):
    db = Session()
    result = ReviewerService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message": "reviewer don't found","status_code":404})
    ReviewerService(db).delete_reviewer(id)
    return JSONResponse(content={"message":"reviewer delete successfully", "status_code":200},status_code=200)
    