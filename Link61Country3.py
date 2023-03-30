#https://lanouvelletribune.info/tag/benin/




import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()



cursor = cnxn.cursor()
r=requests.get('https://www.weekendpost.co.bw/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("h3", class_= "jeg_post_title"):
    title=x.get_text()
    myurl=x.find('a')['href']
    
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # print("...................................................")

for x in soup.findAll("div",class_="jeg_post_excerpt"):
    
    descr.append(x.get_text().lstrip())
    

for x in soup.findAll('div',class_="thumbnail-container"):
    t=x.find('img')['src']
    images.append(t)
    

for x in range(len(url)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],3,1,today,url[x])

cnxn.commit()