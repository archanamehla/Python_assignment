# Use the official Python image from the Docker Hub
FROM python:3

# Set the working directory in the container
WORKDIR /app

COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt

# Copy the entire local directory into the container
COPY . .

# Command to run your Python application
CMD [ "python", "./app/main.py" ]
