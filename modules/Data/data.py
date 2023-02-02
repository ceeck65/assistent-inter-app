
import json
from modules.Databases.database import Database


def setDolar(dolar):
	with open('modules/Data/data.json', 'r', encoding = "utf-8") as jsonFile:
		data = json.load(jsonFile)
		data["dolar"] = dolar
		jsonFile.seek(0)
	with open('modules/Data/data.json', 'w', encoding = "utf-8") as jsonFile:
		json.dump(data, jsonFile)
		jsonFile.truncate()

def getDolar():
	with open('modules/Data/data.json', 'r', encoding = "utf-8") as jsonFile:
		data = json.load(jsonFile)
	return data["dolar"]



def setChat(chat):
	with open('modules/Data/data.json', 'r', encoding = "utf-8") as jsonFile:
		data = json.load(jsonFile)
		data["chats"] = chat
		jsonFile.seek(0)
	with open('modules/Data/data.json', 'w', encoding = "utf-8") as jsonFile:
		json.dump(data, jsonFile)
		jsonFile.truncate()       

def getChat():
	with open('modules/Data/data.json', 'r', encoding = "utf-8") as jsonFile:
		data = json.load(jsonFile)
	return data["chats"]

def resetChat():
	with open('modules/Data/data.json', 'r', encoding = "utf-8") as jsonFile:
		data = json.load(jsonFile)
		data["chats"] = 0
		jsonFile.seek(0)
	with open('modules/Data/data.json', 'w', encoding = "utf-8") as jsonFile:
		json.dump(data, jsonFile)
		jsonFile.truncate()


def setChatTransfer(chat):
	with open('modules/Data/data.json', 'r', encoding = "utf-8") as jsonFile:
		data = json.load(jsonFile)
		data["chats_transfers"] = chat
		jsonFile.seek(0)
	with open('modules/Data/data.json', 'w', encoding = "utf-8") as jsonFile:
		json.dump(data, jsonFile)
		jsonFile.truncate()       

def getChatTransfer():
	with open('modules/Data/data.json', 'r', encoding = "utf-8") as jsonFile:
		data = json.load(jsonFile)
	return data["chats_transfers"]

def resetChatTransfer():
	with open('modules/Data/data.json', 'r', encoding = "utf-8") as jsonFile:
		data = json.load(jsonFile)
		data["chats_transfers"] = 0
		jsonFile.seek(0)
	with open('modules/Data/data.json', 'w', encoding = "utf-8") as jsonFile:
		json.dump(data, jsonFile)
		jsonFile.truncate()




# def getPricesByProducts(product):
#      sql = "SELECT plans_packages.name, price, currency FROM products \
#              INNER JOIN plans_packages on plans_packages.product_id = products.id \
#              INNER JOIN prices on prices.plans_id = plans_packages.id \
#              INNER JOIN currencies on prices.currency_id = currencies.id \
#              WHERE products.name = '" + product + "'"
             
#      dicts = {}
#      i=0
#      query = getQuery(sql)
#      while query.next():
         
#          dicts[i] = query.value(0)
         
#      i+1
#      print(dicts)
#      return query
    