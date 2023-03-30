



import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()



cursor = cnxn.cursor()
r=requests.get('https://publiceyenews.com/category/news/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

primary = soup.find("div", {"id": "primary"})

for x in primary.findAll("h3", class_= "article-title"):
    title=x.get_text()
    myurl=x.find('a')['href']
    
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # # # # print("...................................................")

for x in primary.findAll("div",class_="post-description"):
    
    descr.append(x.get_text().lstrip())
  
for x in primary.findAll('div',class_="data-bg-hover"):
    t=x.find('img')['src']
    images.append(t)
    

for x in range(len(titles)):
    cursor.execute("insert into nc_news(tTitle,tDescription,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?)",titles[x],descr[x],26,1,today,url[x])

cnxn.commit()