import fastapi.middleware.cors
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from Backend.Router.auth_router import auth_router
from Backend.Router.teacher_router import teacher_router
from Backend.Router.student_router import student_router
from Backend.Router.group_test_router import group_test_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="Backend/Static"), name="static")

app.add_middleware(
    fastapi.middleware.cors.CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(teacher_router)
app.include_router(student_router)
app.include_router(group_test_router)

import logging

logging.getLogger('passlib').setLevel(logging.ERROR)

# (fastAPI) PBL5---Quizit> uvicorn Backend.main:app --port 4444
# (fastAPI) PBL5---Quizit> hypercorn Backend.main:app --worker-class trio --workers 4 --bind 0.0.0.0:4444
