import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog

today = date.today()

try: 
    cursor = cnxn.cursor()
    r=requests.get('http://abidjantv.net/', headers= {'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")

    titles=[]
    descr=[]
    images=[]
    url=[]

    for x in soup.findAll("div", class_="widget-content"):
        title = x.find('h2', class_='entry-title').get_text().lstrip().rstrip()
        myurl = x.find('h2', class_='entry-title').find('a')['href']
        desc = x.find('div', class_='entry-excerpt').get_text().lstrip().rstrip().replace('\r\n\t\t', '').replace('\t','')
        if(x.find('a').find('img') is None):
            t = ''
        else:
            t = x.find('a').find('img')['data-lazy-src']

        titles.append(title)
        url.append(myurl)
        descr.append(desc)
        images.append(t)

    for x in range(len(titles)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],24,1,today,url[x])

    cnxn.commit()
    
except Exception as e:
    printErrorLog(__file__.split('\\').pop(), e)