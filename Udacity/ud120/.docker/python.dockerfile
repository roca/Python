# Base this docker container off the official golang docker image.
# Docker containers inherit everything from their base.
FROM python:2.7

RUN pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
RUN pip install -U scikit-learn
RUN pip install nltk
RUN pip install --upgrade PILLOW
RUN rm /usr/bin/python
RUN ln -s /usr/local/bin/python /usr/bin/python
# Create a directory inside the container to store all our application and then make it the working directory.
RUN mkdir -p /var/Udacity/ud120
WORKDIR /var/Udacity/ud120
# Copy the example-app directory (where the Dockerfile lives) into the container.
ADD . /var/Udacity/ud120
#ENV ip `$(ifconfig en0 | grep inet | awk '$1=="inet" {print $2}')`
EXPOSE 3000
ENTRYPOINT ["tail", "-f", "/dev/null"]