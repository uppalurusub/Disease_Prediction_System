import requests
from utils.config import PREDICT_ENDPOINT
def predict(data):
    try:
        r=requests.post(PREDICT_ENDPOINT,json=data,timeout=60)
        r.raise_for_status()
        return {"success":True,"data":r.json()}
    except Exception as ex:
        return {"success":False,"message":str(ex)}
