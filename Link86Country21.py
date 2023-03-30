import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()

cursor = cnxn.cursor()
r=requests.get('https://citinewsroom.com/news/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("div", class_= "row vc_row wpb_row vc_row-fluid"):
    if(x.find('article', class_='format-standard') is not None):
        if(x.find('article', class_='format-standard').find('h3', class_='jeg_post_title') is None):
            title=x.find('article', class_='format-standard').find('h2', class_='jeg_post_title').get_text()
        else:
            title=x.find('article', class_='format-standard').find('h3', class_='jeg_post_title').get_text()

        myurl=x.find('article', class_='format-standard').find('div', 'jeg_thumb').find('a')['href']

        if(x.find('article', class_='format-standard').find('div', 'jeg_thumb').find('div', class_='lazyloaded') is None):
            t = x.find('article', class_='format-standard').find('div', 'jeg_thumb').find('div', class_='thumbnail-container').find('img')['src']
        else:
            t = x.find('article', class_='format-standard').find('div', 'jeg_thumb').find('div', class_='lazyloaded')['data-src']

        titles.append(title.lstrip())
        url.append(myurl.lstrip())
        descr.append('')
        images.append(t)

for x in range(len(titles)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],'',images[x],21,1,today,url[x])

cnxn.commit()