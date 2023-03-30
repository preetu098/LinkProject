# h tag not found & formate not spacify



import requests
from datetime import date
from bs4 import BeautifulSoup
# from connection import cnxn
today = date.today()


# cursor = cnxn.cursor()
r=requests.get('https://www.pulse.com.gh/')
soup = BeautifulSoup(r.content, "html.parser")

data=soup.select("local/lazyLoad.run")

aTag=[x.find("a") for x in data]
ahref=[x['href'] for x in aTag]
print(aTag)

iTag=[x.find("img") for x in data]
imgSrc=[x['src'] for x in iTag]
print(imgSrc)

# hTag=[x.find("h3").get_text().lstrip() for x in data]
# print(hTag)


# pTag=[x.find("p").get_text().lstrip() for x in data]
# print(pTag)



# for x in range(len(url)):
#     cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",hTag[x],pTag[x],imgSrc[x],6,1,today,ahref[x])
# cnxn.commit()
