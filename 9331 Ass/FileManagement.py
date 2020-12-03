'''
T3 COMP9331
YUAN GAO
z5239220 
'''
import os
import sys
import shutil
 
# Read "credentials.txt" registered
users = {}
fileName = open("credentials.txt")
line = fileName.readline()
while line:
    name, passWord = line.split(" ")
    passWord = passWord.rstrip('\n')
    users[name] = passWord
    line = fileName.readline()
fileName.close()

def GetuserDic():
    '''
    Get registered name dictionary
    '''
    return users

def CreateNewUser(name, passWord):
    '''
    Create a new user
    '''
    f = open("credentials.txt", "a")
    f.write(name + " " + passWord + "\n")
    users[name] = passWord
    f.close()
    return users

def CreateNewThread(filename, usrname, trd):
    '''
    Create a new thread
    '''
    f = open(filename, "a")
    f.write(usrname + " " + trd + "\n")
    f.close()

def ReadFile(filename):
    '''
    Read thread file list
    '''
    if not os.path.getsize(filename):
        return ""
    else:
        f = open(filename)
        txt = ""
        line = f.readline()
        while line:
            usr, trd = line.split(" ")
            txt += trd
            line = f.readline()
        f.close()
        txt = txt.rstrip('\n')
    return txt

def ReadMsg(filename):
    '''
    Read message of thread list
    '''
    if not os.path.getsize(filename):
        return ""
    else:
        f = open(filename)
        txt = []
        line = f.readline()
        while line:
            tmp = line.split(" ")
            txt.append(tmp)
            line = f.readline()
        f.close()
    return txt

def WriteMsg(filename, num, usrname, msg):
    '''
    Write massage on thread file
    '''
    f = open(filename, "a")
    f.write(num + " " + usrname + ": " + msg + "\n")
    f.close()

def rewriteMsg(filename, txt):
    '''
    Edit massafe on thread file
    '''
    f = open(filename, "w") 
    for value in range(len(txt)):
        tmp = " ".join(txt[value][2:])
        f.write(str(value + 1) + " " + txt[value][1] + " " + tmp)
    f.close()

def delAllFile():
    '''
    Delete all of file when run 'SHT'
    '''
    try:
        shutil.rmtree('forum')
        return True
    except Exception:
        return False

    