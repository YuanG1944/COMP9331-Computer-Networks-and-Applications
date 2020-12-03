# 导入socket库
# 服务端代码
from socket import *
import threading
import time
import datetime as dt

# 主机地址为0.0.0.0, 表示绑定本机所有网络接口的ip地址
# 等待客户端来连接
IP = "0.0.0.0"

#端口号
PORT = 50000
#定义一次从socket缓冲区最多读入512个字节数据
BUFLEN = 512

#实例化一个socket对象
#参数AF_INT表示该socket网络层使用IP协议
#参数SOCK_STREAM表示该socket传输层使用tcp协议
#等待客户端的连接
listenSocket = socket(AF_INET, SOCK_STREAM)

#socket绑定地址和端口
#提供IP地址和端口号
listenSocket.bind((IP, PORT))

#使socket处于监听状态,等待客户端的连接请求
#参数5表示最多接收多少个等待连接的客户端
listenSocket.listen(5)
print(f'服务器端启动成功, 在{PORT}端口等待客户端连接...')

# dataSocket = 产生一个新的socket用来传输文件
# addr = 返回客户端的ip地址
dataSocket, addr = listenSocket.accept()
print('接受一个客户端连接:', addr)

while True:
    #尝试读取对方发送的消息
    #BUFLEN 指定从接收缓冲里最多读取多少字节
    recved = dataSocket.recv(BUFLEN)

    #如果返回空bytes, 表示对方关闭了连接
    #退出循环,结束消息收发
    if not recved:
        break

    #读取的字节数据是bytes类型,需要解码为字符串
    info = recved.decode()
    print(f'收到对方的信息: \"{info}\"')

    #发送的数据类型必须是bytes, 所以需要编码
    dataSocket.send(f'服务器接收到了信息\"{info}\"'.encode())


#服务器也调用close()关闭socket
dataSocket.close()
listenSocket.close()
