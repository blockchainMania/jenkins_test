from fastapi import FastAPI
from datetime import datetime

app = FastAPI()#선언

# 1. 메인 페이지: 서버 상태 확인
@app.get("/")
def read_root():
    return {
        "status": "Running",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "owner": "YS Kim"
    }

@app.get("/test")
def read_test():
    return {
        "status": "Running",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "owner": "DH Kim"
    }