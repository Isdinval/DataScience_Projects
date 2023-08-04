import cv2
import pandas as pd
from ultralytics import YOLO
import numpy as np
import time
import math


class Tracker:
    def __init__(self):
        # Store the Kalman filter for each tracked object
        self.kalman_filters = {}

        # Keep the count of the IDs
        # each time a new object id detected, the count will increase by one
        self.id_count = 0

    def update(self, objects_rect):
        # Objects boxes and ids
        objects_bbs_ids = []

        # Get center point of new object and update Kalman filters
        for rect in objects_rect:
            x, y, w, h = rect
            cx = (x + x + w) // 2
            cy = (y + y + h) // 2

            # Find out if that object was detected already
            same_object_detected = False
            for obj_id, kf in self.kalman_filters.items():
                prediction = kf.predict()
                predicted_x, predicted_y = prediction[0], prediction[1]

                dist = math.hypot(cx - predicted_x, cy - predicted_y)

                if dist < 35:
                    # Update Kalman filter with new measurement
                    measurement = np.array([[cx], [cy]], dtype=np.float32)
                    kf.correct(measurement)

                    objects_bbs_ids.append([x, y, w, h, obj_id])
                    same_object_detected = True
                    break

            # New object is detected, we create a new Kalman filter for it
            if not same_object_detected:
                kf = cv2.KalmanFilter(4, 2)  # 4 state variables, 2 measurement variables
                kf.measurementMatrix = np.array([[1, 0, 0, 0], [0, 1, 0, 0]], dtype=np.float32)
                kf.transitionMatrix = np.array([[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [0, 0, 0, 1]], dtype=np.float32)
                kf.processNoiseCov = 0.01 * np.eye(4, dtype=np.float32)
                kf.measurementNoiseCov = 0.1 * np.eye(2, dtype=np.float32)

                measurement = np.array([[cx], [cy]], dtype=np.float32)
                kf.statePre = np.array([[cx], [cy], [0], [0]], dtype=np.float32)
                kf.statePost = np.array([[cx], [cy], [0], [0]], dtype=np.float32)

                self.kalman_filters[self.id_count] = kf

                objects_bbs_ids.append([x, y, w, h, self.id_count])
                self.id_count += 1

        return objects_bbs_ids

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        colorsBGR = [x, y]
        print(colorsBGR)

def main():
    model = YOLO('yolov8s.pt')

    cv2.namedWindow('RGB')
    cv2.setMouseCallback('RGB', RGB)

    # cap=cv2.VideoCapture('veh2.mp4')
    video_path = r"C:\Users\Olivi\OneDrive\Documents\FREELANCER\Python_OPENCV\Python_Based_Vehicle_Speed_Estimation_from_Smartphone_Video_Recording\sample_video_speed.mp4"
    cap = cv2.VideoCapture(video_path)



    my_file = open("coco.txt", "r")
    data = my_file.read()
    class_list = data.split("\n")
    print(class_list)

    count = 0

    tracker = Tracker()

    # Define two points to create the lines
    line_point1 = (117, 783)
    line_point2 = (283, 751)
    line_point3 = (351, 865)
    line_point4 = (653, 801)

    offset = 6 #6
    crossed_ids = set()

    # Calculate the slope and intercept of each line
    slope1 = (line_point2[1] - line_point1[1]) / (line_point2[0] - line_point1[0])
    intercept1 = line_point1[1] - slope1 * line_point1[0]

    slope2 = (line_point4[1] - line_point3[1]) / (line_point4[0] - line_point3[0])
    intercept2 = line_point3[1] - slope2 * line_point3[0]

    # Initialize counters to keep track of cars going up and down the lines
    counter = []
    counter1 = []

    vh_down = {}  # Dictionary to store the time when a car crosses the line going down
    vh_up = {}  # Dictionary to store the time when a car crosses the line going up

    # Initialize the Kalman Filters for tracking
    kf_dict = {}
    
    going_up = 0
    going_down = 0
    
    crossed_line1_time = {}
    crossed_line2_time = {}
    




    # Initialize the VideoWriter for saving the annotated video
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output_video = cv2.VideoWriter('output_video.avi', fourcc, 30, (int(cap.get(3)), int(cap.get(4))))
    
    





    while True:
        ret, frame = cap.read()
        if not ret:
            break
        count += 1
        if count % 3 != 0:
            continue
        
        # Create the mask as a polygon
        mask = np.zeros_like(frame)
        pts = np.array([[37, 700], [1076, 813], [1078, 1008], [0, 1008]], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.fillPoly(mask, [pts], (255, 255, 255))
        # Apply the mask to the frame
        masked_frame = cv2.bitwise_and(frame, mask)

        results = model.predict(masked_frame)
        a = results[0].boxes.data
        px = pd.DataFrame(a).astype("float")

        list = []
        for index, row in px.iterrows():
            x1 = int(row[0])
            y1 = int(row[1])
            x2 = int(row[2])
            y2 = int(row[3])
            d = int(row[5])
            c = class_list[d]
            if 'car' in c:
                list.append([x1, y1, x2, y2])
        bbox_id = tracker.update(list)
        for bbox in bbox_id:
            x3, y3, x4, y4, id = bbox
            cx = int(x3 + x4) // 2
            cy = int(y3 + y4) // 2

            # Check if the car crosses line 1
            if abs(cy - (slope1 * cx + intercept1)) < offset and id not in crossed_line1_time:
                # Record the crossing time for line 1
                crossed_line1_time[id] = time.time()
    
            # Check if the car crosses line 2
            if abs(cy - (slope2 * cx + intercept2)) < offset and id not in crossed_line2_time:
                # Record the crossing time for line 2
                crossed_line2_time[id] = time.time()
            
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
            cv2.rectangle(frame, (x3, y3), (x4, y4), (0, 0, 255), 2)
            cv2.putText(frame, str(id), (cx, cy), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)

            # Check if the car crosses the lines
            pt_car = np.array((cx, cy))
            dist1 = cy - (slope1 * cx + intercept1)
            dist2 = cy - (slope2 * cx + intercept2)

            if abs(dist1) < offset and id not in crossed_ids:
                # Check the direction of the car with respect to line 1
                direction = "Going Up" if dist1 < 0 else "Going Down"

                # Draw the direction on the frame
                cv2.putText(frame, direction, (cx, cy - 20), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)

                # Update counters for going up or going down
                if dist1 < 0:
                    going_up += 1
                else:
                    going_down += 1

                # Add the car ID to the set of crossed IDs
                crossed_ids.add(id)
                    
                    
        # Calculate the intersection points of each line with the video frame edges
        y_left1 = int(slope1 * 0 + intercept1)
        y_right1 = int(slope1 * frame.shape[1] + intercept1)
        y_left2 = int(slope2 * 0 + intercept2)
        y_right2 = int(slope2 * frame.shape[1] + intercept2)

        # Draw the extended lines
        cv2.line(frame, (0, y_left1), (frame.shape[1], y_right1), (255, 255, 255), 1)
        cv2.line(frame, (0, y_left2), (frame.shape[1], y_right2), (255, 255, 255), 1)

        cv2.putText(frame, 'L1', line_point1, cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
        cv2.putText(frame, 'L2', line_point3, cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)

        # Draw the counters on the frame
        cv2.putText(frame, 'Going Up: ' + str(going_up), (60, 90), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)
        cv2.putText(frame, 'Going Down: ' + str(going_down), (60, 130), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 255), 2)


        # Write the frame with annotations to the output video
        output_video.write(frame)
        cv2.imshow("RGB", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    # Calculate the distance between line 1 and line 2 (known distance in pixels)
    distance_between_lines = math.sqrt((line_point1[0] - line_point3[0]) ** 2 + (line_point1[1] - line_point3[1]) ** 2)
    


    # Known real-world distance (width of the road in meters)
    known_distance_real_world = 14.0  # 14 meters
    # Corresponding points in the video frame
    point1 = (4, 939)   # (x1, y1)
    point2 = (758, 779)  # (x2, y2)
    # Calculate the corresponding number of pixels (distance in pixels)
    distance_pixels = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    # Compute the pixel scale (real-world distance per pixel)
    pixel_scale = known_distance_real_world / distance_pixels
    time_scale = 1 / 30




    # Compute the velocity for each car that crossed both lines
    for obj_id, time1 in crossed_line1_time.items():
        if obj_id in crossed_line2_time:
            # Get the crossing times for both lines
            time2 = crossed_line2_time[obj_id]
    
            # Calculate the time difference between crossing both lines
            time_difference = time2 - time1
    
            # Calculate the velocity in pixels per second
            if time_difference > 0:
                velocity_px_per_second  = distance_between_lines / time_difference
                # Convert velocity to real-world units if necessary (e.g., km/h)
                # velocity_real_world = pixels_to_real_world(velocity)
                velocity_km_per_hour = (velocity_px_per_second * pixel_scale * time_scale) * 3.6 * 100

                print(f"Car {obj_id}: Velocity: {velocity_px_per_second:.2f} px/s")
                print(f"Car {obj_id}: Velocity: {velocity_km_per_hour:.2f} km/h")
                print('  ')

    # Release the VideoWriter and close the output video file
    output_video.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
