# Base this docker container off the official golang docker image.
# Docker containers inherit everything from their base.
FROM python:3.8

RUN apt-get update
RUN apt-get install -y nodejs
RUN apt-get install -y npm
RUN npm install npm@latest -g

RUN pip install awscli
RUN pip install boto3
RUN npm install -g serverless
RUN apt-get install -y gnupg

# RUN pip install numpy scipy matplotlib ipython jupyter pandas sympy nose
# RUN pip install -U scikit-learn
# RUN pip install nltk
# RUN pip install --upgrade PILLOW
# RUN pip install kaggle --upgrade
# RUN pip install seaborn
# RUN pip install biopython


# RUN rm /usr/bin/python
# RUN ln -s /usr/local/bin/python /usr/bin/python

RUN mkdir -p /var/project
WORKDIR /var/project

ADD . /var/project


EXPOSE 3000
# ENTRYPOINT ["tail", "-f", "/dev/null"]