# Dockerfile
FROM python:3.10

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY wallet_api /app/wallet_api

# Command to run the application
CMD ["gunicorn", "wallet_api.wsgi:application", "--bind", "0.0.0.0:8000"]
