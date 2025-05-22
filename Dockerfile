FROM python:3.11-slim

RUN apt-get update && apt-get install -y build-essential git curl && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

# Optional: Automatically build vector DB at build time (comment out if you want manual control)
RUN python vector_builder.py || echo "Index will be rebuilt at runtime if needed"

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
