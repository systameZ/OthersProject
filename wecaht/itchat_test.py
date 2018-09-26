#coding=utf8
import itchat,time
from itchat.content import *
import urllib.request,urllib.parse
import http_request
#http://api.qingyunke.com/api.php?key=free&appid=0&msg=

'''
##自动回复的功能
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg['Text']
'''

@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
    #qyk=http_request.Qyk_robot()   #青云客API
    qyk=http_request.Tul_robot() #图灵
    response=qyk(msg['Text'])
    itchat.send('%s'%response,msg['FromUserName'])
    time.sleep(3)

@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s'%({'Picture':'img','Video':'vid'}.get(msg['Type'],'fil'),msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text'])# 该操作将自动将好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!',msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT,isGroupChat=True)
def text_reply(msg):
    if msg['isAt']:
        itchat.send(u'@%s\u2005I received: %s '%(msg['ActualNickName'],msg['Content']),msg['FromUserName'])


itchat.auto_login()
#users = itchat.search_friends(na)#search_mps，search_friends
#获取对方UserName
#print(users[0]['UserName'])
#向文件助手发送消息
#itchat.send('Are You OK! ',toUserName=users[0]['UserName'])
#itchat.send("@img@%s" % '',toUserName=users[0]['UserName'])
#itchat.send("@vid@%s" % '',toUserName=users[0]['UserName'])
#itchat.send("@fil@%s" % '',toUserName=users[0]['UserName'])
itchat.run()
