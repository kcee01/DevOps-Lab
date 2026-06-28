# Use a lightweight Python 3.12 base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only the requirements file first (for better Docker layer caching)
COPY requirements.txt .

# Install Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 5000 so the Flask app can be accessed outside the container
EXPOSE 5000

# Default command to run the application
CMD ["python3", "app.py"]
