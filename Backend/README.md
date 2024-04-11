1. <code>pip install -r requirements.txt</code>
2. * <code>PBL5---Quizit> uvicorn Backend.main:app --port 4444</code>
   * <code>PBL5---Quizit> hypercorn Backend.main:app --worker-class trio --workers 4 --bind localhost:4444</code>
