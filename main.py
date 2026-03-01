from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

# 1. 메인 페이지: 서버 상태 확인
@app.get("/")
def read_root():
    return {
        "status": "Running",
        "server_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "owner": "YS Kim"
    }

# 2. 분석 결과 제공: CES 2026 관련 가상 데이터 (IP/analysis)
@app.get("/analysis")
def get_analysis():
    return {
        "project": "CES 2026 Auto Report",
        "top_keywords": ["AI-Agent", "On-Device LLM", "Spatial Computing"],
        "patent_count": 1250,
        "message": "Analysis completed successfully."
    }

# 3. 개발/디버깅용: 간단한 파라미터 전달 테스트 (IP/dev/{name})
@app.get("/dev/{name}")
def dev_test(name: str):
    return {
        "mode": "Development",
        "greeting": f"Hello {name}, Docker is working perfectly!"
    }