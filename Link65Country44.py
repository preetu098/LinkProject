



import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()



cursor = cnxn.cursor()
r=requests.get('https://wardheernews.com/')
soup = BeautifulSoup(r.content, "html.parser")
data=soup.select("div.media_wrapper_inner div.media")


heading=soup.select("div.media_wrapper_inner div.media div.media_title")

paragraph=soup.select("div.media_wrapper_inner div.media div.media_excerpt")

aTag=[x.find("a") for x in data]
aUrl=[x['href'] for x in aTag]




imgTag=[x.find("img") for x in data]
imgUrl=[x['src'] for x in imgTag]


headTag=[x.get_text().lstrip() for x in heading]



pTag=[x.get_text().lstrip() for x in paragraph]






for x in range(len(headTag)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",headTag[x],pTag[x],imgUrl[x],44,7,today,aUrl[x])

cnxn.commit()