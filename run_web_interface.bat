@echo off
echo Starting DDR Generation Web Interface...
echo.
echo Opening browser at http://localhost:8501
echo.
echo Press Ctrl+C to stop the server
echo.
call venv\Scripts\activate.bat
streamlit run app.py
