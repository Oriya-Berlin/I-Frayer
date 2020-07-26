import hashlib
from datetime import date
from App.models import Stores, SubStores
import xmltodict


def calculateAge(date_of_birth):
    today = date.today()
    age = today.year - date_of_birth.year - ((date_of_birth.year, today.day) < (date_of_birth.month, date_of_birth.day))
    return age-1


def generateHash(password):
    hashed_pass = hashlib.md5(password.encode()).hexdigest()
    return hashed_pass


def getID(str):
    str = str.split('/')
    id = str[5]
    return id


def getURL(str):
    str = str.split('"')
    return str[1]


def get_sub_stores(store_name):
    store = Stores.objects.get(name=store_name)
    sub_stores = SubStores.objects.filter(chain_id=store.chain_id)

    sub_stores_list = []
    for sub in sub_stores:
        tpl = tuple((sub.city + ' ' + sub.address, sub.city + ' ' + sub.address))
        sub_stores_list.append(tpl)
    return sub_stores_list


def calculate_cart1(url, cart_list):  # rami levi, yohananof
    sum = 0
    with open(url, 'r') as file:
        data = file.read()
        data_dict = xmltodict.parse(data)
        for item in cart_list:  # item need to be an object
            for i in range(0, 10000):
                if item.Item_Code == data_dict['Root']['Items']['Item'][i]['ItemCode']:
                    sum = sum + float(data_dict['Root']['Items']['Item'][i]['ItemPrice'])
                    break

    return sum


def calculate_cart2(url, cart_list):  # victory
    sum = 0
    with open(url, 'r') as file:
        data = file.read()
        data_dict = xmltodict.parse(data)
        for item in cart_list:  # item need to be an object
            for i in range(0, 10000):
                if item.Item_Code == data_dict['Prices']['Products']['Product'][i]['ItemCode']:
                    sum = sum + float(data_dict['Prices']['Products']['Product'][i]['ItemPrice'])
                    break

    return sum