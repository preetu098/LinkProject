
import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()



cursor = cnxn.cursor()
r=requests.get('http://camerounlink.com/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

primary = soup.findAll("div", id="newsium_single_col_categorised_posts-2") 
for x in primary:
    div= x.findAll("div", class_= "read-single color-pad")
    for w in div:
        divurl = w.find("div", "read-title")
        myurl=divurl.find('a')['href']
        title=divurl.find('a').get_text()
        print("TITLE = " +title)
        print("URL = " +'https://camerounlink.com/' + myurl)
        titles.append(title.lstrip())
        url.append('https://camerounlink.com/' + myurl.lstrip())

# # # # # print("...................................................")

for x in primary:
    div = x.findAll("div",class_="post-description")
    for w in div:
        print(w.get_text())
        descr.append(w.get_text().lstrip())
  
for x in primary:
    div = x.find_all('div',class_="read-img pos-rel col-2 float-l read-bg-img af-sec-list-img")
    for w in div:
        t=w.find('a')
        i='https://www.camerounlink.com/'+t.find('img')['data-src'].replace('./','')
        images.append(i)
        print(i)
for x in range(len(images)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],7,1,today,url[x])
cnxn.commit()
print("done")