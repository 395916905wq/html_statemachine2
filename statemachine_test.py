# coding:utf-8
from statemachine import StateMachine
from string import upper
import re
import os

def doctype_way(txt): #检验doctype
    sped_txt = txt.split( "<",1)[1].split(None,1) #分离字符串
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word =="!DOCTYPE":
        txt = sped_txt[1].lstrip()
        newstate = 'doctype_state' #到达完成doctype状态
    else:
        reason = 'watch the tags !DOCTYPE'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def doctype_state_way(txt): #检验doctype后面的html字符
    sped_txt = txt.split('>',1)
    word = sped_txt[0].upper().strip()
    t = len(txt.split("\n"))
    if word == 'HTML':
        txt = sped_txt[1].lstrip()
        newstate = 'dhtml_state' #到达完成第一个html状态
    else:
        reason = 'watch the tags !DOCTYPE HTML'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def dhtml_state_way(txt): #检验<html>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'HTML':
        txt = sped_txt[1].lstrip()
        newstate = 'shtml_state' #到达完成<html>状态
    else:
        reason = 'watch the tags HTML'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def shtml_state_way(txt): #检验<head>|<body>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'HEAD':
        txt = sped_txt[1].lstrip()
        newstate = 'shead_state' #到达完成<head>状态
    elif word =='BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'sbody_state' #到达完成<body>状态
    else:
        reason = 'watch the tags HEAD or BODY'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def shead_state_way(txt): #检验<title>|</head>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'TITLE':
        txt = sped_txt[1].lstrip()
        newstate = 'stitle_state' #到达完成<title>状态
    elif word =='/HEAD':
        txt = sped_txt[1].lstrip()
        newstate = 'ehead_state' #到达完成</head>状态
    else:
        reason = 'watch the tags TITLE OR /HEAD'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def stitle_state_way(txt): #检验</title>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == '/TITLE':
        txt = sped_txt[1].lstrip()
        newstate = 'etitle_state' #到达完成</title>状态
    else:
        reason = 'watch the tags /TITLE'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def etitle_state_way(txt): #检验</head>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == '/HEAD':
        txt = sped_txt[1].lstrip()
        newstate = 'ehead_state' #到达完成</head>状态
    else:
        reason = 'watch the tags /HEAD'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def ehead_state_way(txt): #检验<body>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'sbody_state' #到达完成<body>状态
    else:
        reason = 'watch the tags BODY'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def sbody_state_way(txt): #检验<p>|<a>|</body>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'P':
        txt = sped_txt[1].lstrip()
        newstate = 'sp_state' #到达完成<p>状态
    elif word[0] == 'A':
        txt = sped_txt[1].lstrip()
        newstate = 'sa_state' #到达完成<a>状态
    elif word =='/BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'ebody_state' #到达完成</body>状态
    else:
        reason = 'watch the tags P or A or /BODY'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def sp_state_way(txt): #检验</p>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == '/P':
        txt = sped_txt[1].lstrip()
        newstate = 'ep_state' #到达完成</p>状态
    else:
        reason = 'watch the tags /P'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def ep_state_way(txt): #检验<p>|<a>|</body>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'P':
        txt = sped_txt[1].lstrip()
        newstate = 'sp_state' #到达完成<p>状态
    elif word[0] == 'A':
        txt = sped_txt[1].lstrip()
        newstate = 'sa_state' #到达完成<a>状态
    elif word =='/BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'ebody_state' #到达完成</body>状态
    else:
        reason = 'watch the tags P or A or /BODY'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def sa_state_way(txt): #检验</a>
    sped_txt = txt.split('<',1)[1].split(">",1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == '/A':
        txt = sped_txt[1].lstrip()
        newstate = 'ea_state' #到达完成</a>状态
    else:
        reason = 'watch the tags /A'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-len(sped_txt[1].split("\n"))
    return (newstate,txt)

def ea_state_way(txt): #检验<p>|<a>|</body>
    sped_txt = txt.split('<',1)[1].split('>',1)
    word = sped_txt[0].upper()
    t = len(txt.split("\n"))
    if word == 'P':
        txt = sped_txt[1].lstrip()
        newstate = 'sp_state' #到达完成<p>状态
    elif word[0] == 'A':
        txt = sped_txt[1].lstrip()
        newstate = 'sa_state' #到达完成<a>状态
    elif word =='/BODY':
        txt = sped_txt[1].lstrip()
        newstate = 'ebody_state' #到达完成</body>状态
    else:
        reason = 'watch the tags P or A or /BODY'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i-t+1
    return (newstate,txt)

def ebody_state_way(txt): #检验</html>
    if '<' in txt:
        sped_txt = txt.split('<',1)[1].split('>',1)
        t = len(txt.split("\n"))
        if len(sped_txt)>1:
            word = sped_txt[0].upper()
        else:
            word=txt
        if word == '/HTML':
            txt = sped_txt[0]
            newstate = 'correct html file' #到达最终接受状态
        else:
            reason = 'watch the tags /HTML'
            newstate = 'wrong html file'
            print reason,'!','wrong row number: ', i-t+1
    else:
        reason = 'watch the tags /HTML'
        newstate = 'wrong html file'
        print reason,'!','wrong row number: ', i
    return (newstate,txt)



if __name__=='__main__': #主函数
    m = StateMachine() #定义类
    m.add_state('orig',doctype_way)
    m.add_state('doctype_state',doctype_state_way )
    m.add_state("dhtml_state",dhtml_state_way)
    m.add_state("shtml_state",shtml_state_way)
    m.add_state("shead_state",shead_state_way)
    m.add_state("stitle_state",stitle_state_way)
    m.add_state("etitle_state",etitle_state_way)
    m.add_state("ehead_state",ehead_state_way)
    m.add_state("sbody_state",sbody_state_way)
    m.add_state("sp_state",sp_state_way)
    m.add_state("ep_state",ep_state_way)
    m.add_state("sa_state",sa_state_way)
    m.add_state("ea_state",ea_state_way)
    m.add_state("ebody_state",ebody_state_way)
    m.add_state("correct html file",None,end_state=1)
    m.add_state("wrong html file", None, end_state=1)
    m.set_start('orig') #添加各种状态的方法
    dir = "./"
    for root, dirs, files in os.walk(dir):
        for name in files:
            global a_path
            a_path=os.path.join(root,name)
            print 'file: ',a_path
            file_lines = open(a_path).read()
            global i
            i = len(file_lines.split("\n"))
            m.run(file_lines) #读取文件
            relink = re.compile(r'<A href="(.*)".*>') #正则匹配url链接
            print 'URL:', relink.findall(open(a_path).read())
