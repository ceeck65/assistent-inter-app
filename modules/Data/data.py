
import json
from modules.Databases.database import Database
from PyQt5.QtWidgets import  QPushButton, QMessageBox

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



def templateUndefined(message):
	msgBox = QMessageBox()
	msgBox.setIcon(QMessageBox.Information)
	msgBox.setText(message)
	msgBox.setWindowTitle("Plantilla No definida")
	QMessageBox.about("Plantilla No definida", message)