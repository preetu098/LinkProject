import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn, printErrorLog, printErrorLog
today = date.today()
try: 
 
    cursor = cnxn.cursor()
    r=requests.get('https://www.guinee360.com/category/news/economie/', headers={'User-Agent': 'newsroom'})
    soup = BeautifulSoup(r.content, "html.parser")

    titles=[]
    descr=[]
    images=[]
    url=[]

    for x in soup.find('div','jeg_posts jeg_block_container').findAll("article"):
        title = x.find('h3','jeg_post_title').get_text().lstrip().rstrip()
        myurl = x.find('h3','jeg_post_title').find('a')['href']
        desc = x.find('div','jeg_post_excerpt').get_text().lstrip().rstrip()
        t = x.find('div', 'jeg_thumb').find('img')['data-src']

        titles.append(title)
        url.append(myurl)
        descr.append(desc)
        images.append(t)

    for x in range(len(titles)):
        cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],1,1,today,url[x])

    cnxn.commit() 
except Exception as e:
    printErrorLog("Link129Country1", e)   