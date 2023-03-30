import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()

cursor = cnxn.cursor()
r=requests.get('https://www.investiraucameroun.com/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]
primary = soup.find("div", id="sppb-addon-1569506476871") 
for x in primary.findAll("div", class_="aidanews2_k2_positions"):
    title=x.find('div', class_='aidanews2_k2_topR').find('p', 'aidanews2_k2_title').get_text()
    myurl=x.find('div', class_='aidanews2_k2_topR').find('p', 'aidanews2_k2_title').find('a')['href']
    titles.append(title.lstrip())
    url.append('https://www.investiraucameroun.com'+myurl.lstrip())


# # # # # print("...................................................")

for x in primary.findAll("div",id="sppb-addon-1569506476871"):
    print(x.find('div', class_='aidanews2_k2_topR').find('span', 'aidanews2_k2_text').get_text())
    descr.append(x.get_text().lstrip())
  
for x in soup.findAll('div',id="sppb-addon-1569506476871"):
    t=x.find('div', class_='aidanews2_k2_top').find('a', class_='aidanews2_k2_img1').find('img')['src']
    images.append(t)
print(len(t))
for x in range(len(descr)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],images[x],7,1,today,url[x])

cnxn.commit()