import urllib.request,urllib.parse
import requests
#http://api.qingyunke.com/api.php?key=free&appid=0&msg=
#http://www.tuling123.com/openapi/api?key=7403046cfcc8423db07e52b4745db18e&info=%E4%BD%A0%E5%A5%BD
class Qyk_robot:
    def __call__(self,str):
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
class Tul_robot:
    def __call__(self,str):
        query = {
            'key': '',#使用key
            'info' : str
        }
        response=requests.get( 'http://www.tuling123.com/openapi/api',params=query)
        return self.splite(response.content.decode('utf-8'))
    def splite(self,str):
        str_list=str.split(':',2)
        return  str_list[2][1:-2]

if __name__== '__main__' :
     qyk=Qyk_robot()
     print(qyk('不言不语，我在这里'))