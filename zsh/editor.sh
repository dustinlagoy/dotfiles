#!/bin/bash
echo "args $@"
sleep 1
item=$1
docker run --rm -it --user $UID:$(id -g) -e TERM -e COLORTERM=truecolor \
  -e DISPLAY=$DISPLAY --net=host -v $HOME/.Xauthority:/root/.Xauthority \
  -v $item:$item \
  git-collab.nrc-cnrc.gc.ca:4000/haa/draosw/proto/helix-image/base:latest \
  hx + $item
