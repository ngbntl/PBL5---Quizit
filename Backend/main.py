from Backend.Router import app

import logging
logging.getLogger('passlib').setLevel(logging.ERROR)



# (fastAPI) PBL5---Quizit> uvicorn Backend.main:app --port 4444
# (fastAPI) PBL5---Quizit> hypercorn Backend.main:app --worker-class trio --workers 4 --bind 0.0.0.0:4444
