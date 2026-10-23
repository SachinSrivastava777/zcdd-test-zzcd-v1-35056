FROM python:3.11-slim

WORKDIR /app

# System deps some python packages need to build (kept minimal)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt gunicorn

# Non-root user for sandboxing
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

ENV PORT=5000
EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
