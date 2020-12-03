# 导入socket库
# 服务端代码
from socket import *

# 主机地址为0.0.0.0, 表示绑定本机所有网络接口的ip地址
# 等待客户端来连接
IP = "127.0.0.1"
#端口号
SERVER_PORT = 50000
#定义一次从socket缓冲区最多读入512个字节数据
BUFLEN = 512

#实例化一个socket对象
#参数AF_INT表示该socket网络层使用IP协议
#参数SOCK_STREAM表示该socket传输层使用tcp协议
dataSocket = socket(AF_INET, SOCK_STREAM)

#连接服务端的socket
dataSocket.connect((IP, SERVER_PORT))

while True:
    #从终端读入用户输入的字符串
    toSend = input('>> ')
    if toSend == '':
        break
    #发送消息,也要编码为bytes
    dataSocket.send(toSend.encode())

    #等待接收服务段的消息
    recved = dataSocket.recv(BUFLEN)

    #如果返回空bytes,表示对方关闭了连接
    if not recved:
        break

    print(recved.decode())

dataSocket.close()