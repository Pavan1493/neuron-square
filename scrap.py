from attr import attrs
import requests
from bs4 import BeautifulSoup
import json

url='https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage='

Data=[]
for i in range(1,3):
    res=requests.get(url+str(i))
    soup=BeautifulSoup(res.content,'html5lib')
    All_Items=soup.find('div',attrs={'class':'product-container'})
    for row in All_Items.find_all('div'):
        dic={}
        try:
            dic['Name']=row.find('a',attrs={'class':'catalog-item-name'}).text 
            dic['Brand_Name']=row.find('a',attrs={'class':'catalog-item-brand'}).text 
            dic['Price']=row.find('span',attrs={'class':'price'}).text
            Stock=None
            try:
                row.find('span',attrs={'class':'out-of-stock'})
                Stock=False
            except:
                Stock=True
            dic['Stock']=Stock        
            Data.append(dic)
        except:
            print('Missing elements')
with open('Scrap_items.json','w') as file:
    json.dump(Data,file)