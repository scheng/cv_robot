
#return 0 => on right
#return 1 => on left
import math
import cv2
import numpy as np
import time

WIDTH = 320
HEIGHT = 240

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)

time.sleep(2)
_,_ = cap.read()
_,_ = cap.read()

def linePos():

	ret, img = cap.read()
	img = np.delete(img, np.s_[WIDTH-2:WIDTH], 1)
	img = cv2.flip(img, -1)	
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	edge = cv2.Canny(gray, 300, 400)
	kernal = np.ones((1, 2), np.uint8)

	lines = cv2.HoughLinesP(edge, rho = 1, theta = 3.1415/360, threshold = 50,minLineLength = 30,maxLineGap =  20)

	maxMag = 0
	try:	
		for x in range(0, len(lines)):
			for x1,y1,x2,y2 in lines[x]:
				mag = math.hypot(x1-x2, y1-y2)
				if mag > maxMag: 
					maxMag = mag
					mx1 = x1; mx2 = x2; my1 = y1; my2 = y2
		avgPt = lines[0][0][0] + lines[0][0][2] + lines[1][0][0] + lines[1][0][2]
		avgPt /= 4
		if avgPt > 160: return "0" #print ("line on right")
		else: return "1" #print ("line on left")
	except: return "2"
#	cv2.imwrite('pic/edges' + str(y) + '.jpg', edge)
#	cv2.imwrite('pic/lines' + str(y) + '.jpg', img)
#linePos()
#
