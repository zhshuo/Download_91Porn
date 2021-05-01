import requests
import threading
import os 
from video_no_by_user import get_all_video
class MyThread_Download_91(threading.Thread):
    def __init__(self, src,client_src,name):
        super(MyThread_Download_91, self).__init__()#  继承父类的__init__函数
        self.src=src
        self.client_src=client_src
        self.name=name

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
                ts_src=self.client_src+self.name+self.src
                self.mkdir(ts_src)
                with open(ts_src+"//"+str(fragment).rjust(10,'0')+".ts",'wb') as f:
                    f.write(r.content)
                fragment=fragment+1
            else:
                break

# number=438630
# number_end=number+20

def get_named_video_by_id(id,name):
    t = MyThread_Download_91(str(id), client_src, name)
    t.start()

# 运行程序
if __name__ == '__main__':


    client_src="D://资源//"
    videos=get_all_video()
    for x in videos:
        get_named_video_by_id(x,videos[x])
