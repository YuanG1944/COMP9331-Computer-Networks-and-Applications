'''
T3 COMP9331
YUAN GAO
z5239220

reference form:
https://blog.csdn.net/qq_31063727/article/details/89740190?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.channel_param
'''
import socket
import struct
import json


def download(fpath): 
    '''
    download function
    :param fpath: file path
    '''
    sk = socket.socket()
    sk.bind(('127.0.0.1', 5745))  #bind ip address and port
    sk.listen()   # start listen
    conn, addr = sk.accept() 
    try:
        head_len = conn.recv(4)
        head_len = struct.unpack('i', head_len)[0]  # unpack header
        # receve header
        json_head = conn.recv(head_len).decode('utf-8')
        head = json.loads(json_head)
        file_size = head['filesize']

        with open(fpath, 'ab') as f:
            # print(file_size)
            while file_size:
                if file_size >= 1024:
                    content = conn.recv(1024)
                    f.write(content)
                    file_size -= 1024
                else:
                    content = conn.recv(file_size)
                    f.write(content)
                    file_size = 0
                    break
        conn.close()
        sk.close()
        return True
    except Exception:
        return False


# download()