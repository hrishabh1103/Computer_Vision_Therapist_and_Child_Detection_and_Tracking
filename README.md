# Person Detector and Tracker for Autism Spectrum Disorder (ASD) Analysis
This project implements a person detection and tracking system to identify and monitor children with Autism Spectrum Disorder (ASD) and therapists in video footage. The solution assigns unique IDs to each detected person, tracks their movements throughout the video, handles re-entries, and manages occlusions to ensure continuous tracking.

# Table of Contents
Introduction
Features
Requirements
Installation
Usage
Output
Methodology
Customization
License

# Introduction
The primary objective of this project is to analyze the interaction between children with ASD and therapists by tracking their movements in long-duration videos. The tracking information can be used to study behavioral patterns, emotions, and engagement levels, which are crucial for developing effective treatment plans.

# Features
Person Detection: Utilizes YOLOv5 for accurate detection of persons in the video.
Unique ID Assignment: Assigns unique IDs to detected persons and tracks them across frames.
Re-entry Tracking: Handles cases where persons leave and re-enter the frame.
Post-Occlusion Tracking: Re-tracks persons after partial or complete occlusion.
Filtered Tracking: Focuses on tracking only the relevant individuals (children and therapists) by filtering out other objects.

# Requirements
The project is implemented in Python and requires the following libraries:

Python 3.8+
PyTorch
OpenCV
SORT (Simple Online and Realtime Tracking)
Numpy

# You can install the required dependencies using Conda and pip:
conda install -c conda-forge opencv
pip install torch torchvision sort numpy

# Installation
1. Clone the repository:
git clone https://github.com/hrishabh1103/Computer_Vision_Therapist_and_Child_Detection_and_Tracking.git
cd Computer_Vision_Therapist_and_Child_Detection_and_Tracking

2.Install the required Python packages as mentioned in the Requirements section.

# Usage
1.Place your input video in the project directory or specify its path in the script.
2.Run the person_tracker.py script:
python person_tracker.py
3. The script will process the video and save the output with detected persons and their unique IDs in the specified output path.

# Output
The script generates an output video with the following features:
1. Bounding boxes around detected children and therapists.
2. Unique ID labels overlaid on the video for each tracked individual.
3. Continuous tracking across frames, including re-entries and post-occlusion.

# Methodology
Model Selection: We use YOLOv5, a state-of-the-art object detection model pre-trained on the COCO dataset, to detect persons in each frame.
Tracking Algorithm: The SORT algorithm is used to assign unique IDs to detected persons and maintain these IDs across frames.
Filtering: The detection results are filtered to focus exclusively on "persons" (children and therapists), ignoring other objects in the scene.
Size Filtering (Optional): A size threshold is used to differentiate between children and therapists, though this can be customized based on the video characteristics.

# Customization
Threshold Adjustment: You can adjust the size threshold or modify the detection logic in person_tracker.py to better distinguish between children and therapists.
Model Fine-Tuning: If needed, you can fine-tune a detection model on a dataset that includes distinct labels for children and adults to improve accuracy.

# License
This project is licensed under the MIT License. See the LICENSE file for details.


