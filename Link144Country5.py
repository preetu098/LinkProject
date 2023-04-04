import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog, printErrorLog
today = date.today()
try:
    cursor = cnxn.cursor()
    hdr = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get('https://www.sidwaya.info/',headers=hdr)     
    soup = BeautifulSoup(r.content, "html.parser")

    titles=[]
    descr=[]
    images=[]
    url=[]

    for x in soup.find('div', id = 'tdi_44').findAll("div", 'td-animation-stack'):
        title = x.find('h3','entry-title').get_text().lstrip().rstrip()
        myurl = x.find('h3','entry-title').find('a')['href']
        t = x.find('div', 'td-module-thumb').find('span', 'entry-thumb')['data-img-url']

        titles.append(title)
        url.append(myurl)
        descr.append('')
        images.append(t)

    for x in range(len(titles)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],5,1,today,url[x])

    cnxn.commit()
except Exception as e:
    printErrorLog("Link144Country5", e)   