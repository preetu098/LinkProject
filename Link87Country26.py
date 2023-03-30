import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()

# cursor = cnxn.cursor()
r=requests.get('https://sundayexpress.co.ls/category/news/')
soup = BeautifulSoup(r.content, "html.parser")

data=soup.select("div.listing article")
datades=soup.select("div.listing article div.post-summary")



aTag=[x.find("a") for x in data]
aRecord=[x['href'] for x in aTag]


aheading=[x.find("h2").get_text() for x in data]


aDesc=[x.get_text() for x in datades]



# for x in range(len(aheading)):
#     cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",aheading[x],aDesc[x],'',26,1,today,aRecord[x])

# cnxn.commit()