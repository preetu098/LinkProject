import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn
today = date.today()
 
cursor = cnxn.cursor()
r=requests.get('https://www.standardmedia.co.ke/')
soup = BeautifulSoup(r.content, "html.parser")

titles=[]
descr=[]
images=[]
url=[]

primary = soup.select_one(".second :first-child")

for x in primary.findAll('div', class_='col-12'):
    title = x.find('div', class_='sub-title mt-2').get_text().replace('\n\n', '')
    myurl = x.find('div', class_='sub-title mt-2').find('a')['href']
    t = x.find('div', class_='mt-3').find('img', class_='style-image-two mb-3 w-100')['src']
    
    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    descr.append('')
    images.append(t)
 
for x in range(len(descr)):
    cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",titles[x],descr[x],'',25,1,today,'')

cnxn.commit()