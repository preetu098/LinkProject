import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog
today = date.today()

try:
    cursor = cnxn.cursor()
    r=requests.get('https://bushchicken.com/category/news/',headers={'User-Agent': 'newsroom'})
    soup = BeautifulSoup(r.content, "html.parser")
    
    details=soup.select("div.content-inner article")
    aTag=[x.find("a") for x in details]
    aUrl=[x['href'] for x in aTag]
    imgTag=[x.find("img") for x in details]
    imgUrl=[x['src'] for x in imgTag]
    headTag=[x.find("h2").get_text().lstrip() for x in details]
    pTag=[x.find("p").get_text().lstrip() for x in details]

    for x in range(len(aUrl)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",headTag[x],pTag[x],imgUrl[x],27,1,today,aUrl[x])

    cnxn.commit()
    
except Exception as e:
    printErrorLog(__file__.split('\\').pop(), e)