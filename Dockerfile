# Use a lightweight version of Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python application file into the container
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port 80 to the container
EXPOSE 80

# Run the Python script
CMD ["python", "hello.py"]
