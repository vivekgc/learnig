FROM ubuntu:14.04
LABEL name="vivek-test"
LABEL email="admin@vivektest.com"
ENV NAME vivek
ENV PASS password
RUN pwd > /tmp/1stpwd.txt
RUN cd /tmp
RUN pwd>/tmp/2ndpwd.txt
WORKDIR /tmp
RUN pwd>/tmp/3rdpwd.txt
RUN apt-get update && apt-get install -y openssh-server && apt-get install -y python
RUN useradd -d /home/gaurav -g root -G sudo -m -p $(echo "$PASS" | openssl passwd -1 -stdin) $NAME
RUN whoami>/tmp/1stwhoami.txt
USER $NAME
RUN whoami>/tmp/2ndwhoami.txt
RUN mkdir -p /tmp/project
ADD testproject /tmp/project