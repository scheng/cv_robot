#return values switched for some reason
#return 0 => on right
#return 1 => on left
import math
import cv2
import numpy as np
import time
import warp

WIDTH = 320
HEIGHT = 240

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)

time.sleep(2)
_,_ = cap.read()
_,_ = cap.read()

def maxThree(arr):
	min = 1000
	maxLoc = -1
	for pix in range(0, len(arr)-3+1):
		avg = arr[pix]
#		avg = arr[pix]/3 + arr[pix + 1]/3 + arr[pix + 2]/3
		if (avg) < min:
			min = avg
			maxLoc = pix
	return maxLoc + 1

def linePos():
	debug = True
	ret, img = cap.read()
	img = np.delete(img, np.s_[WIDTH-2:WIDTH], 1)
	img = cv2.flip(img, -1)	
	img = warp.warpImg(img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = gray.astype(int)
#	print (len(gray[0]))
	#for x in gray:
	#	print (maxThree(x))
	sum = 0	
	sumtop = 0
	if debug:
		for num in range(len(gray)):
			if np.min(gray[num]) < 128:
				gray[num][np.argmin(gray[num])] = 255
			
	for num in range(0, 30):
		if np.min(gray[num]) < 128: sumtop += np.argmin(gray[num])/30
	for num in range(len(gray)-30, len(gray)):
		if np.min(gray[num]) < 128: sum += np.argmin(gray[num])/30
	cv2.imwrite("new4.jpg", gray)
	if sumtop - sum > len(gray[0])/5:
		if debug: print ("curve RIGHT")
	if sumtop - sum < -len(gray[0])/5:
		if debug: print ("curve LEFT")
	if sum > len(gray[0])/2:
		if debug: print("turn RIGHT")
		return "0" #line to the right of the robot, turn left
	elif sum < len(gray[0])/2:
		if debug: print("turn LEFT")
		return "1"
	else:
		if debug: print ("BIG PROBLEM")
		return "2" #big problem
#		gray[num][maxThree(gray[num])] = 255
	if debug: print("FINISHED")
linePos()
#count = 0
#while True:
#	count = count + 1
#	t = time.time()
#	linePos()
#	if (count % 100 == 0): print (time.time() - t)
