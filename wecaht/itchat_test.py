import itchat,time
#
# def lc():
#     print("Finash")
# def ec():
#     print("logout")
# @itchat.msg_register(itchat.content.PICTURE)
# def text_reply(msg):
#     print(msg)
#     itchat.send(msg['Picture'],msg['FromUserName'])
# itchat.auto_login(hotReload=True)
# itchat.run()

#coding=utf8
import itchat,time
from itchat.content import *
import urllib.request,urllib.parse
import http_request
#http://api.qingyunke.com/api.php?key=free&appid=0&msg=
class Qyk_robot:
    def __call__(self,str):
        str = '你好'
        query = {
            'key': 'free',
            'appid': '0',
            'msg': str
        }
        req_str = 'http://api.qingyunke.com/api.php?' + urllib.parse.urlencode(query)
        req = urllib.request.Request(req_str)
        response = urllib.request.urlopen(req)
        content = self.splite(response.read().decode('utf-8'))
        return content
    def splite(self,str):
        str_list=str.split(':')
        return  str_list[2][1:-2]
'''
##自动回复的功能
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg['Text']
#http://api.qingyunke.com/api.php?key=free&appid=0&msg=
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