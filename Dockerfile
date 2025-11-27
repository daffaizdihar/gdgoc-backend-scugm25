FROM python:3.10-slim

WORKDIR /app

# Install system dependencies (psycopg might need this)
RUN apt-get update && apt-get install -y build-essential

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose FastAPI port
EXPOSE 8080

# Run server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
