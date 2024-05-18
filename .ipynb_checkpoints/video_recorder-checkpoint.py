""" This Project have funtionality related to load a video from a path or record 
 a video and  save it on working directrey """
 
import cv2 

print( "Welcome to video_player") 
print("Please select a options")

key = int(input(" 1. Record Vidoe \n 2. Play video \n 3. exit \n"))
 
if key == 1:
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv2.imshow("frame",frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if key == 2:
    path = input("enter path of the video file:- ")
    vid = cv2.VideoCapture(path,cv2.CAP_DSHOW)
    print("video matrix", vid)
    
    while True:
        ret , frame = vid.read()
        if ret == True:
            frame = cv2.resize(frame, (640,480))
            cv2.imshow("frame",frame)
            k = cv2.waitKey(100)
            if k == ord('q') & 0xff:
                break
    vid.release()
    cv2.destroyAllWindows()
    
    
if key ==3:
    pass
