import pyodbc 
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()

cursor = cnxn.cursor()
# r=requests.get('https://informante.web.na/category/news/')
#r=requests.get('https://informante.web.na')
r=requests.get('http://www.thevillager.com.na/categories/10/Business/')
soup = BeautifulSoup(r.content, "html.parser")



titles=[]
descr=[]
images=[]
url=[]

for x in soup.find("ul", "post-list-small post-list-small--2").find_all('article', 'post-list-small__entry clearfix'):
    title = x.find('h3').get_text().lstrip().rstrip()
    myurl =x.find('h3').find('a')['href']
    desc = x.find('li', 'entry__excerpt').get_text().lstrip().rstrip()
    t = ''
    
    titles.append(title)
    url.append(myurl)
    descr.append(desc)
    images.append(t)

for x in range(len(images)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],36,1,today,url[x])

cnxn.commit()



