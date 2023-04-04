import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog
today = date.today()
 
try:
    cursor = cnxn.cursor()
    r=requests.get('https://portalmoznews.com/category/ultima-hora')
    soup = BeautifulSoup(r.content, "html.parser")
    details=soup.select("#content article")

    aTag=[x.find("a") for x in details]
    aUrl=[x['href'] for x in aTag]
    imgUrl=[x.img['data-lazy-src'] for x in details]
    headTag=[x.find("h2").get_text().lstrip() for x in details]
    pTag=[x.get_text().lstrip() for x in details]

    for x in range(len(aUrl)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",headTag[x],pTag[x],imgUrl[x],35,1,today,aUrl[x])

    cnxn.commit()

except Exception as e:
    printErrorLog(__file__.split('\\').pop(), e)