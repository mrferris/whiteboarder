import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(3)
print vc.read()
for i in range(-20,20):
	print cv2.VideoCapture(i).read()
if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break