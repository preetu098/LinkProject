import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()

cursor = cnxn.cursor()
r=requests.get('http://lestimes.com/category/news/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

primary = soup.find("div", id="uid_41d199e")

for x in primary.findAll("div", class_= "p-wrap p-grid p-grid-1"):
    
    title=x.find('h4', class_='entry-title').get_text()
    myurl=x.find('h4', class_='entry-title').find('a')['href']
    desc = x.find('p', class_='entry-summary').get_text().replace('\xa0', '')
    t = x.find('div', class_='p-featured').find('img', class_='featured-img wp-post-image')['src']
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    descr.append(desc.lstrip())
    images.append(t)

for x in range(len(images)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],25,1,today,url[x])

cnxn.commit()