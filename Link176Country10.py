



import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()



cursor = cnxn.cursor()
r=requests.get('https://tchadinfos.com/')
soup = BeautifulSoup(r.content, "html.parser")

data=soup.select("div.et_pb_ajax_pagination_container article")

print(len(data))

# for x in range(len(titles)):
#     cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],'',images[x],10,1,today,url[x])

# cnxn.commit()