#!/usr/bin/env python3
from ev3dev.ev3 import *
mR = LargeMotor('outA')
mL = LargeMotor('outC')
mR.stop_action = 'coast'
mL.stop_action = 'coast'
mR.polarity = 'normal'
mL.polarity = 'normal'
print('Hello, my name is EV3!')

def moveR():
	mR.run_forever()
def moveL():
    mL.run_forever()

def GM(R, L):
    print ("running", R, " ",  L)
    stop()
    mR.run_forever(speed_sp = R)
    mL.run_forever(speed_sp = L)

def GM2(R, L):
    print ("running: ", R, " ", L)
    mR.run_forever(speed_sp = R)
    mL.run_forever(speed_sp = L)

    
def goback():
    stop()
    mR.run_forever(speed_sp = -300)
    mL.run_forever(speed_sp = -300)

def forward():
    stop()
    moveR()
    moveL()

def stop():
    mR.stop()
    mL.stop()

def turnL():
    stop()
    moveR()

def turnR():
    stop()
    moveL()

stop()
