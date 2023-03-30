#https://abola.pt/




import requests
from datetime import date
from bs4 import BeautifulSoup
# from connection import cnxn
today = date.today()



# cursor = cnxn.cursor()
r=requests.get('https://novojornal.co.ao/')
soup = BeautifulSoup(r.content, "html.parser")
details=soup.select("div.articles-panel article")

images=soup.select("div.articles-panel  article figure")

aTag=[x.find("a") for x in details]
aUrl=[x['href'] for x in aTag]




image=[x.find('img') for x in images]
imgUrl=[x['src'] for x in image]


headTag=[x.get_text().lstrip() for x in details]
print(headTag)



# pTag=[x.find('p').get_text().lstrip() for x in details]
# 





# for x in range(len(aUrl)):
#     cursor.execute("insert into nc_news(tTitle,tDescription,tPhoto,country_Id,category_Id,createdDate,aURL) values(?,?,?,?,?,?,?)",headTag[x],'',imgUrl[x],2,1,today,aUrl[x])

# cnxn.commit()
