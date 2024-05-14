# from Backend.WebSocket import app
from Backend.Router import app

import logging

logging.getLogger('passlib').setLevel(logging.ERROR)

# (fastAPI) PBL5---Quizit> uvicorn Backend.main:app --port 4444
# (fastAPI) PBL5---Quizit> daphne Backend.main:app --bind 0.0.0.0 --port 4444
