from socket import *
import sys

IP = "127.0.0.1"
SERVER_PORT = int(sys.argv[1])
BUFLEN = 2048

listenSocket = socket(AF_INET, SOCK_STREAM)
listenSocket.bind((IP, SERVER_PORT))
listenSocket.listen(5)

while True:
    dataSocket, addr = listenSocket.accept()
    pkg = dataSocket.recv(BUFLEN)
    pkg = pkg.decode()
    print(pkg)

    idx = pkg.split("\n")[0].split(" ")[1][1:]
    
    try:
        f = open(idx, 'rb')
        content = f.read()
        if("html" in idx):
            response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n"
        elif("png" in idx):
            response = "HTTP/1.1 200 OK\r\nContent-Type: image/png\r\n\r\n"

        dataSocket.sendall(response.encode())
        dataSocket.sendall(content)
        dataSocket.close()
    except FileNotFoundError:
        response = "HTTP/1.1 404 File not found\r\n\r\n"
        content = "<h1><head><center> 404 Error: File not found! </center></head></h1>"

        dataSocket.sendall(response.encode())
        dataSocket.sendall(content.encode())
        dataSocket.close()


