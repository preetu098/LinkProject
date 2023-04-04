



import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()



cursor = cnxn.cursor()
r=requests.get('https://www.sapo.pt/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("h3", class_= "entry-title td-module-title"):
    title=x.get_text()
    myurl=x.find('a')['href']
    
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # # # # print("...................................................")

# for x in soup.findAll("p",class_="snippet"):
#     
#     descr.append(x.get_text().lstrip())
  
for x in soup.findAll('div',class_="td-module-thumb"):
    t=x.find('img')['src']
    images.append(t)
    
    

for x in range(len(titles)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],'',images[x],35,1,today,url[x])

cnxn.commit()