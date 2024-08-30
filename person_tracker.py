import cv2
import torch
import numpy as np
from sort import Sort

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
tracker = Sort()

# Input and Output paths
video_path = r"C:\Users\hrish\Downloads\Input_Daniel.mp4"
output_path = r"C:\Users\hrish\Downloads\output_Daniel.mp4"

# Open video
cap = cv2.VideoCapture(video_path)

# Video writer setup
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform detection
    results = model(frame)
    detections = results.xyxy[0].cpu().numpy()

    # Prepare detections for tracking
    detections_for_tracking = []
    for det in detections:
        x1, y1, x2, y2, conf, cls = det
        # Only consider persons (usually class ID 0 for YOLOv5)
        if int(cls) == 0:
            # Optional: Add size-based filtering to distinguish between child and adult
            width = x2 - x1
            height = y2 - y1

            # Example: Consider small bounding boxes as children and large as adults
            if width * height > 5000:  # Example threshold, tweak as needed
                detections_for_tracking.append([x1, y1, x2, y2, conf])

    detections_for_tracking = np.array(detections_for_tracking)

    # Perform tracking
    tracked_objects = tracker.update(detections_for_tracking)

    # Draw results
    for det in tracked_objects:
        x1, y1, x2, y2, obj_id = det
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv2.putText(frame, f'ID: {int(obj_id)}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Write frame to output
    out.write(frame)

    # Optional: Display the frame
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
