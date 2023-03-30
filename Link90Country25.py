import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()

cursor = cnxn.cursor()
r=requests.get('https://kbc.co.ke/channel1/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

primary = soup.find("div", class_= "list--widget list--widget-1") 

for x in primary.findAll("div", class_= "post--item post--layout-3"):
    
    title=x.find('h3', class_='h4').get_text()
    myurl=x.find('h3', class_='h4').find('a')['href']
    t = x.find('a', class_='thumb').find('img')['src']
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    descr.append('')
    images.append(t)

for x in range(len(url)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],25,1,today,url[x])

cnxn.commit()