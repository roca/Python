
#!/bin/bash
export XHOST_IP=`ifconfig en0 | grep inet | awk '$1=="inet" {print $2}'`
xhost + $XHOST_IP
docker-compose up
