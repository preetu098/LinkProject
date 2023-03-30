#https://lanouvelletribune.info/tag/benin/
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()


cursor = cnxn.cursor()
# r=requests.get('http://fasozine.com/') Not Working 
#r=requests.get('https://www.sidwaya.info/') Dont Have Access
r=requests.get('https://www.burkinademain.com/')

soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
main = soup.find("div", id="tdi_50")
for x in main.findAll("div", class_= "td-block-span4"):
    title=x.find('h3', class_='entry-title td-module-title').get_text()
    myurl=x.find('h3', class_='entry-title td-module-title').find('a')['href']
    print('TITLE = '+ title)
    print('URL = '+myurl)
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # print("...................................................")

for x in main.findAll("div",class_="td-excerpt"):
    descr.append(x.get_text().lstrip())
    print('DESCRIPTION = '+x.get_text())

for x in main.findAll("img",class_="entry-thumb"):
    t=x['src']
    images.append(t)
    print('IMAGE = '+t)
"""
for x in range(len(url)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],5,1,today,url[x])
"""
print("done")
cnxn.commit()