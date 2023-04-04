import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog
today = date.today()

try:
    cursor = cnxn.cursor()
    r=requests.get('https://www.jeune-independant.net/', headers= {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")

    titles=[]
    descr=[]
    images=[]
    url=[]

    for x in soup.select("li.d-f.fxd-c"):
        if(x.h3 and x.img is not None):
            title = x.h3.get_text().lstrip().rstrip()
            myurl =x.a['href']
            t = x.img['src']
            
            titles.append(title)
            url.append(myurl)
            descr.append('')
            images.append(t)

    for x in range(len(titles)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],1,1,today,url[x])

    cnxn.commit()
    
except Exception as e:
    printErrorLog(__file__.split('\\').pop(), e)