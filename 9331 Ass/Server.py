'''
T3 COMP9331
YUAN GAO
z5239220 
'''
import socket
import threading
import json
import sys
import os
import time
import FileManagement
from Command import ForumCommad
import FTclient
import FTserver

class Server:
    """
    Server class
    """
    def __init__(self, port_num, admin_password):
        """
        Init
        :param port_num: Port number
        :param admin_password: administrator password
        """
        self.__password = admin_password
        self.__port_num = port_num

        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP protocol
        self.__connections = list()  # online user id
        self.__nicknames = list()  # online user nickname
        self.__users = {}  # Registered users
    
    def create_info(self):
        """
        mkdir 'forum' folder
        Creat 'forumList' which store the created forum thread
        """
        dirs = 'forum/'
        filename = 'forum/forumList'
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        if not os.path.exists(filename):
            os.system(r"touch {}".format(filename)) # Call the system command line to create a file

    def user_thread(self, user_id):
        """
        user subthread
        :param user_id: user id
        """

        connection = self.__connections[user_id]
        nickname = self.__nicknames[user_id]
        print(f'{nickname} successful login')


        # Listen
        while True:
            try:
                forum_commad = ForumCommad()
                buffer = connection.recv(1024).decode()
                obj = json.loads(buffer)

                if obj["type"] == "CRT":
                    if obj["len"] == 2:
                        print(f'{nickname} issued {obj["type"]} command')
                        if forum_commad.create_thread(nickname, obj["message"]):
                            mess = "Thread " + obj['message'] + " created"
                            print(mess)
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                        else:
                            mess = "Thread " + obj['message'] + " exists"
                            print(mess)
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                    else:
                        mess = "Incorrect syntax for CRT"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "MSG":
                    if obj["len"] == 3:
                        print(f'{nickname} issued {obj["type"]} command')
                        if forum_commad.post_message(nickname, obj["trd"], obj["message"]):
                            msg = f"Message posted to {obj['trd']} thread"
                            print(msg)
                            self.private_msg(obj['sender_id'], msg, obj['trd'])
                        else:
                            print("Message posted faild")
                    else:
                        mess = "Incorrect syntax for MSG"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "DLT":
                    if obj["len"] == 3:
                        print(f'{nickname} issued {obj["type"]} command')
                        if forum_commad.del_message(nickname, obj["trd"], obj["num"]):
                            mess = "The message has been deleted"
                            print(mess)
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                        else:
                            mess = "The message belongs to another user and cannot be deleted"
                            print("Message cannot be deleted")
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                    else:
                        mess = "Incorrect syntax for DLT"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "EDT":
                    if obj["len"] == 4:
                        print(f'{nickname} issued {obj["type"]} command')
                        if forum_commad.edit_message(nickname, obj["trd"], obj["num"], obj["message"]):
                            print("Message has been edited")
                            mess = "The message has been edited"
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                        else:
                            print("Message cannot be edited")
                            mess = "The message belongs to another user and cannot be edited"
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                    else:
                        mess = "Incorrect syntax for EDT"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "LST":
                    if obj["len"] == 1:
                        print(f'{nickname} issued {obj["type"]} command')
                        mess = forum_commad.list_threads()
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                    else:
                        mess = "Incorrect syntax for LST"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "RDT":
                    if obj["len"] == 2:
                        print(f'{nickname} issued {obj["type"]} command')
                        lst = forum_commad.read_thread(obj["trd"])
                        if lst == "False":
                            print(f"Thread cannot {obj['trd']} read")
                            mess = f"Thread {obj['trd']} does not exist"
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                        else:
                            print(f"Thread {obj['trd']} read")
                            if lst == "":
                                self.private_msg(obj['sender_id'], "Thread 9331 is empty", obj['trd'])
                            else:
                                self.private_msg(obj['sender_id'], lst, obj['trd'])
                    else:
                        mess = "Incorrect syntax for RDT"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "UPD":
                    if obj["len"] == 3:
                        if forum_commad.post_message(nickname, obj["trd"], ("uploaded " + obj["filename"])):
                            print(f'{nickname} issued {obj["type"]} command')
                        else:
                            print("Faild upload")
                        FTclient.up_load("", obj["filename"])
                        print(f"{nickname} uploaded file {obj['filename']} to {obj['trd']} thread")
                    else:
                        mess = "Incorrect syntax for UPD"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "DWN":
                    if obj["len"] == 3:
                        filename = "forum/" + obj["trd"] + "/" + obj["trd"] + "-" + obj["filename"]
                        print(filename)
                        print(f'{nickname} issued {obj["type"]} command')
                        if not os.path.exists(filename):
                            mess = f"{obj['filename']} dose not exist in Thread {obj['trd']}"
                            print(mess)
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                        else:
                            FTserver.download(obj["filename"])
                            mess = f"{obj['filename']} successfully downloaded"
                            print(mess)
                            forum_commad.post_message(nickname, obj["trd"], ("dwonloaded " + obj["filename"]))
                            
                    else:
                        mess = "Incorrect syntax for DWN"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "RMV":
                    if obj["len"] == 2:
                        print(f'{nickname} issued {obj["type"]} command')
                        if forum_commad.delete_threads(nickname, obj["trd"]):
                            print(f"{obj['trd']} has been removed")
                            mess = f"Thread {obj['trd']} has been removed"
                            self.private_msg(obj['sender_id'], mess, obj['trd'])
                        else:
                            print(f"Thread {obj['trd']} cannot be removed")
                            print("The thread was created by another user and cannot be removed")
                    else:
                        mess = "Incorrect syntax for RMV"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "XIT":
                    if obj["len"] == 1:
                        print(f'{nickname} exit')
                        # self.online_list.remove(myconnection)
                        self.private_msg(obj['sender_id'], "XIT", obj['trd'])
                        self.__connections[user_id] = None
                        self.__nicknames[user_id] = None
                        self.__connections[user_id].close()
                        # myconnection.send(b'XIT')
                    else:
                        mess = "Incorrect syntax for XIT"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                elif obj["type"] == "SHT":
                    if obj["len"] == 2:
                        if obj["password"] == str(self.__password):
                            print(f'{nickname} exit')
                            print("Server shutting down")
                            mess = "Server shutting down"
                            self.broadcast(obj['sender_id'], mess)
                            FileManagement.delAllFile()
                            self.__flag = 0
                            os._exit(0)
                        else:
                            msg = "Incorrect password"
                            self.private_msg(user_id, msg, obj['trd'])
                    else:
                        mess = "Incorrect syntax for SHT"
                        self.private_msg(obj['sender_id'], mess, obj['trd'])
                # else:
                #     print("Invalid command")
            except Exception:
                try:
                    # print('Connection failure:', connection.getsockname(), connection.fileno())
                    self.__connections[user_id].close()
                    self.__connections[user_id] = None
                    self.__nicknames[user_id] = None
                except Exception:
                    print(f"Waiting for clients")
                    break
                    

    def broadcast(self, user_id=0, message=''):
        """
        broadcast
        :param user_id: user id
        :param message: broadcast information
        """
        for i in range(1, len(self.__connections)):
            if self.__connections[i] != None:
                self.__connections[i].send(json.dumps({
                    'sender_id': user_id,
                    'typ': "public",
                    'sender_nickname': self.__nicknames[user_id],
                    'message': message
                }).encode())

    def private_msg(self, user_id, message, thread, up_down="False"):
        """
        private message
        :param user_id: user id
        :param message: private message information
        """
        self.__connections[user_id].send(json.dumps({
            'sender_id': user_id,
            'typ': "private",
            'sender_nickname': self.__nicknames[user_id],
            'trd': thread,
            'message': message,
            'up_down': up_down
        }).encode())
        
        
    def start(self):
        """
        start up 
        """
        self.create_info()
        # bind port
        self.__socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__socket.bind(('127.0.0.1', int(self.__port_num)))
        # start listen
        self.__socket.listen(10)
        print('Waiting for clients')

        # Clear list and dictionary
        self.__connections.clear()
        self.__nicknames.clear()
        self.__connections.append(None)
        self.__nicknames.append('System')

        # Registered users
        self.__users = FileManagement.GetuserDic()
    
        # Listen
        while True:
            connection, address = self.__socket.accept()
            print('Client connected', connection.getsockname(), connection.fileno())

            # try to recive message
            try:
                flag = 1
                # If it is a connection command, 
                # then a new user number is returned to receive the user connection
                while flag == 1:
                    buffer = connection.recv(1024).decode()
                    # Parse into json data
                    obj = json.loads(buffer)
                    if obj['type'] == 'login':
                        # Determine whether this account has been registered
                        user_name = obj['nickname']
                        if(user_name in self.__users.keys()):
                            if (user_name in self.__nicknames):
                                msg = user_name+ " has already logged in"
                                connection.send(json.dumps({
                                    'type': 'error',
                                    'password': msg
                                }).encode())
                                print(f"{user_name} asd has already logged in")
                            else:
                                # Determine whether this password is correct
                                msg = "verify password"
                                connection.send(json.dumps({
                                    'type': 'name correct',
                                    'password': msg
                                }).encode())
                                
                                buffer = connection.recv(1024).decode()
                                pass_word = json.loads(buffer)

                                if(self.__users[user_name] == pass_word['password']):
                                    flag = 0
                                    # print(user_name + " successful login")
                                    mss = 'Welcome to the forum'
                                    connection.send(json.dumps({
                                        'isvalid': 'True',
                                        'welcome': mss
                                    }).encode())
                                    buffer = connection.recv(1024).decode()
                                    json.loads(buffer) # message must one send and one recv
                                    self.__connections.append(connection)
                                    self.__nicknames.append(user_name)
                                    break
                                else:
                                    flag = 1
                                    msg = 'Wrong PassWord'
                                    connection.send(json.dumps({
                                        'isvalid': 'False',
                                        'welcome': msg
                                    }).encode())
                                    buffer = connection.recv(1024).decode()
                                    json.loads(buffer) # message must one send and one recv
                        else:
                            flag = -1
                            print("Incorrect username")
                            connection.send(json.dumps({
                                'type': 'name invalid',
                            }).encode())
                            valid = connection.recv(1024).decode()
                            
                            # Register a new account
                            if valid == "yes":
                                flag = 0
                                connection.send(b'Please enter your new password: ')
                                newpass_word = connection.recv(1024).decode()
                                self.users = FileManagement.CreateNewUser(user_name, newpass_word)
                                print("Create a new user")
                                self.__connections.append(connection)
                                self.__nicknames.append(obj['nickname'])
                                connection.send(b'Welcome to the forum')
                                connection.recv(1024).decode()
                    else:
                        print('Unable to parse json packet:', connection.getsockname(), connection.fileno())
                
                # Open a new thread
                if flag == 0:
                    connection.send(json.dumps({
                        'id': len(self.__connections) - 1
                    }).encode())
                    thread = threading.Thread(target=self.user_thread, args=(len(self.__connections) - 1, ))
                    thread.setDaemon(True)
                    thread.start()
            except Exception:
                print('Unable to accept data:', connection.getsockname(), connection.fileno())


if __name__ == "__main__":
    try:
        PORT = sys.argv[1]
        PASSWORD = sys.argv[2]
        server = Server(PORT, PASSWORD)
        server.start()
    except OSError:
        print("Address or port already in use")
    except Exception:
        print("Incorrect syntax for starting sever")
    
