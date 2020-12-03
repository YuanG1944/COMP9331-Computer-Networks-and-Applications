'''
T3 COMP9331
YUAN GAO
z5239220 
'''

import sys
import os 
import shutil
import FileManagement

class ForumCommad:
    '''
    Operate forum command
    '''
    def __init__(self):
        self.conmmand_list = ["CRT", "MSG", "DLT", "EDT", "LST", "RDT", "UPD", "DWN", "RMV", "XIT", "SHT"]
    
    def not_conmmad(self, comm):
        '''
        Determine whether command is correct
        '''
        if(comm in self.conmmand_list):
            return False
        else:
            return True
    
    def create_thread(self, username, threadtitle):
        '''
        Create new forum thread
        '''
        filename = 'forum/' + threadtitle
        writefile = 'forum/forumList'
        if not os.path.exists(filename):
            os.makedirs(filename)
            filename = 'forum/' + threadtitle + "/" + threadtitle
            os.system(r"touch {}".format(filename))
            FileManagement.CreateNewThread(writefile, username, threadtitle)
            return True
        else:
            return False

    def post_message(self, username, threadtitle, msg):
        '''
        Write message in current thread
        '''
        filename = 'forum/' + threadtitle + "/" + threadtitle
        if not os.path.exists(filename):
            return False
        else:
            txt = FileManagement.ReadMsg(filename)
            if txt == "":
                FileManagement.WriteMsg(filename, "1", username, msg)
            else:
                tmp = txt[-1][0]
                num = str(int(tmp) + 1)
                FileManagement.WriteMsg(filename, num, username, msg)
            return True

    def edit_message(self, username, threadtitle, num, msg):
        '''
        Edit message in current thread
        '''
        filename = 'forum/' + threadtitle + "/" + threadtitle
        if not os.path.exists(filename):
            return False
        else:
            try:
                txt = FileManagement.ReadMsg(filename)
                num = int(num) - 1
                if username == txt[num][1][:-1]:
                    del txt[num][2:]
                    msg = msg + "\n"
                    txt[num].append(msg)
                    FileManagement.rewriteMsg(filename, txt)
                    return True
                else:
                    return False
            except Exception:
                return False

    def del_message(self, username, threadtitle, num):
        '''
        Delete message in current thread
        '''
        filename = 'forum/' + threadtitle + "/" + threadtitle
        if not os.path.exists(filename):
            return False
        else:
            try:
                txt = FileManagement.ReadMsg(filename)
                num = int(num) - 1
                if username == txt[num][1][:-1]:
                    del txt[num]
                    FileManagement.rewriteMsg(filename, txt)
                    return True
                else:
                    return False
            except Exception:
                return False

    def read_thread(self, threadtitle):
        '''
        Read message in current thread
        '''
        filename = 'forum/' + threadtitle + "/" + threadtitle
        if not os.path.exists(filename):
            return "False"
        else:
            try:
                res = ""
                txt = FileManagement.ReadMsg(filename)
                for value in txt:
                    tmp = " ".join(value)
                    res += tmp
                return res
            except Exception:
                return "False"
                

    def list_threads(self):
        '''
        List exist thread
        '''
        writefile = "forum/forumList"
        txt = FileManagement.ReadFile(writefile)
        if txt == "":
            mess = "No threads to list"
            return mess
        else:
            mess = "The list of active threads:\n"
            mess += txt
            return mess


    def delete_threads(self, createname, threadtitle):
        '''
        Delete exist thread
        '''
        totalinfo = createname + " " + threadtitle
        if not os.path.getsize('forum/forumList'):
            return "False"
        else:
            try:
                f = open('forum/forumList')
                txt = []
                line = f.readline()
                while line:
                    tmp, t = line.rsplit('\n')
                    txt.append(tmp)
                    line = f.readline()
                f.close()
                if totalinfo in txt:
                    num = txt.index(totalinfo)
                    del txt[num]
                    rmdir = "forum/" + threadtitle
                    shutil.rmtree(rmdir)
                    f = open('forum/forumList', "w") 
                    for value in txt:
                        f.write(value + "\n")
                    f.close()
                    return "True"
            except Exception:
                return "False"


# if __name__ == "__main__":
#     f = ForumCommad()
#     a = f.delete_threads("aaa", "测试")
#     print(a)
#     # f.edit_message("asd", "AAA", "2", "改内容")
#     # f.del_message("asd", "AAA", "2")
#     # f.read_thread("AAA")

            
    