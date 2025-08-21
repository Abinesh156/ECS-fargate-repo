# Use a lightweight version of Python
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Python application file into the container
COPY hello.py .

# Run the Python script
CMD ["python", "hello.py"]
