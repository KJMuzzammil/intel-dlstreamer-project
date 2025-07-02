#!/bin/bash
docker run -it --rm \
  --device=/dev/dri \
  --env DISPLAY=$DISPLAY \
  --volume=/tmp/.X11-unix:/tmp/.X11-unix \
  --volume=$HOME/.Xauthority:/root/.Xauthority \
  --volume=$HOME/intel/models:/home/dlstreamer/models \
  --env MODELS_PATH=/home/dlstreamer/models \
  --volume=$HOME/dlstreamer_input:/videos \
  intel/dlstreamer:latest
