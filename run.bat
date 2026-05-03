@echo off
echo Starting FastAPI server on http://localhost:8000...
py -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
pause