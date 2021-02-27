import requests
import threading
import os 

class MyThread_Download_91(threading.Thread): 
    def __init__(self, src,client_src): 
        super(MyThread_Download_91, self).__init__()#  继承父类的__init__函数
        self.src=src
        self.client_src=client_src

    def mkdir(self,path):
        path=path.strip()
        path=path.rstrip("\\")
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path) 
            return True
        else:
            return False

    def run(self):
        base_dir="https://cdn.91p07.com//m3u8/"
        fragment=0
        while True:
            url = base_dir+self.src+"//"+self.src+str(fragment)+".ts"
            print(url)
            r = requests.get(url) 
            if r.ok==True:
                ts_src=self.client_src+self.src
                self.mkdir(ts_src)
                with open(ts_src+"//"+str(fragment).rjust(10,'0')+".ts",'wb') as f:
                    f.write(r.content)
                fragment=fragment+1
            else:
                break

# number=438630
# number_end=number+20

# 运行程序
if __name__ == '__main__':

    # number 6位整数，后三位可以修改，50为一次下多少部片。
    # client_src:下载后保存在本地什么位置。
    number=428330
    number_end=number+50
    client_src="D://资源//"

    while True:

        t=MyThread_Download_91(str(number),client_src)
        t.start()
        number=number+1
        if number==number_end:
            break
