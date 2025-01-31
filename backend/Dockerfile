# Backend Dockerfile (backend/Dockerfile)

# ---- Build Backend ----
    FROM python:3.9 AS backend

    WORKDIR /app
    
    # Copy requirements.txt and install Python dependencies
    COPY backend/requirements.txt ./
    RUN pip install --no-cache-dir -r requirements.txt
    
    # Copy the rest of the backend source code
    COPY backend/ .
    
    # Expose the port the backend will run on
    EXPOSE 5000
    
    # Command to start the backend server (e.g., using Uvicorn)
    CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
    