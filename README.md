# Person Detector and Tracker for Autism Spectrum Disorder (ASD) Analysis
This project implements a person detection and tracking system to identify and monitor children with Autism Spectrum Disorder (ASD) and therapists in video footage. The solution assigns unique IDs to each detected person, tracks their movements throughout the video, handles re-entries, and manages occlusions to ensure continuous tracking.

# Analyzing Model Predictions

# Overview
The goal of this project is to detect and track persons (children and therapists) in video footage to analyze their behaviors, emotions, and engagement levels, particularly in the context of Autism Spectrum Disorder (ASD). The pipeline involves using YOLOv5 for detection and SORT for tracking, with a focus on assigning unique IDs, handling re-entries, and managing occlusions.

# Step-by-Step Breakdown

# Loading the YOLOv5 Model:
We utilize the YOLOv5 model from Ultralytics, which is pre-trained on the COCO dataset. This model is highly efficient for real-time object detection and is capable of identifying 80 different classes, including "person."
The model is loaded using the PyTorch hub.load function, which allows us to easily access and use pre-trained models.

# Video Capture:
The input video is loaded using OpenCV's cv2.VideoCapture method. This allows us to read the video frame by frame, which is necessary for applying detection and tracking in real-time.

# Detection:
For each frame, the YOLOv5 model processes the image and outputs bounding boxes, confidence scores, and class labels for detected objects.
Since our focus is on persons (children and therapists), we filter out all other detections by checking if the class ID corresponds to "person" (class ID 0 in the COCO dataset).

# Filtering Detections:
We only retain detections classified as "person." This ensures that non-relevant objects, such as toys or furniture, are ignored.
An optional size-based filtering can be applied to further distinguish between children and adults based on the area of the bounding box. This is useful if there is a noticeable size difference between the two groups in the video footage.

# Tracking with SORT:
The filtered detections are passed to the SORT (Simple Online and Realtime Tracking) algorithm, which assigns unique IDs to each detected person and tracks them across frames.
SORT uses a combination of Kalman Filters and the Hungarian algorithm to predict and update object trajectories, ensuring that IDs are consistently maintained even when objects move or temporarily exit the frame.

# Handling Re-entries and Occlusions:
Re-entries: If a person exits the frame and re-enters, SORT attempts to reassign the same ID if the prediction is consistent with the previous trajectory.
Occlusions: When a person is partially or fully occluded (e.g., passing behind another person or object), SORT attempts to maintain the correct ID by predicting the person’s movement until they are visible again.

# Overlaying Predictions on Video:
For each tracked person, the corresponding bounding box and unique ID are drawn on the video frame using OpenCV’s cv2.rectangle and cv2.putText functions.
This visual overlay helps in reviewing the accuracy and effectiveness of the detection and tracking process.

# Saving the Output Video:
The processed frames with overlaid predictions are written to an output video file using OpenCV’s cv2.VideoWriter. This video can then be reviewed to analyze the interactions between children and therapists.

# Analyzing Results
The final output video shows bounding boxes around each detected person, labeled with a unique ID that persists throughout the video. This output can be analyzed for:
Behavioral Analysis: By tracking the movement and interactions of children with ASD and therapists, we can gain insights into behavioral patterns, social engagement, and response to therapy.
Engagement Levels: By monitoring the proximity and attention between the child and therapist, we can infer levels of engagement and areas needing further intervention.

# Reproducibility
To reproduce the results:
1. Setup: Ensure that the required dependencies are installed as outlined in the Requirements section of the README.
2. Run the Script: Execute the person_tracker.py script on your video data, ensuring that the video_path and output_path are correctly set.
3. Review the Output: The output video will be saved with bounding boxes and IDs overlaid, allowing you to analyze the tracked movements.

By following these steps and understanding the underlying logic, evaluators can easily reproduce the results and potentially modify the pipeline for different use cases or datasets.

# Now check the process for your ease and do as mentioned next

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


