import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()

cursor = cnxn.cursor()
#r=requests.get('https://garoweonline.com/en/')  Right Clikc and Developer Toolbar disabled
r=requests.get('https://hiiraan.com/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("div", class_= "featured-story2"):
    title=x.find('div', class_='title').find('a').get_text()
    myurl='https://hiiraan.com'+x.find('div', class_='title').find('a')['href']
    t='https://hiiraan.com/'+x.find('div', class_='image').find('a').find('img')['src']
    desc = ''
    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    images.append(t)
    descr.append(desc)

for x in range(len(titles)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],'',images[x],44,1,today,url[x])

cnxn.commit()