
#!/bin/bash
export XHOST_IP=`ifconfig en$1 | grep inet | awk '$1=="inet" {print $2}'`
echo $XHOST_IP
xhost + $XHOST_IP
docker-compose up
