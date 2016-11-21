#!/usr/bin/env bash
docker rm -f order-tracker
docker build -t rfpt/order-tracker .

rc=$?;
if [[ $rc != 0 ]];
then
exit $rc;
fi


if [[ $HOSTNAME == "ubuntu" ]];
then
    docker run -d --name order-tracker --restart always -p 80:80 rfpt/order-tracker
else
    docker run -d --name order-tracker --restart always -p 8080:80 rfpt/order-tracker
fi

# install:
# apt-get -y install docker.io
# ln -sf /usr/bin/docker.io /usr/local/bin/docker
# sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io
# update-rc.d docker.io defaults
