#!/bin/bash
item=$(readlink -m $1)
dir=$(dirname $item)
base=$(basename $item)
docker run --rm -it --user $UID:$(id -g) -e TERM -e COLORTERM=truecolor \
  -e DISPLAY=$DISPLAY --net=host -v $HOME/.Xauthority:/root/.Xauthority \
  -v $dir:/work -w /work \
  git-collab.nrc-cnrc.gc.ca:4000/haa/draosw/proto/helix-image/base:latest \
  hx + $base
