import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()

 
cursor = cnxn.cursor()
r=requests.get('https://dailynewsegypt.com/')
soup = BeautifulSoup(r.content, "html.parser")
print(r)
titles=[]
descr=[]
images=[]
url=[]
for x in soup.findAll("h3", class_= "elementor-post__title"):
    title=x.get_text()
    myurl=x.find('a')['href']
    print(title)
    print(myurl)
    titles.append(title.lstrip())
    url.append(myurl.lstrip())

# # # # # print("...................................................")

for x in soup.findAll("div",class_="elementor-post__excerpt"):
    print(x.find("p").get_text())
    descr.append(x.get_text().lstrip())
  
for x in soup.findAll('div',class_="elementor-post__thumbnail"):
    t=x.find('img')['src']
    images.append(t)
    

for x in range(len(descr)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],15,1,today,url[x])

cnxn.commit()