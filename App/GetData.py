#import requests

#import xml.dom.minidom
#from xml.dom import minidom
#import xml.etree.ElementTree as ET

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Final_Project.settings')
django.setup()

import urllib
import gzip
import xmltodict
import urllib.request

from App.models import Item, Stores, SubStores
from App.functions import getID, getURL
from selenium import webdriver

"""
url = 'http://www.matrixcatalog.co.il/CompetitionRegulationsFiles/latest/7290696200003/PriceFull7290696200003-002-202003290309-001.xml.gz'
url2 = 'http://www.matrixcatalog.co.il/CompetitionRegulationsFiles/latest/7290696200003/StoresFull7290696200003-000-202003290558-000.xml.gz'

with urllib.request.urlopen(url) as response:
    with gzip.GzipFile(fileobj=response) as uncompressed:
        data = uncompressed.read()  # a `bytes` object
        data = data.decode()
        response_dict = xmltodict.parse(data)
       
        i = 0
        while response_dict['Prices']['Products']['Product'][i]['ItemCode'] != None:
            print(response_dict['Prices']['Products']['Product'][i]['ItemCode'])
            i += 1
"""




"""
path='https://www.rami-levy.co.il/he/shop/%D7%9C%D7%97%D7%9D_%D7%95%D7%9E%D7%90%D7%A4%D7%99%D7%9D/%D7%9E%D7%90%D7%A4%D7%94_%D7%9E%D7%9C%D7%95%D7%97'

driver = webdriver.Chrome('/home/berlin/Desktop/chromedriver')
driver.get(path)
results = driver.find_elements_by_class_name('product-img')
print(type(results))


for res in results:
    attr = res.get_attribute('style')
    url = getURL(attr)
    id = getID(attr)

    if Item.objects.filter(Item_Code=id).exists():
        item = Item.objects.get(Item_Code=id)
        item.Audience = 'General'
        item.Image = url
        item.Category = 'Salty pastry'
        item.save()
        print(id)
    else:
        print(f"    *{id}*")
"""





url='https://url.retail.publishedprices.co.il/file/d/Stores7290058140886-202004022005.xml'


#  17904 => 17905
with open('/home/berlin/Desktop/rami.xml', 'r') as file:

    data = file.read()
    data_dict = xmltodict.parse(data)
    for i in range(0, 10000):
        print(data_dict['Root']['Items']['Item'][i]['ItemCode'])
        print(data_dict['Root']['Items']['Item'][i]['ItemPrice'])

    """
    for i in range(0, 200):
        chain_id = data_dict['Root']['ChainId']
        sub_chain_id = data_dict['Root']['SubChains']['SubChain']['SubChainId']
        store_id = data_dict['Root']['SubChains']['SubChain']['Stores']['Store'][i]['StoreId']
        print(store_id)
        store_name = data_dict['Root']['SubChains']['SubChain']['Stores']['Store'][i]['StoreName']
        address = data_dict['Root']['SubChains']['SubChain']['Stores']['Store'][i]['Address']
        city = data_dict['Root']['SubChains']['SubChain']['Stores']['Store'][i]['City']

        sub_store = SubStores(chain_id=chain_id,
                    sub_chain_id=sub_chain_id,
                    store_id=store_id,
                    store_name=store_name,
                    address=address,
                    city=city,)
        sub_store.save()
"""


