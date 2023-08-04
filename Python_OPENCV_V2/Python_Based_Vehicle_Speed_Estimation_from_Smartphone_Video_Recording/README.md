# Vehicle Speed Estimation from Video using Object Detection and Kalman Filtering

This project is an implementation of a vehicle speed estimation system using computer vision techniques. The system can estimate the speed of vehicles in a video by detecting and tracking them using object detection and Kalman filtering.
https://github.com/Isdinval/DataScience_Projects/assets/34789438/444f749b-1a78-4c0e-8e35-8383e96d1be0

## Features:

* Object Detection with YOLO: The system uses YOLO (You Only Look Once), a powerful object detection algorithm, to detect vehicles in each frame of the input video.
* Kalman Filtering for Tracking: Detected vehicles' positions are tracked over time using Kalman filters, which provide accurate and smooth tracking results.
* Line-based Speed Estimation: The system estimates the speed of vehicles by analyzing their time taken to cross two user-defined lines in the video frame.
* Real-world Speed Conversion: The estimated speeds are converted from pixel-based measurements to real-world units (e.g., km/h) using a pixel scale and time scale.

## How to Use:

Clone the repository to your local machine.
Install the required dependencies, including OpenCV, pandas, numpy, and ultralytics (YOLO).
Download a pre-trained YOLO model (e.g., yolov8s.pt) and place it in the project folder.
Update the video path variable with the path to your input video.
Define the two lines in the video frame where the vehicles' speeds will be estimated.
Run the script using Python
The script will display the video with tracked vehicles and speed estimation information. It will also save an annotated output video with tracked objects and estimated speeds.

## Requirements:
Python 3.7 or higher
OpenCV
pandas
numpy
ultralytics (YOLO)

## Sample Video:
A sample video is included in the repository to test the system. You can use it to see how the speed estimation works.

#Note:
Please make sure to comply with the terms of use of any pre-trained YOLO models you use and respect the licenses of the dependencies.



