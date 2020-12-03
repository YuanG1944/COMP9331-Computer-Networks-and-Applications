
# version: python 3.7
# zID: z5052292

from socket import *
from datetime import datetime
import time
import sys

serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
clientSocket = socket(AF_INET, SOCK_DGRAM)
list_rtts = []
packets_lost = 0

for i in range(10):
	time_stamp = datetime.now().isoformat(sep=' ')[:-3]
	ping_message = "PING" + str(i) + ' ' + time_stamp + '\r\n'
	time_send = datetime.now()
	clientSocket.sendto(ping_message.encode(), (serverIP, serverPort))

	try:
		clientSocket.settimeout(1)
		response, severAddress = clientSocket.recvfrom(2048)
		time_receive = datetime.now()
		rtt = round((time_receive - time_send).total_seconds() * 1000)
		list_rtts.append(rtt)
		print(f'Ping to {serverIP}, seq = {i}, rtt = {rtt} ms')
		clientSocket.settimeout(None)

	except timeout:
		packets_lost += 1
		print(f'Ping to {serverIP}, seq = {i}, rtt = time out')

print("\n")
print(f'Minimun RTT = {min(list_rtts)} ms')
print(f'Maximun RTT = {max(list_rtts)} ms')
print(f'Average RTT = {round(float(sum(list_rtts)/len(list_rtts)))} ms')
print(f'10 packets transmitted, {10 - int(packets_lost)} packets received, {float(packets_lost) / 10 * 100}% of packets loss.')
clientSocket.close() 
