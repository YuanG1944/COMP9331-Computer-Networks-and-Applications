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
import FTclient
import FTserver


class Client:
    """
    Client
    """
    
    def __init__(self, addr, port_num):
        """
        init:
        :param addr: IP address
        :param port_num: Port number
        """
        self.__address = addr
        self.__port = port_num
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP protocol
        self.__id = None  # thread ID
        self.intro = '\nEnter one of the following commands: \n(CRT, MSG, DLT, EDT, LST, RDT, UPD, DWN, RMV, XIT, SHT):'

    def receive_message_thread(self):
        """
        Receive thread message and processing
        """
        while True:
            try:
                buffer = self.__socket.recv(1024).decode()
                obj = json.loads(buffer)
                print(obj['message'])

                # obj["up_down"] -> contrl the client download command
                if obj["up_down"] != "False":
                    FTclient.up_load("", obj["up_down"])
                    print(f"{obj['sender_nickname']} downloaded from {obj['trd']} thread")
            except Exception:
                print('Goodbye')
                os._exit(0)


    def __send_message_thread(self, message):
        """
        Send thread message and processing
        :param message: message infomation

        Using josn send message
        """
        # Split string to list according to " "
        message_list = message.split(" ")

        # Sending different command
        if(message_list[0] == "CRT"):
            if len(message_list) == 1:
                self.__socket.send(json.dumps({
                    'type': 'CRT',
                    'len': 1,
                    'sender_id': self.__id,
                    'trd': " ",
                    'message': "Incorrect syntax for " + message_list[0] + "\n"
                }).encode())
            else:
                self.__socket.send(json.dumps({
                    'type': 'CRT',
                    'len': 2,
                    'sender_id': self.__id,
                    'trd': " ",
                    'message': message_list[1]
                }).encode())
        elif(message_list[0] == "MSG"):
            if len(message_list) < 3:
                self.__socket.send(json.dumps({
                    'type': 'MSG',
                    'len': 2,
                    'sender_id': self.__id,
                    'forum': "",
                    'trd': " ",
                    'message': "Incorrect syntax for " + message_list[0] + "\n"
                }).encode())
            else:
                msg = ' '.join(message_list[2:])
                self.__socket.send(json.dumps({
                    'type': 'MSG',
                    'len': 3,
                    'sender_id': self.__id,
                    'trd': message_list[1],
                    'message': msg
                }).encode())
        elif(message_list[0] == "DLT"):
            if len(message_list) < 3:
                self.__socket.send(json.dumps({
                    'type': 'DLT',
                    'len': 2,
                    'sender_id': self.__id,
                    'trd': " ",
                    'message': "error"
                }).encode())
            else:
                self.__socket.send(json.dumps({
                    'type': 'DLT',
                    'len': 3,
                    'sender_id': self.__id,
                    'trd': message_list[1],
                    'num': message_list[2]
                }).encode())
        elif(message_list[0] == "EDT"):
            if len(message_list) < 4:
                self.__socket.send(json.dumps({
                    'type': 'EDT',
                    'len': 1,
                    'sender_id': self.__id,
                    'trd': " ",
                    'message': "error"
                }).encode())
            else:
                msg = ' '.join(message_list[3:])
                self.__socket.send(json.dumps({
                    'type': 'EDT',
                    'len': 4,
                    'sender_id': self.__id,
                    'trd': message_list[1],
                    'num': message_list[2],
                    "message": msg
                }).encode())
        elif(message_list[0] == "LST"):
            if len(message_list) == 1:
                self.__socket.send(json.dumps({
                    'type': "LST",
                    'len': 1,
                    'sender_id': self.__id,
                    'message': " ",
                    'trd': " "
                }).encode())
            else:
                self.__socket.send(json.dumps({
                    'type': 'LST',
                    'len': 2,
                    'sender_id': self.__id,
                    'trd': " ",
                }).encode())
        elif(message_list[0] == "RDT"):
            if len(message_list) == 2:
                self.__socket.send(json.dumps({
                    'type': 'RDT',
                    'len': 2,
                    'sender_id': self.__id,
                    'trd': message_list[1],
                }).encode())
            else:
                self.__socket.send(json.dumps({
                    'type': 'RDT',
                    'len': 1,
                    'sender_id': self.__id,
                    'trd': " ",
                }).encode())
        elif(message_list[0] == "UPD"):
            if len(message_list) == 3:
                self.__socket.send(json.dumps({
                    'type': 'UPD',
                    'len': 3,
                    'sender_id': self.__id,
                    'trd': message_list[1],
                    'filename': message_list[2]
                }).encode())
                print(f"{message_list[2]} uploaded to {message_list[1]} thread")
                filename = "forum/" + message_list[1] + "/" + message_list[1] + "-" + message_list[2]

                # Start file transmition server
                FTserver.download(filename)
            else:
                self.__socket.send(json.dumps({
                    'type': 'UPD',
                    'len': 1,
                    'sender_id': self.__id,
                    'trd': " ",
                }).encode())
        elif(message_list[0] == "DWN"):
            if len(message_list) == 3:
                self.__socket.send(json.dumps({
                    'type': 'DWN',
                    'len': 3,
                    'sender_id': self.__id,
                    'trd': message_list[1],
                    'filename': message_list[2]
                }).encode())
            else:
                self.__socket.send(json.dumps({
                    'type': 'DWN',
                    'len': 1,
                    'sender_id': self.__id,
                    'trd': " ",
                }).encode())
        elif(message_list[0] == "RMV"):
            if len(message_list) == 2:
                self.__socket.send(json.dumps({
                    'type': 'RMV',
                    'len': 2,
                    'sender_id': self.__id,
                    'trd': message_list[1],
                }).encode())
            else:
                self.__socket.send(json.dumps({
                    'type': 'RMV',
                    'len': 1,
                    'sender_id': self.__id,
                    'trd': " ",
                }).encode())
        elif(message_list[0] == "XIT"):
            self.__socket.send(json.dumps({
                'type': "XIT",
                'len': 1,
                'sender_id': self.__id,
                'message': " "
            }).encode())
            return 0
        elif(message_list[0] == "SHT"):
            if len(message_list) == 2:
                self.__socket.send(json.dumps({
                    'type': 'SHT',
                    'len': 2,
                    'sender_id': self.__id,
                    'password': message_list[1],
                    'trd': " "
                }).encode())
            else:
                self.__socket.send(json.dumps({
                    'type': 'SHT',
                    'len': 1,
                    'sender_id': self.__id,
                    'trd': " ",
                }).encode())    
        elif(message_list[0] == "loop"):
            pass
        else:
            print("Invalid command")
        return 1
        
    def do_login(self):
        """
        Login forum
        """

        NAME = "___none"
        self.__socket.connect((self.__address, int(self.__port)))
        ifmess = "False"
        while ifmess == "False":
            user_name = input('Enter username: ')
            self.__socket.send(json.dumps({
                'type': 'login',
                'nickname': user_name
            }).encode())

            # Receve name verify information
            buffer = self.__socket.recv(1024).decode()
            welmess = json.loads(buffer)
            if welmess['type'] == 'name correct':
                pass_word = input('Enter password: ')
                self.__socket.send(json.dumps({
                    'password': pass_word
                }).encode())
                buffer = self.__socket.recv(1024).decode()
                welmess = json.loads(buffer)
                self.__socket.send(json.dumps({
                    'type': 'login',
                    'nickname': "connect"
                }).encode())
                if welmess['isvalid'] == "True":
                    ifmess = "True"
                    NAME = user_name
                else:
                    print("Wrong PassWord, please try again")

            # If Receve name not in dic, register a new one
            elif welmess['type'] == 'name invalid':
                ifmess = "True"
                print('Do you want to create this account?(yes/no): ')
                valid = input()
                self.__socket.send(valid.encode())
                if valid == "yes":
                    NAME = user_name
                    # Please enter your new password: 
                    print(self.__socket.recv(1024).decode())
                    new_password = input('')
                    self.__socket.send(new_password.encode())
                    # Welcome to the forum
                    print(self.__socket.recv(1024).decode())
                    self.__socket.send(b'connect')
                else:
                    return False
            elif welmess['type'] == 'error':
                print(f"{user_name} has already logged in")


        # usrername and password verified successfully
        # Try to create new thread and receve message
        os.system("clear") #clear shell
        print("Welcome to the forum")
        if NAME != "___none":
            try:
                buffer = self.__socket.recv(1024).decode()
                obj = json.loads(buffer)
                if obj['id']:
                    self.__id = obj['id']

                    # Create subthread using recive message
                    thread = threading.Thread(target=self.receive_message_thread)
                    thread.setDaemon(True)
                    thread.start()
                    return True
                else:
                    print('Cannot log in to chat room')
            except Exception:
                print('Unable to get data from server')

    def do_send(self, mention):
        """
        Send message
        :param mention:  = self.intro
        """

        while True:
            # Sometimes the result will appear befor self.intro, therefore using sleep() make sure result appear first
            time.sleep(0.1)
            
            print(mention)
            message = input()

            # Create subthread to send message
            thread = threading.Thread(target=self.__send_message_thread, args=(message,))
            thread.setDaemon(True)
            thread.start()


    def start(self):
        """
        Start the client
        """
        # 1. login
        flag = self.do_login()
        # 2. loop forum
        if flag == True:
            self.do_send(self.intro)


if __name__ == "__main__":
    try:
        addr = sys.argv[1]  # IP address
        port = sys.argv[2]  # port

        client = Client(addr, port)
        client.start()
    except OSError:
        print("Address or port already in use")
    except Exception:
        print("Incorrect syntax for starting client")