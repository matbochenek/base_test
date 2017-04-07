FROM kaixhin/vnc

# Getting base image from https://hub.docker.com/r/kaixhin/vnc/ 
# This driver is for firefox. Get it from here: https://github.com/mozilla/geckodriver/releases
COPY geckodriver-v0.14.0-linux64.tar.gz /usr/local/bin/

WORKDIR /usr/local/bin
RUN tar -xvf geckodriver-v0.14.0-linux64.tar.gz
RUN rm -rf *.gz

WORKDIR /root
COPY test /root/test



RUN apt-get update && apt-get install -y python-pip \
                       xvfb \
                       python-dev \
                       build-essential \
                       libffi-dev 
RUN pip install selenium
RUN pip install pyvirtualdisplay selenium
RUN pip install pytest
RUN pip install appdirs
