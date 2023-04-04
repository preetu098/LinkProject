import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog

today = date.today()
try: 
    cursor = cnxn.cursor()
    r=requests.get('https://neweralive.na/category/front-page-news', headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.content, "html.parser")

    details=soup.select("section.archive-pro-wrap ul section.new-item")

    aTag=[x.find("a") for x in details]
    aUrl=[x['href'] for x in aTag]
    imgTag=[x.find("img") for x in details]
    imgUrl=[x['src'] for x in imgTag]
    headTag=[x.find("h2").get_text().lstrip() for x in details]
    pTag=[x.get_text().lstrip() for x in details]

    for x in range(len(aUrl)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",headTag[x],pTag[x],imgUrl[x],36,1,today,aUrl[x])

    cnxn.commit()
    
except Exception as e:
    printErrorLog(__file__.split('\\').pop(), e)   