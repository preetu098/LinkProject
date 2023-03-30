
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()
 
cursor = cnxn.cursor()
r=requests.get('https://moz24h.co.mz/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

for x in soup.findAll("article", "jeg_post jeg_pl_md_3 format-standard"):
    title = x.find('h3').get_text().lstrip().rstrip()
    myurl =x.find('h3').find('a')['href']
    desc = x.find('div', 'jeg_post_excerpt').get_text().lstrip().rstrip()
    t = x.find('div', 'jeg_thumb').find('img')['data-src']
    
    titles.append(title)
    url.append(myurl)
    descr.append(desc)
    images.append(t)
    
for x in soup.findAll("article", "jeg_post jeg_pl_md_1 format-standard"):
    title = x.find('h3').get_text().lstrip().rstrip()
    myurl =x.find('h3').find('a')['href']
    desc = x.find('div', 'jeg_post_excerpt').get_text().lstrip().rstrip()
    t = x.find('div', 'jeg_thumb').find('img')['data-src']
    
    titles.append(title)
    url.append(myurl)
    descr.append(desc)
    images.append(t)

for x in range(len(images)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],35,1,today,url[x])

cnxn.commit()