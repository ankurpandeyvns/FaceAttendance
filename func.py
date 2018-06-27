from cv2 import *
import os
cam = VideoCapture(0)
s, img = cam.read()
if s:
    imshow("cam-test",img)
    destroyWindow("cam-test")
    imwrite("./ToCheck/filename.jpg",img)
    t=os.popen("face_recognition --cpus 2 ./KnownFaces ./ToCheck | cut -d ',' -f2").read()
    name=t.split()
    name=str(name[len(name)-1])
    print (name)