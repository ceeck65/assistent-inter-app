
import json


def setDolar(dolar):
	with open('data.json', 'r') as jsonFile:
		data = json.load(jsonFile)
		data["dolar"] = dolar
		jsonFile.seek(0)
	with open('data.json', 'w') as jsonFile:
		json.dump(data, jsonFile)
		jsonFile.truncate()

def getDolar():
	with open('data.json', 'r') as jsonFile:
		data = json.load(jsonFile)
	return data["dolar"]