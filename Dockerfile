# Use Python 3.9 slim image as a base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the application code into the container
COPY . /app

# Install the necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 for the container
EXPOSE 80

# Use Gunicorn to serve the app on port 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
