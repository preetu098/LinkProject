#https://lanouvelletribune.info/tag/benin/
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog

today = date.today()

try:
    cursor = cnxn.cursor()
    r=requests.get('https://lanouvelletribune.info/tag/benin/', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")

    record=soup.select("div.jeg_block_container article")
    aTag=[x.find("a") for x in record]
    aUrl=[x['href'] for x in aTag]
    headTag=[x.find("h3").get_text().lstrip() for x in record]
    imgTag=[x.find("img") for x in record]
    imgUrl=[x['src'] for x in imgTag]
    pTag=[x.find("p").get_text().lstrip() for x in record]

    for x in range(len(aUrl)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",headTag[x],pTag[x],imgUrl[x],3,1,today,aUrl[x])

    cnxn.commit()

except Exception as e:
    printErrorLog(__file__.split('\\').pop(), e)   