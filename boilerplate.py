import sys, socket, time

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    print "More arguments"
    print sys.argv[0],"<IP> <port>"
    sys.exit()

payload = "" #Dont forget the carriage return/new line feed

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.recv(1024) # Recieve Banner
s.send(payload)
print s.recv(1024) # Recieve Reply

s.close() # Close the Connection

