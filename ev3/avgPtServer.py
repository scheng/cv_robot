import socket
import time
import movement
from concurrent.futures import ThreadPoolExecutor as TPE
s = socket.socket()
host = socket.gethostname()
port = 1250
s.bind((host,port))
s.listen(5)
c, addr = s.accept()

#global MM 
MM = 0
oldMM = 0
# 0 = stay still
# 1 = move forward
# 2 = turn right
# 3 = turn left
# 4 = move backward

def moveLeft():
    movement.GM2(150, -35)
    print ("going left")

def moveRight():
    movement.GM2(-35, 150)
    print ('going right')

def moveForward():
    movement.GM2(70, 70)
    print ('straight')

def moveMotors():
    global MM
    global oldMM
    while True:
        if MM == 2 and oldMM != MM:
            movement.GM(-20,50)
            print ("turnin' right")
            oldMM = MM
        elif MM == 3 and oldMM != MM:
            movement.GM(50,-20)         
            print ("turnin' left")
            oldMM = MM

def getInfos():
    global MM
    x = 0
    with c:
        print("Connection accepted from " + repr(addr[1]))
        while True:
            print (x)
            x = x + 1
       # c, addr = s.accept()
            dat = c.recv(1)
            msg = str(dat.decode())
            print (msg)
            if msg == "0":
                moveRight()
                print ("0, turning right")
                #MM=2
            if msg == "1":
                moveLeft()
                print ("1, turning left")
                #MM = 3
            if msg == "2":
                #moveRight()
                moveForward()
                print ("2, something is BROKED")
            else:
                print ("recieved:" + msg +"!!")
            if not dat:
                break
            c.sendall(dat)
            time.sleep(0.1)

EXL = []         
with TPE(max_workers = 2) as executor:
    EXL.append(executor.submit(getInfos))
#    EXL.append(executor.submit(moveMotors))

