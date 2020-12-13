import socket

s = socket.socket()

PORT = 9898
print("\nServer is listening on port :", PORT, "\n")

s.bind(('', PORT))

s.listen(10)

file = open("try.txt", "wb")
print("\n Copied file name will be try.txt at server side\n")

while True:
    conn, addr = s.accept()


    msg ="\n\n-----\n Hi Client[IP address: "+ addr[0] + "], \n**Welcome to Server** \n -Server\n-----\n \n\n"
    conn.send(msg.encode())

    RecvData = conn.recv(1024)
    while RecvData:
        file.write(RecvData)
        RecvData = conn.recv(1024)

    file.close()
    print("\n File has been coppied successfully \n")

    conn.close()
    print("\nServer closed the connection \n")

    
    break
