import scrapy 
import json


class Task1Spider(scrapy.Spider):
    name="Task1"

    start_urls=['https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1','https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=2']
    
    def parse(self, response):
        req=response.css("div.product-container")
        Data=[]
        for row in req.css("div.product"):
            dic={}
            try:
                dic["name"]=row.css("a.catalog-item-name::text").extract()[0]
                dic["brand"]=row.css("a.catalog-item-brand::text").extract()[0]
                Price=row.css("span.price span::text").extract()
                dic["Price"]=Price[0]
                Stock=None
                try:
                    row.css("span.out-of-stock")
                    Stock=False
                except:
                    Stock=True
                dic["Stock"]=Stock        
                Data.append(dic)
            except:
                continue    
        with open('Result.json','w') as file:
            json.dump(Data,file)