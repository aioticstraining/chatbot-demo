# Use the latest Python slim image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file first for dependency installation
COPY requirements.txt .

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set the command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]

