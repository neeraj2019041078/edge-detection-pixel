import cv2
import numpy as np
import time
def detect_edges(video_path):
    video_capture = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break
        
        height, width = frame.shape[:2]
        angle = 5
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
        rotated_frame = cv2.warpAffine(frame, rotation_matrix, (width, height))
   
        left_x = int(0.1 * width)
        right_x = int(0.93 * width)

        cv2.rectangle(rotated_frame, (0, 0), (left_x, height), (0, 0, 0), -1)
        cv2.rectangle(rotated_frame, (right_x, 0), (width, height), (0, 0, 0), -1)

        gray = cv2.cvtColor(rotated_frame, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 10, 255, 0)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            for contour in contours:
                area = cv2.contourArea(contour)
                if area < 100:
                    cv2.fillPoly(thresh, [contour], (0, 0, 0))
                else:
                    cv2.fillPoly(thresh, [contour], (255, 255, 255))
        
        output = cv2.bitwise_and(rotated_frame, rotated_frame, mask=thresh)

        crop_image = output[1200:1250, left_x:right_x]
      
        middle_y = crop_image.shape[0] // 2

        if crop_image.size > 0 and np.any(crop_image):
            first_point = np.where(crop_image.any(axis=0))[0][0]
            p1 = (first_point + left_x, middle_y + 1225)

            reverse_img = np.flip(crop_image, axis=1)

            second_point = np.where(reverse_img.any(axis=0))[0][0]
            second_point = crop_image.shape[1] - second_point - 1
            p2 = (second_point + left_x, middle_y + 1225)
            distance = p2[0] - p1[0]
            distance_str = str(int(distance))

            cv2.line(output, p1, p2, (0, 0, 255), 2)
            cv2.putText(output, distance_str, p1, cv2.FONT_HERSHEY_COMPLEX, 3, (255, 255, 255), 3)
        else:
            print("Crop image is empty")

        cv2.namedWindow("crop", cv2.WINDOW_NORMAL)
        cv2.imshow("crop", output)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.01)
    video_capture.release()
    cv2.destroyAllWindows()

# List of video file paths
video_paths = [
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-41-50.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-43-14.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-44-30.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-44-55.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-46-24.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-46-33.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-46-52.avi",
    #   r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-48-10.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-54-28.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-58-13.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_12-59-12.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_13-00-12.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_13-00-51.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_13-02-06.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_13-05-59.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_13-08-06.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_13-10-00.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_13-11-22.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-42-47.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-43-26.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-45-24.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-46-11.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-46-20.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-46-22.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-46-25.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-47-09.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-47-14.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-47-15.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-48-39.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-48-45.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-50-46.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-54-27.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-55-05.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-56-53.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-58-23.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_14-59-58.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-03-09.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-11-11.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-11-37.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-12-58.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-15-14.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-16-02.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-18-44.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-21-19.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-23-25.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-25-23.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-25-24.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-25-44.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-27-09.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-29-43.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-30-39.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-30-56.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-32-17.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-35-03.avi",
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-36-04.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-38-32.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-40-15.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-43-31.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-44-27.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-48-14.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-52-46.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-55-40.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-56-58.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_15-59-15.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-00-06.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-02-05.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-03-21.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-05-50.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-06-38.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-09-16.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-13-18.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-15-20.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-19-13.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-21-40.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-22-20.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-23-53.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-29-06.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-29-09.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-33-53.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-33-55.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-35-16.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-35-20.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-35-21.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-38-48.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-38-49.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-41-14.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-41-33.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-42-41.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-45-39.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-48-44.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-51-38.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-51-39.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-55-21.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-56-46.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-56-47.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-56-54.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-56-55.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-57-29.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_16-58-58.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_17-02-46.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_17-04-40.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_17-10-33.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_17-15-14.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_17-17-37.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-25-40.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-26-57.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-30-33.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-33-33.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-35-02.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-36-45.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-39-53.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-41-52.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-45-32.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-46-41.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-47-58.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-48-18.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_18-58-40.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_19-00-23.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_19-01-43.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_19-04-29.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_19-05-41.avi",
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_19-06-23.avi"
    #  r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_19-08-34.avi"
    # r"C:\Users\DSI-LPT-006\Desktop\test\2024-03-27\video_19-09-46.avi"

]

# Iterate through each video path and call detect_edges function
for path in video_paths:
    print(f"Processing video: {path}")
    detect_edges(path)
    print("Video processing completed.")
