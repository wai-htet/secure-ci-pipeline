# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY . .

# Install dependencies
RUN pip install flask

# Expose port
EXPOSE 5000

# Start the app
CMD ["python", "app.py"]
