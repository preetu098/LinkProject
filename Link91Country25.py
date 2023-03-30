import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()
 
cursor = cnxn.cursor()
r=requests.get('https://www.tuko.co.ke/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

for x in soup.findAll("article", class_= "c-article-card-with-badges l-card-collection-section__item"):
    title = x.find('a', class_='c-article-card-with-badges__headline').get_text().replace('\n', '')
    myurl = x.find('a', class_='c-article-card-with-badges__headline')['href']
    t = x.find('div', class_='thumbnail-picture c-article-card-with-badges__image').find('img')['src']
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    descr.append('')
    images.append(t)

for x in range(len(url)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],25,1,today,url[x])

cnxn.commit()