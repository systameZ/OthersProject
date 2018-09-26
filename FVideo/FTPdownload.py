import win32com
import urllib.request
import re
import random
import os
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory

class gui():
    def __init__(self,root):
        self.root=root
        self.input()
    def input(self):
        self.botom=LabelFrame(self.root)
        self.botom.grid(row=1,column=0,padx=15,pady=2)
        self.lab_notice=Label(self.botom,text="服务器格式：248,249,250 || 日期格式：20170508")
        self.lab_notice.grid(row=1,column=0,padx=15,pady=2,sticky="e",columnspan=2)

        """self.path = StringVar()
        self.path_Label=Label(self.botom,text = "目标路径:").grid(row = 2, column = 0,padx=15,pady=2,sticky="e")
        self.path_Entry=Entry(self.botom, textvariable = self.path,bd=2).grid(row = 2, column = 1,padx=15,pady=2)
        self.path_Button=Button(self.botom, text = "路径选择", command = self.selectPath,relief=SOLID,bd=2).grid(row = 2, column = 2,padx=15,pady=2)
        """


        self.lab_server=Label(self.botom,text="输入服务器：")
        self.lab_server.grid(row=3,column=0,padx=15,pady=2,sticky="e")
        self.intext_server_var=StringVar()
        self.intext_server=Entry(self.botom,bd=2,textvariable=self.intext_server_var)
        self.intext_server.grid(row=3,column=1,padx=15,pady=2)
        self.lab_num=Label(self.botom,text="输入视频个数：")
        self.lab_num.grid(row=4,column=0,padx=15,pady=2,sticky="e")
        self.intext_num_var=StringVar()
        self.intext_num=Entry(self.botom,bd=2,textvariable=self.intext_num_var)
        self.intext_num.grid(row=4,column=1,padx=15,pady=2)

        self.lab_day=Label(self.botom,text="输入日期：")
        self.lab_day.grid(row=5,column=0,padx=15,pady=2,sticky="e")
        self.intext_day_var=StringVar()
        self.intext_day=Entry(self.botom,bd=2,textvariable=self.intext_day_var)
        self.intext_day.grid(row=5,column=1,padx=15,pady=2)

        
        self.btn=Button(self.botom,text="确认",relief=SOLID,bd=2,width=10,command=self.show_info)
        self.btn.grid(row=6,column=1,padx=15,pady=2,sticky="e")
    def show_info(self):
        try:
            server=self.intext_server_var.get()
            num=self.intext_num_var.get()
            server_list=['248','249','250']
            if server in server_list:
                link="http://10.80.28."+server+":8080"
            else:
                link="http://10.80.28."+"249"+":8080"
                messagebox.showinfo('Python Tkinter', '输入的服务器不正确，将下载249服务器视频')
            nowday=self.intext_day_var.get()
            messagebox.showinfo('Python Tkinter', '正在下载，请勿关闭')
            cleardir()
            lin=get_link_file(get_html(link,nowday,"nowday"))
            down_list=get_random_link(lin,make_random(len(lin),int(num)))
            save_file(link,down_list)
            messagebox.showinfo('Python Tkinter', '下载完成')
        except Exception as e:
            messagebox.showinfo('Python Tkinter',"出现错误"+str(e))
    def selectPath(self):
          path_ = askdirectory()
          self.path.set(path_)
        

def get_html(url_in,search,mode):#mode分搜索和当日，search和nowday(20170508格式)
    url_top = url_in
    if mode=="search":
        url =url_in+"/?search="+search
    elif mode=="nowday":
        url= url_in+"/F%3A/"+search
    auth = urllib.request.HTTPBasicAuthHandler()#basic认证模式
    auth.add_password("Everything",url_top,"alog","alog")  
    opener = urllib.request.build_opener(auth)  
    urllib.request.install_opener(opener)  
    res_data = urllib.request.urlopen(url)  
    res = res_data.read().decode("utf-8")
    return res
def get_link_file(html):
    html=html
    sel=re.compile('/F.*?.flv')
    href=sel.findall(html)
    if href:
        return href
    else:
        return "notfindlink"
def make_random(len_link,link_num):
    num=range(int(len_link))
    ran=random.sample(num,link_num)
    num=list(set(ran))
    return num
def get_random_link(link_file,random):
    nile_list=[]
    for i in random:
        nile_list.append(link_file[i])
    return nile_list
def down_file(link,down_link):
    download=link+down_link
    f=urllib.request.urlopen(download)
    data=f.read()
    return data
def save_file(link,down):
    os.makedirs("video")
    for i in down:
        write=open(("video\\"+i.split("/")[3]),"wb")
        write.write(down_file(link,i))
        write.close()
def cleardir():
    if os.path.exists("video"):
        list_dir=os.listdir("video")
        for i in list_dir:
                os.remove("video\\"+i)
        os.rmdir("video")
if __name__=="__main__":
    try:
        root=Tk()
        root.title("视频下载")
        gui(root)
        root.mainloop()
    except Exception as e:
        print(e)
    
