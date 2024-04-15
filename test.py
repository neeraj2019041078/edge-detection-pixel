import cv2
import numpy as np

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
                    cv2.fillPoly(thresh,[contour],(0,0,0))

                else:
                    cv2.fillPoly(thresh,[contour],(255,255,255))
        
        output=cv2.bitwise_and(rotated_frame,rotated_frame,mask=thresh)

        # cv2.namedWindow("output",cv2.WINDOW_NORMAL)
        # cv2.imshow("output",output)
        crop_image=output[1200:1250,left_x:right_x]
        print(crop_image)
        middle_y=crop_image.shape[0]//2

        p1=(left_x,middle_y)
        p2=(right_x,middle_y)
        cv2.line(crop_image,p1,p2,(0,0,255),1)
        cv2.namedWindow("output",cv2.WINDOW_NORMAL)
        cv2.imshow("output",crop_image)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

video_path = r"C:/Users/DSI-LPT-006/Desktop/test/2024-03-28/video_4500_13-02-13.avi"
detect_edges(video_path)









# text_position=(p1[0]+left_x+2,p1[1]+1250)
 # cv2.line(output, (p1[0] + left_x + 2, p1[1] + 1250), (p2[0] + right_x+ 2, p2[1] + 1250), (0, 0, 255), 2)