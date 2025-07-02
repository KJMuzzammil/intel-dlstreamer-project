# Intel DL Streamer Project – Real-Time Object Detection & Scalability

## Overview

This project demonstrates real-time video analytics using Intel® DL Streamer with OpenVINO™ on Intel CPU and GPU. It implements a pipeline for object detection, decoding, and classification across multiple video streams and benchmarks scalability and performance.

## Repository Structure
intel-dlstreamer-project/
├── dlstreamer_input/ # Test videos and live_dashboard.py (Python dashboard)
├── camera1_logs/ # JSON output logs from camera 1 stream
├── screenshots/ # System info, FPS, htop, dashboard screenshots
├── report/ # Final approved project report (PDF)
├── test_videos/ # Sample test videos (files <100 MB)
├── README.md # This file


## Models Used

- **person-vehicle-bike-detection-2004** (object detection)
- **person-attributes-recognition-crossroad-0230** (classification)
  
*All models are standard OpenVINO pre-trained models available [here](https://github.com/openvinotoolkit/open_model_zoo). Models are **not included** in this repo due to size and licensing.*

## Prerequisites

- Linux OS with Docker installed
- Intel DL Streamer Docker image ([https://dlstreamer.github.io/](https://dlstreamer.github.io/))
- Python 3 environment for running dashboard

## How to Run

1. Start Intel DL Streamer Docker container.

2. Download and export required models inside the container.

3. Run the pipeline (example for CPU/GPU):

   gst-launch-1.0 -v \
     filesrc location=/path/to/test_video.mp4 ! decodebin ! videoconvert ! \
     gvadetect model=person-vehicle-bike-detection-2004.xml device=CPU ! gvatrack ! \
     gvaclassify model=person-attributes-recognition-crossroad-0230.xml device=CPU ! \
     gvawatermark ! videoconvert ! fpsdisplaysink video-sink=ximagesink sync=false'''

4.Run the dashboard for real-time analytics:
   
    python3 dlstreamer_input/live_dashboard.py

Notes
:
--Models are not pushed to GitHub due to size and licensing. Download from OpenVINO model zoo as instructed.

--Test videos are limited to <100 MB due to GitHub constraints.

--Report is included in /report/final_report.pdf.

--System tested on Intel Core i3-8100 CPU and UHD Graphics 630 GPU.

