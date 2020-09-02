import socket

s = socket.socket()
host = socket.gethostname()
port= 3333
s.bind((host, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print ("Connection made from:", addr)
    c.send("Thank you for connecting")
    c.close()
    
