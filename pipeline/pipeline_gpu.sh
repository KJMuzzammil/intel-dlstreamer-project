gst-launch-1.0 -v \
filesrc location=${VIDEO_EXAMPLE} ! decodebin ! videoconvert ! \
gvadetect model=${DETECTION_MODEL} model_proc=${DETECTION_MODEL_PROC} device=GPU inference-interval=10 ! queue ! \
gvatrack tracking-type=short-term ! queue ! \
gvaclassify model=${CLASSIFICATION_MODEL} model_proc=${CLASSIFICATION_MODEL_PROC} device=GPU reclassify-interval=10 ! queue ! \
gvawatermark ! videoconvert ! \
fpsdisplaysink video-sink=ximagesink sync=false
