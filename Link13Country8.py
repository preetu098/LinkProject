#http://yaoundeinfo.com/
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog
today = date.today()

try:
    cursor = cnxn.cursor()
    r=requests.get('https://inforpress.cv/category/politica-pt/',headers={'User-Agent': 'newsroom'})
    soup = BeautifulSoup(r.content, "html.parser")
    titles=[]
    descr=[]
    images=[]
    url=[]

    for x in soup.select('div.elementor-post__text'):
        if(x.h3 is not None):
            title = x.h3.get_text().lstrip().rstrip()
            myurl = x.a['href']
            desc = x.p.get_text().lstrip().rstrip()
            t = x.previous_element.parent.img['src']

            titles.append(title)
            url.append(myurl)
            descr.append(desc)
            images.append(t)

    for x in range(len(titles)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],8,1,today,url[x])

    cnxn.commit()
    
except Exception as e:
    printErrorLog(__file__.split('\\').pop(), e)    