FROM continuumio/anaconda:latest

RUN /opt/conda/bin/conda install jupyter -y --quiet 
RUN mkdir -p /opt/notebooks 

WORKDIR /opt/notebooks 

EXPOSE 8888
# ENTRYPOINT ["tail", "-f", "/dev/null"]