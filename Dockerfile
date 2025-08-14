FROM python:3.13.0-slim

WORKDIR /app

# Create user first
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "10001" \
    appuser

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN python -m pip install -r requirements.txt

# Copy ALL project files (this is the key!)
COPY . .

# NOW run migrations (after files are copied)
RUN mkdir -p /app/db
RUN python manage.py makemigrations
RUN python manage.py migrate

# Make database writable
RUN chmod 777 /app
RUN chmod 777 /app/db.sqlite3 || true

# Switch to non-root user
USER appuser

# Expose port
EXPOSE 8000

# Start server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]