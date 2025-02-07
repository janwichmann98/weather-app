# Use an official Python runtime as a parent image.
FROM python:3.9-slim

# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container.
WORKDIR /app

# Copy the requirements file into the container and install dependencies.
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the entire project into the container.
COPY . /app/

# Expose port 5000 for the Flask app.
EXPOSE 5000

# Set the environment variable to tell Flask which application to run.
ENV FLASK_APP=app.py

# Run the application.
CMD ["flask", "run", "--host=0.0.0.0"]
