#https://anacao.cv/ 





import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()


cursor = cnxn.cursor()
r=requests.get('https://anacao.cv/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("ul", class_= "blog-widget-list left relative"):
    title=x.find('div', 'blog-widget-text left relative').find('h2').get_text()
    myurl=x.find('a')['href']
    
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # # # # print("...................................................")

for x in soup.findAll("ul", class_= "blog-widget-list left relative"):
    print(x.find('div', 'blog-widget-text left relative').find('p').get_text())
    descr.append(x.find('div', 'blog-widget-text left relative').find('p').get_text().lstrip())
  
for x in soup.findAll('ul',class_="blog-widget-list left relative"):
    t=x.find('div', 'blog-widget-img left relative').find('img')['data-src']
    images.append(t)
    

for x in range(len(descr)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],8,1,today,url[x])

cnxn.commit()
