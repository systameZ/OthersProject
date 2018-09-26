import requests,csv
users=[]
def reque(id):
    date={'DDDDD':id,'upass':'a82d0bc0a9695b22269f9c8092db3c40123456782','0MKKey':'123456','R1':'0','R2':'1','para':'00'}
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0',
    }
    url='http://192.168.2.5/0.htm'
    req=requests.session()
    req.headers=header
    response=req.post(url,data=date)
    index=response.text.find('msga')
    ret=response.text[786:792]
    if ret=='error1':
        users.append(id)
for i in range(197000,198100,1):
    print(i)
    reque(i)
write=csv.writer(open('users.csv','w',newline=""))
for k in users:
        write.writerow([k])