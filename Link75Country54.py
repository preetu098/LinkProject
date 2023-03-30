import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()



cursor = cnxn.cursor()
r=requests.get('https://www.thezimbabwemail.com/zimbabwe/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("h3", class_= "mh-posts-list-title"):
    title=x.get_text()
    myurl=x.find('a')['href']
    #
    #
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # # # # print("...................................................")

for x in soup.findAll("div",class_="mh-posts-list-excerpt"):
    #print(x.find('p').get_text())
    descr.append(x.get_text().lstrip())
  
for x in soup.findAll("div",class_="mh-posts-list-thumb"):
    t=x.find('img')['src']
    images.append(t)
    #
    
for x in range(len(titles)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],54,1,today,url[x])
cnxn.commit()
print("done")