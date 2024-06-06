from Backend.WebSocket import app
# from Backend.Router import app

import logging

logging.getLogger('passlib').setLevel(logging.ERROR)

# (fastAPI) PBL5---Quizit> uvicorn Backend.main:app --host 0.0.0.0 --port 4444
# (fastAPI) PBL5---Quizit> daphne Backend.main:app --bind 0.0.0.0 --port 4444


# MULTIPLE WORKERS
# FOR WSL LINUX
# (fastAPI) PBL5---Quizit> gunicorn Backend.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:4444

# sudo kill -9 $(netstat -ltnp | grep ':4444' | awk '{print $7}' | cut -d'/' -f1)

# Accessing a WSL 2 distribution from your local area network (LAN)
# netsh interface portproxy add v4tov4 listenport=<yourPortToForward> listenaddress=0.0.0.0 connectport=<yourPortToConnectToInWSL> connectaddress=(wsl hostname -I)
# netsh interface portproxy add v4tov4 listenport=4444 listenaddress=0.0.0.0 connectport=4444 connectaddress=172.31.54.89
