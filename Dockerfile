# Use Python slim base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install Roboto SDK
RUN pip install --no-cache-dir roboto

# Copy the dataset creation script
COPY create_dataset.py .
COPY test.ulg . 

# Run the script when container starts
CMD ["python", "create_dataset.py"]
