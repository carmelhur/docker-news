FROM python:3.11-slim

WORKDIR /app

# Install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# App files
COPY config.py run_processor.py ./

# Run
CMD ["uvicorn", "run_processor:svc", "--host", "0.0.0.0", "--port", "8002"]
