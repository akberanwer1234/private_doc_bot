# Use Python 3.10 as the base image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the entire PrivateDocBot directory into the container
COPY PrivateDocBot /app

# Copy the requirements file
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the default Chainlit port (8501)
EXPOSE 8000

# Run the Chainlit application
CMD ["chainlit", "run", "main.py", "-w"]