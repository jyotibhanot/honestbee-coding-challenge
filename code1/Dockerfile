# Base Ubuntu image with base packages
FROM jyotibhanot30/ubuntu-base:latest

# Install curl
RUN apt-get install curl -y

# Adding to $PATH
WORKDIR /usr/local/bin

# Copy python code
COPY git-info.py .

# Running python code
CMD ["git-info.py"]
