import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today() 
cursor = cnxn.cursor()
r=requests.get('http://eldjazairmag.com/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

primary = soup.find("div", id="recent-news")

for x in primary.findAll("div", class_='status-publish'):
    title = x.find('h2', class_='title').get_text()
    myurl = x.find('h2', class_='title').find('a')['href']
    desc = x.find('div', class_='entry').get_text().replace('\n', '')
    t = x.find('img', class_='woo-image')['src']

    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    descr.append(desc.lstrip())
    images.append(t)

for x in range(len(images)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],1,1,today,url[x])

cnxn.commit()