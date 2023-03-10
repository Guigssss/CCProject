# Use an official Python 3?8 image as a parent image
FROM python:3.8
# Set the working directory to /app
WORKDIR /app
# Copy the current directory (on the host machine) contents into the container at /app
COPY . /app
# Install packages specified in requirements.txt and we don't cache the downloaded packages
RUN pip install --no-cache-dir -r requirements.txt
# Make port 5001 available to the world outside this container (so we can map it to our pc after ine the docker-compose.yml file)
EXPOSE 5001
# Run app.py when the container launches
CMD ["python", "app.py"]
