import cv2,time,pandas
from datetime import datetime

first_frame = None
status_list=[None,None]
times = []
df = pandas.DataFrame(columns=["Start","End"])
video = cv2.VideoCapture(0)
# argument may be video file path / 0,1,2 defining position of webcam or external cameras

while True:  #will run code infinitely

    check, frame = video.read()
    status = 0      #no motion in the given frame.....the first frame here
    # print(check)
    # print(frame)
    # time.sleep(3)

    gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(21,21),0)   #standard deviation

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)

    thresh_frame = cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]
    # 30. . the threshold. . . if diff is >30 then assign 255

    # remove black spots from larger white areas ...smoothing the frame. . . iterations is the no of times you want the image to go thr smoothing
    # thresh_frame1 = cv2.dilate(thresh_frame,None,iterations=8)
    thresh_frame = cv2.dilate(thresh_frame,None,iterations=8)

    # contours   ...cv2.RETR_EXTERNAL..to find the external countours
    (_,cnts,_) = cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    # filter the Countours
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:    #1000 pixels
            continue

        status = 1
        (x,y,h,w) = cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+h,y+h),(0,255,0),3)

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    cv2.imshow("Gray frame",gray)
    cv2.imshow("Delta frame",delta_frame)
    cv2.imshow("Threshold frame",thresh_frame)
    # cv2.imshow("Threshold frame1",thresh_frame1)
    cv2.imshow("Contours frame",frame)

    key = cv2.waitKey(1)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

    print(status)

print(status_list)
print(times)

for i in range(0,len(times),2):        #step of 2
    df = df.append({"Start":times[i],"End":times[i+1]},ignore_index=True)

df.to_csv("Times.csv")
video.release()

cv2.destroyAllWindows()
