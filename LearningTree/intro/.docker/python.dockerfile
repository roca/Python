# Base this docker container off the official golang docker image.
# Docker containers inherit everything from their base.
FROM python:3.6.4

RUN pip install --upgrade pip
RUN pip install psycopg2

RUN rm /usr/bin/python
RUN ln -s /usr/local/bin/python /usr/bin/python
# Create a directory inside the container to store all our application and then make it the working directory.
RUN mkdir -p /var/LearningTree/intro
WORKDIR /var/LearningTree/intro
# Copy the example-app directory (where the Dockerfile lives) into the container.
ADD . /var/LearningTree/intro
#ENV ip `$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')`
EXPOSE 3000
ENTRYPOINT ["tail", "-f", "/dev/null"]