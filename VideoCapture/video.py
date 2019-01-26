import cv2,time

video = cv2.VideoCapture(0)
# argument may be video file path / 0,1,2 defining position of webcam or external cameras

a=0

while True:  #will run code infinitely
    a+=1
    check, frame = video.read()
    print(check)
    print(frame)
    # time.sleep(3)

    # gray  = cv2.cvtColor(frame,cv2.COLOR_BGRTGRAY)
    cv2.imshow("Capturing video",frame)
    key = cv2.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()

cv2.destroyAllWindows()
