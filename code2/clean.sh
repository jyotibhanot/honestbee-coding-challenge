#! /usr/bin/env bash
# Description: Script to cleanup all containers and images.
# Author: jyoti.bhanot
docker ps -a | awk '{print $1}' | xargs docker rm -f
docker images | awk '{print $3}' | xargs docker rmi
docker ps -a
docker images
