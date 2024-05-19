# Use an appropriate base image
FROM --platform=linux/x86_64 python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the entire folder into the container
COPY . /app

# Install any dependencies required by your script
# RUN pip install some-package
RUN pip install -r requirements.txt

# Run the script
CMD ["python", "cron.py"]