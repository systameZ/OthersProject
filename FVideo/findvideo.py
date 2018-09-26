import win32com
import urllib.request
import re
import os
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory,askopenfilename
from tkinter import ttk
class gui():
    def __init__(self,root):
        self.root=root
        self.input()
    def input(self):
        self.botom=LabelFrame(self.root)
        self.botom.grid(row=1,column=0,padx=15,pady=2)
        self.path = StringVar()
        self.path_Label=Label(self.botom,text = "目标路径:").grid(row = 1, column = 0,padx=15,pady=2,sticky="e")
        self.path_Entry=Entry(self.botom, textvariable = self.path,bd=2).grid(row = 1, column = 1,padx=15,pady=2)
        self.path_Button=Button(self.botom, text = "路径选择", command = self.selectPath,relief=SOLID,bd=2).grid(row = 1, column = 2,padx=15,pady=2)
        self.lable_search_var=StringVar()
        self.lable_search_var.set('请输入搜索内容：')
        self.lable_search=Label(self.botom,textvariable=self.lable_search_var).grid(row=2,column=0,padx=15,pady=2,sticky="e")
        self.input_search_var=StringVar()
        self.input_search=Entry(self.botom,bd=2,textvariable=self.input_search_var).grid(row=2,column=1,padx=15,pady=2)
        self.xlsx_Button = Button(self.botom, text="批量导入", command=self.selectxlsx, relief=SOLID, bd=2).grid(row=2,column=2,padx=15,pady=2)
        self.checkvar=IntVar()
        self.check=Checkbutton(self.botom,text="下载",variable=self.checkvar).grid(row=3,column=0,sticky='e')
        self.btn=Button(self.botom,text="确认",relief=SOLID,bd=2,width=10,command=self.show_info)
        self.btn.grid(row=3,column=1,padx=15,pady=2,sticky="e")
        
    def show_info(self):
       # try:
            save_path=self.path.get()
            search_content=self.input_search_var.get()
            link=["http://10.80.28.248:8080","http://10.80.28.249:8080","http://10.80.28.250:8080"]
            get_ip=[]
            get_link=[]
            for i in link:
                lin=get_link_file(get_html(i,search_content,"search"))
                if lin!="notfindlink":
                    for add in lin:
                        get_link.append(i+add)
                        get_ip.append(link.index(i))
            get_ip=list(set(get_ip))
            ip="  "
            for p in get_ip:
                ip=ip+link[p]+"   "
            if self.checkvar.get()==1: 
                messa=("共有"+str(len(get_link))+"个搜索结果正从"+i+"下载，请勿关闭主程序")
                messagebox.showinfo('提示！', messa)
            elif self.checkvar.get()==0:
                messa_false=("共有"+str(len(get_link))+"个搜索结果位于"+ip)
                messagebox.showinfo('提示！', messa_false)
            if len(get_link)>0 and self.checkvar.get()==1:
                save_file(get_link,save_path)
                messagebox.showinfo('提示！', "下载完成")
            
                   
        
    def selectPath(self):
          path_ = askdirectory()
          self.path.set(path_)
    def selectxlsx(self):
        xlsx_=askopenfilename(filetypes=[('Excel files','*.xlsx;*.xls')])
        self.lable_search_var.set('批量导入文件：')
        self.input_search_var.set(xlsx_)
def read_xlsx(path):
    workbook=xlrd.open_workbook(path)
    booksheet=workbook.sheet_by_index(0)
    ret_list=[]
    try:
            for row in range(booksheet.nrows):
                    ret_list.append(str(booksheet.cell(row,0).value))
    except Exception as e:
        return 'Error:'+str(e)
    return ret_list

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


def save_file(link,save_path):
    for i in link:
        write=open((str(save_path)+"/"+i.split("/")[5]),"wb")
        write.write(down_file(i))
        write.close()

def down_file(link):
    auth = urllib.request.HTTPBasicAuthHandler()#basic认证模式
    auth.add_password("Everything",link,"alog","alog")  
    opener = urllib.request.build_opener(auth)  
    urllib.request.install_opener(opener)
    f=urllib.request.urlopen(link)
    data=f.read()
    return data

if __name__=="__main__":
    try:
        root=Tk()
        root.title("视频搜索")
        gui(root)
        root.mainloop()
    except Exception as e:
        print(e)


