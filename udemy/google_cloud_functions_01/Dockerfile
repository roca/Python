# Base this docker container off the official golang docker image.
# Docker containers inherit everything from their base.
FROM python:3.8

RUN apt-get update

RUN apt-get install -y gnupg

RUN mkdir -p /var/project
WORKDIR /var/project

ADD . /var/project

# RUN pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
# RUN pip install -U scikit-learn
# RUN pip install nltk
# RUN pip install --upgrade PILLOW
# RUN pip install kaggle --upgrade
# RUN pip install seaborn
# RUN pip install biopython
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


RUN rm /usr/bin/python
RUN ln -s /usr/local/bin/python /usr/bin/python

RUN export PATH=/var/project/bin:$PATH

EXPOSE 3000