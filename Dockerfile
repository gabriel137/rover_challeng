# Use the official Python image as base
FROM python:3.10-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the project dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container
COPY . .

# Set the environment variable to run the app
ENV PYTHONPATH=/app

# Set the default command to run when the container starts
CMD ["python",  "-i", "app/main.py"]
