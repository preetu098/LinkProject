



import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()


cursor = cnxn.cursor()
r=requests.get('https://rtnb.bi/fr/index.php/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("h3", class_= "post-grid-content-title"):
    title=x.get_text()
    myurl=x.find('a')['href']
    
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # # # # print("...................................................")

for x in soup.findAll("div",class_="post-grid-content"):
    print(x.find('p').get_text())
    descr.append(x.get_text().lstrip())
  
for x in soup.findAll("article",class_="post-grid element-bottom-20 text-left"):
    t=x.find('img')['src']
    images.append(t)
    
    

for x in range(len(titles)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],24,1,today,url[x])

cnxn.commit()