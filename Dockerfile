# image is based on Ubuntu 16.04
# has headless Chrome set up
FROM selenium/standalone-chrome:3.141.59
MAINTAINER Mike Dawson-Haggerty <mikedh@kerfed.com>

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

# -u is unbuffered, otherwise prints are eaten
CMD ["python3", "-u", "monitor.py"]
