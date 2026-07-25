# Stage 1: Build & Dependency Stage
FROM python:3.12-slim AS builder

WORKDIR /app

# Install dependencies into wheels cache
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Final Runtime Stage
FROM python:3.12-slim AS runner

WORKDIR /app

# Create non-root system user
RUN groupadd -r appgroup && useradd -r -g appgroup -s /sbin/nologin appuser

# Copy installed packages from builder stage
COPY --from=builder /root/.local /home/appuser/.local
COPY app /app/app

# Set ownership to non-root user
RUN chown -R appuser:appgroup /app

# Configure environment variables
ENV PATH=/home/appuser/.local/bin:$PATH \
    PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]