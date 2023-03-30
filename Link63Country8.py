# http://yaoundeinfo.com/



import requests
from datetime import date
from bs4 import BeautifulSoup
from connection import cnxn

today = date.today()


cursor = cnxn.cursor()
headers = {"User-Agent": "newsroom"}

r = requests.get("https://asemana.publ.cv/", headers=headers)

soup = BeautifulSoup(r.content, "html.parser")

titles = []
descr = []
images = []
url = []
posts_column = soup.find("div", {"id": "actualite"})

import pdb

aLaUne = soup.find("div", {"id": "aLaUne"})

try:
    image = aLaUne.find("img", {"class": "bordureImgAlaUne"})["src"]
    content = aLaUne.find("h2")
    summary = aLaUne.find("h4")
    title = content.get_text()
    myurl = content.a["href"]
    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    images.append(image)
    descr.append(summary.get_text())
except:
    print("error")


actualite = soup.find("div", {"id": "actualite"})


for x in actualite.find_all("div"):
    image = x.find("img")["src"]
    content = x.find("h3")
    summary = x.find("p")
    title = content.get_text()
    myurl = content.a["href"]
    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    images.append(image)
    descr.append(summary.get_text())


for x in soup.findAll("div", {"class": "articleRecente"}):
    content = x.find("dt", {"class": "rubriqueArticlesRecentes"})
    summary = x.find("dd", {"class": "texteArticlesRecentes"})
    title = content.get_text()
    myurl = content.a["href"]
    titles.append(title.lstrip())
    url.append(myurl.lstrip())
    images.append("")
    descr.append(summary.get_text())

print(len(titles), len(descr), len(url), len(images))

for x in range(len(descr)):
    cursor.execute(
        "insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",
        titles[x],
        descr[x],
        images[x],
        8,
        1,
        today,
        url[x],
    )

cnxn.commit()
