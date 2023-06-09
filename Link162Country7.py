#https://www.mmegi.bw/




import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()


cursor = cnxn.cursor()
r=requests.get('http://www.camerounlink.com/actu/Cameroun-Toute-L-actualite-nationale/grpe-1/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("h2", class_= "article-title"):
    title=x.get_text()
    myurl=x.find('a')['href']
    
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # # print("...................................................")

for x in soup.findAll("p",class_="article-body"):
    
    descr.append(x.get_text().lstrip())
    

for x in soup.findAll('div',class_="layout-ratio"):
    t=x.find('img')['src']
    images.append(t)
    

for x in range(len(descr)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],7,1,today,url[x])

cnxn.commit()