FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the necessary port
EXPOSE 5000

# Command to run the app
CMD ["python", "sevanbot.py"]


