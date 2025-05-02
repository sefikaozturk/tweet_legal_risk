FROM python:3.11-slim

WORKDIR /app

# Install build tools for any extensions
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential libssl-dev libffi-dev python3-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy & install Python deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
