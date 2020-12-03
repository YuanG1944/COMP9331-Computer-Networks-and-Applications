'''
T3 COMP9331
YUAN GAO
z5239220 

reference form:
https://blog.csdn.net/qq_31063727/article/details/89740190?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.channel_param&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-7.channel_param
'''
import socket
import os
import json
import struct
 
def up_load(filepath, filename):
    '''
    uploaded function
    :param filepath: the path that the file in
    :param filename: file name
    '''
    sk = socket.socket()
    sk.connect(('127.0.0.1', 5745)) 
    try:
        # Creat header
        head = {'filepath': filepath,
                'filename': filename,
                'filesize': None}  
        file_path = os.path.join(head['filepath'], head['filename'])
        # count size of file
        filesize = os.path.getsize(os.path.join(head['filepath'], head['filename']))  
        head['filesize'] = filesize
        json_head = json.dumps(head) 
        bytes_head = json_head.encode('utf-8') 
        # count length of header
        head_len = len(bytes_head)  
        # using struct package int and fix buffer size
        pack_len = struct.pack('i', head_len) 
        # send header 
        sk.send(pack_len)
        sk.send(bytes_head)

        # sending 
        with open(file_path, 'rb') as f:
            while filesize:
                if filesize >= 1024:
                    content = f.read(1024)
                    filesize -= 1024
                    sk.send(content)  
                else:
                    content = f.read(filesize)
                    sk.send(content)
                    filesize = 0
                    break
        sk.close()
        return True
    except Exception:
        return False

# up_load("","123.png")