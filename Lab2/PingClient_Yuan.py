import sys
import socket as sk
from datetime import datetime
import time as Time

IP = sys.argv[1]
PORT = int(sys.argv[2])
rttList = []
packageLost = 0
maxRTT = 0
minRTT = 0x3f3f3f3f
sequenceNumber = 3330

dataSocket = sk.socket(sk.AF_INET, sk.SOCK_DGRAM) #SOCK_DGRAM(UDP) SOCK_STREAM(TCP)

times = 0
while times < 15:
    times += 1
    timeStamp = datetime.now().isoformat()
    message = f"PING {sequenceNumber + times} {timeStamp}\r\n"
    timeSend = datetime.now()
    dataSocket.sendto(message.encode(), (IP, PORT))
    try:
        dataSocket.settimeout(0.6)
        response, severAddress = dataSocket.recvfrom(1024)
        timeReceive = datetime.now()
        RTT = round((timeReceive - timeSend).total_seconds() * 1000)
        rttList.append(RTT)
        maxRTT = max(maxRTT, RTT)
        minRTT = min(minRTT, RTT)
        output = f"Ping to {IP}, seq = {sequenceNumber + times}, rtt = {RTT} ms"
        print(output)
        dataSocket.settimeout(None)
        
    except sk.timeout:
        packageLost += 1
        print(f'Ping to {IP}, seq = {sequenceNumber + times}, rtt = time out')
        

dataSocket.close()
print("\n")
print(f'In 15 packets, there are {15 - int(packageLost)} packets received: ')
print(f"The minimum RTT is {minRTT} ms")
print(f"The maximum RTT is {maxRTT} ms")
print(f"The average RTT is {round(float(sum(rttList) / len(rttList)))} ms")

