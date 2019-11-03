import cv2
import numpy as np
import dlib
from math import hypot
from pynput.keyboard import Controller
#import time
#cap= cv2.VideoCapture(0)
class EyeDet:
    def starter(self,hel):
        cap= cv2.VideoCapture(0)
        detector= dlib.get_frontal_face_detector()
        predictor= dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
       
        def midpoint(p1, p2):
            return int((p1.x+p2.x)/2), int((p1.y+p2.y)/2)
        font= cv2.FONT_HERSHEY_SIMPLEX
        keyboard = Controller()
        while True:
            ret, frame= cap.read()
            frame=cv2.flip(frame, 1)
            gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces= detector(gray)
            for face in faces:
        #        x, y= face.left(), face.top()
        #        x1, y1= face.right(), face.bottom()
        #        cv2.rectangle(frame, (x,y), (x1,y1),(0,255,0),2)
               
                landmarks= predictor(gray, face)
                left_point= (landmarks.part(36).x, landmarks.part(36).y)
                right_point= (landmarks.part(39).x, landmarks.part(39).y)
                center_top= midpoint(landmarks.part(37), landmarks.part(38))
                center_bottom= midpoint(landmarks.part(41), landmarks.part(40))
               
                cv2.line(frame, left_point, right_point, (0,255,0),2)
                cv2.line(frame, center_top, center_bottom, (0,255,0),2)
           
           
                ver_line_length= hypot((center_top[0]-center_bottom[0]),(center_top[1]-center_bottom[1]))
                hor_line_length= hypot((left_point[0]-right_point[0]),(left_point[1]-right_point[1]))
               
                ratio=hor_line_length/ver_line_length
               
                left_point2= (landmarks.part(42).x, landmarks.part(42).y)
                right_point2= (landmarks.part(45).x, landmarks.part(45).y)
                center_top2= midpoint(landmarks.part(43), landmarks.part(44))
                center_bottom2= midpoint(landmarks.part(47), landmarks.part(46))
               
                cv2.line(frame, left_point2, right_point2, (0,255,0),2)
                cv2.line(frame, center_top2, center_bottom2, (0,255,0),2)
           
           
                ver_line_length2= hypot((center_top2[0]-center_bottom2[0]),(center_top2[1]-center_bottom2[1]))
                hor_line_length2= hypot((left_point2[0]-right_point2[0]),(left_point2[1]-right_point2[1]))
               
                ratio2=hor_line_length2/ver_line_length2
               
               
                if ratio>4.5 or ratio2>4.5:
                #              time.sleep(0.05 )
                    cv2.putText(frame, "BLINKING", (50,150),font, 3, (255,0,0))
                                           
                    keyboard.press(' ')
                                                                                                                                       
                    keyboard.release(' ')
   
        #        elif ratio>4.6:
        #            cv2.putText(frame, "LEFT BLINKING", (50,150),font, 3, (255,0,0))
        #            keyboard.press('  ')
        #            keyboard.release('  ')
        #                                                                  
            cv2.imshow("Frame",frame)  
            key=cv2.waitKey(1)
           
            if key == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    elem = EyeDet()    
