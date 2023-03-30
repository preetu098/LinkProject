
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn

today = date.today()


cursor = cnxn.cursor()
# r = requests.get("https://tumfweko.com/category/politics/")  # 404 not found
r = requests.get("https://tumfweko.com/")
soup = BeautifulSoup(r.content, "html.parser")
data=soup.select("#archive-container article")

aTag=[x.find("a") for x in data]
aUrl=[x['href'] for x in aTag]




# imgTag=[x.find("img") for x in data]
# imgUrl=[x['src'] for x in imgTag]
# 

headTag=[x.find('h2').get_text().lstrip() for x in data]



pTag=[x.find('p').get_text().lstrip() for x in data]






for x in range(len(headTag)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",headTag[x],pTag[x],'',53,7,today,aUrl[x])

cnxn.commit()

