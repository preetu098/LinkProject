 

import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()



cursor = cnxn.cursor()
r=requests.get('https://www.aip.ci/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

for x in soup.findAll("div", class_= "hk-listunit hk-listunit-small hk-listunit-child visual-img"):
    title = x.find('h4', class_='hk-listunit-title').get_text()
    myurl = x.find('h4', class_='hk-listunit-title').find('a')['href']
    t = x.find('div', class_='entry-featured-img-wrap').find('img', class_='attachment-thumbnail')['src']

    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    descr.append('')
    images.append(t)






for x in range(len(descr)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],24,1,today,url[x])

cnxn.commit()