# image is based on ubuntu 16.04
# allows us to do headless chrome selenium testing
FROM selenium/standalone-chrome
MAINTAINER Mike Dawson-Haggerty <mikedh@kerfed.com>

# packages required to build gpcio
#ENV GOOGLE_BUILD="gcc linux-headers build-base libc-dev make musl-dev"

# get pip and python3
RUN sudo apt-get update && \
    sudo apt-get install -y python3 python3-pip && \
    sudo apt-get clean && \
    sudo rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
COPY requirements.txt /tmp/
RUN /usr/bin/pip3 install -r /tmp/requirements.txt

COPY . /opt/monitor
RUN sudo chown seluser: -R /opt/monitor
WORKDIR /opt/monitor

#-u is unbuffered, otherwise prints are eaten
CMD ["python3", "-u", "monitor.py"]
