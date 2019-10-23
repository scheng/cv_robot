import socket
import maxPt
import time
s = socket.socket()
host = '169.254.198.254' # needs to be in quote
port = 1250
s.connect((host, port))
#print (s.recv(1024).decode())

#inpt = input('type anything and click enter... ')
#s.send(inpt.encode())
#data = s.recv(5)
#print ("got", repr(data))
x = 0
while True:
	print (x)
	x = x + 1
#	print ("taking pic")
	#is this getting the lastest frame?
	try:
		s.sendall(maxPt.linePos().encode())
		data = s.recv(1024)
		print ("gotdat", repr(data))
	except:# socket.error, exc:
		print ("error")#, exc)
#	print ("done taking")
	time.sleep(0.1)
