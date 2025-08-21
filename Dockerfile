# Use a lightweight Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Python application to the container
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port 80 for the application to be accessed
EXPOSE 80

# Command to run the Python application
CMD ["python", "app.py"]
