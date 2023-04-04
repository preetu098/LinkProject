
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()


cursor = cnxn.cursor()
r=requests.get('http://eldjazairmag.com/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("h2", class_= "entry__title--bg"):
    title=x.get_text()
    myurl=x.find('a')['href']
    
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# print("...................................................")

for x in soup.findAll("p",class_="small-content"):
    
    descr.append(x.get_text().lstrip())
    

# for x in soup.findAll('div',class_="entry__img-holder post-list__img-holder card__img-holder"):
#     t=x.find('img')['src']
#     images.append(t)
#     

for x in range(len(titles)):
    cursor.execute("insert into nc_news(tTitle,tDescription,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?)",titles[x],descr[x],1,1,today,url[x])

cnxn.commit()