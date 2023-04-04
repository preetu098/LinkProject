
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()
 
cursor = cnxn.cursor()
r=requests.get('http://concordtimes.net/news/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("h3", class_= "entry-title posts-list-title"):
    title=x.get_text()
    myurl=x.find('a')['href']
    
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # # # # print("...................................................")

for x in soup.findAll("div",class_="excerpt"):
    
    descr.append(x.get_text().lstrip())
  
for x in soup.find_all('figure',class_="posts-list-thumb"):
    t=x.find('img')['src']
    images.append(t)
    

for x in range(len(images)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],27,1,today,url[x])

cnxn.commit()