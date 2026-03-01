FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn

COPY main.py .

# main:app 으로 정확히 타겟팅!
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]