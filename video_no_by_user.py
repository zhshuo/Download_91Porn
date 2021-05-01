import requests
from bs4 import BeautifulSoup
import re
UID='aae8Wji4m8HxTnHxsKELfBKgGTYB3mwHKKf8Uxr8g1zSqvqR'

def url_public_video(uid,num=1):
    if num==1:
        return r"http://91porn.com/uvideos.php?UID="+UID+"&type=public"
    else:
        return r"http://91porn.com/uvideos.php?UID="+UID+"&type=public&page="+str(num)

def get_all_video(uid=UID):
    res={}
    i=1
    while True:
        try:
            flag=True
            name=[]
            id=[]
            url=url_public_video(uid,i)
            data=requests.get(url)
            bs=BeautifulSoup(data.text)
            body=bs.body
            #print(body)
            for x in body.find_all("span",{"class":"video-title title-truncate m-t-5"}):
                name.append(str(x).split(">")[1].split("<")[0])
            for x in body.find_all("div",{"class":"thumb-overlay"}):
                id.append(int(str(x.find("img")["src"]).split(".")[-2].split("/")[-1]))
            for j,x in enumerate(id):
                if x in res:
                    flag=False
                res[x]=name[j]
            i+=1
            if flag==False:
                break
        except:
            break
    return res

if __name__=="__main__":
    #print(get_all_video(UID))
    print(len(get_all_video(UID)))