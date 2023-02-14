# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 04:15:14 2023

@author: alesp
"""

import json


        
        
def getTemplate(template):
    with open('modules/Data/templates.json', 'r', encoding = "utf-8") as jsonFile:
        data = json.load(jsonFile)
    return data[template]


def getLabel(template):
    with open('modules/Data/text.json', 'r', encoding = "utf-8") as jsonFile:
        data = json.load(jsonFile)
    return data[template]