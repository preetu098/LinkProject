import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()


cursor = cnxn.cursor()
r=requests.get('https://www.liberianobserver.com/business')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
# primary =  

for x in soup.findAll("div", class_= "views-row listing--articles__item col-md-4"):
    title=x.find("h3", class_= "article--teaser__title").get_text()
    myurl=x.find("article", class_= "article--teaser").find('a')['href']
    titles.append(title.lstrip())
    url.append('https://www.liberianobserver.com/'+myurl.lstrip())
# # # # # print("...................................................")

for x in soup.findAll("div",class_="views-row listing--articles__item col-md-4"):
    descr.append('')

for x in soup.findAll("div", class_= "views-row listing--articles__item col-md-4"):
    t=x.find("article", class_= "article--teaser").find('div', 'img-container').find('img')
    images.append('https://www.liberianobserver.com'+t['src'])
for x in range(len(images)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],27,1,today,url[x])
cnxn.commit()