from Backend.WebSocket import app

import logging

logging.getLogger('passlib').setLevel(logging.ERROR)

# (fastAPI) PBL5---Quizit> uvicorn Backend.main:app --host 0.0.0.0 --port 4444


# MULTIPLE WORKERS
# FOR WSL LINUX
# (fastAPI) PBL5---Quizit> gunicorn Backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:4444
# (fastAPI) PBL5---Quizit> hypercorn Backend.main:app --workers 4 --worker-class uvloop --bind 0.0.0.0:4444
# (fastAPI) PBL5---Quizit> hypercorn Backend.main:app --workers 4 --worker-class trio --bind 0.0.0.0:4444
# (fastAPI) PBL5---Quizit> hypercorn Backend.main:app --workers 4 --worker-class asyncio --bind 0.0.0.0:4444

# Kill the process running on port 4444
# kill -9 $(lsof -t -i:4444)

# Accessing a WSL 2 distribution from your local area network (LAN)
# netsh interface portproxy add v4tov4 listenport=<yourPortToForward> listenaddress=0.0.0.0 connectport=<yourPortToConnectToInWSL> connectaddress=(wsl hostname -I)
# netsh interface portproxy add v4tov4 listenport=4444 listenaddress=0.0.0.0 connectport=4444 connectaddress=172.31.54.89

# disable port forwarding
# netsh interface portproxy delete v4tov4 listenport=4444 listenaddress=0.0.0.0