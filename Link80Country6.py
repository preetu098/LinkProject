#https://lanouvelletribune.info/tag/benin/
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()


cursor = cnxn.cursor()
r=requests.get('https://www.burundi-forum.org/')
soup = BeautifulSoup(r.content, "html.parser")

data=soup.select("#main article")

aTag=[x.find("a") for x in data]
ahref=[x['href'] for x in aTag]

iTag=[x.find("img") for x in data]
imgSrc=[x['src'] for x in iTag]

hTag=[x.find("h3").get_text().lstrip() for x in data]


pTag=[x.find("p").get_text().lstrip() for x in data]
print(pTag)



for x in range(len(url)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",hTag[x],pTag[x],imgSrc[x],6,1,today,ahref[x])
cnxn.commit()
