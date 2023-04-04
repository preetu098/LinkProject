#https://www.mmegi.bw/
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog
today = date.today()

try: 
    cursor = cnxn.cursor()
    r=requests.get('https://www.mmegi.bw/' , headers={'User-Agent': 'newsroom'})
    soup = BeautifulSoup(r.content, "html.parser")

    titles=[]
    descr=[]
    images=[]
    url=[]

    for x in soup.find("div","mmegi-side-vertical-articles").findAll("div", 'row row2'):
        if(x.h2 is not None):
            title=x.h2.get_text().lstrip().rstrip()
            myurl=x.a['href']
            if(x.p is not None):
                desc = x.p.get_text().lstrip().rstrip()
            else:   
                desc = '' 
            if(x.picture.select_one('source:nth-of-type(2)') is not None):
                t = x.picture.select_one('source:nth-of-type(2)')['data-srcset']
            else:   
                t = ''

            titles.append(title.lstrip())
            url.append(myurl.lstrip())
            descr.append(desc)
            images.append(t)

    for x in range(len(titles)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],4,1,today,url[x])
    cnxn.commit()

except Exception as e:
    printErrorLog(__file__.split('\\').pop(), e)