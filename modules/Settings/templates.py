# -*- coding: utf-8 -*-
"""
Created on Sat Jan 28 19:07:57 2023

@author: alesp
"""

from PyQt5.QtWidgets import (
    QDialog,
    QHeaderView
)
from PyQt5.QtGui import QDoubleValidator
from modules.Settings.templates_ui import Ui_Dialog
from modules.Databases.modeldb import modelDb
from PyQt5 import QtCore
import string


class Templates(QDialog):
    def __init__(self):
        super(Templates, self).__init__()
        self.db = modelDb()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.fillCombo()
        self.ui.save_template.clicked.connect(self.saveTemplate)
        self.ui.cancel_template.clicked.connect(self.clearTemplates)
        self.ui.products.currentTextChanged.connect(self.changedProduct)
        self.setComboPlans(1)
        self.tableTemplates(1)


    def fillCombo(self):
        combo_products = self.ui.products
        combo_type_template = self.ui.type_template
        model_productos = self.getProducts()
        model_type = self.getTypeTemplate()

        combo_products.setModel(model_productos)
        combo_products.setModelColumn(1)
        combo_type_template.setModel(model_type)
        combo_type_template.setModelColumn(1)

    def fillComboPackages(self, model):
        combo_plans_packages = self.ui.plans_package
        combo_plans_packages.setModel(model)
        combo_plans_packages.setModelColumn(1)
    
    def saveTemplate(self):
        try:
            template_name = self.ui.template_name.text()
            plans_package_name = self.ui.plans_package.currentText()
            plans_package_id =  self.getPlanIdByName(plans_package_name)
            type_template_id = self.ui.type_template.currentIndex() + 1
            template = self.ui.template_txt.toPlainText()
            sql_product = "SELECT * FROM plans_packages where id= %d" % plans_package_id
            product = self.db.getData(sql_product)
            alias = product.record(0).value("alias")
            product_id = product.record(0).value("product_id")
            if alias == None:
                alias = template_name
                temp = template_name.lower()
                alias =  temp.replace("/", "_")
                alias =  alias.replace(" ", "_")
            sql = "INSERT INTO templates (name, template, type_template_id, alias) VALUES (?, ?, ?, ?);"
            qry = self.db.insert(sql, [template_name, template, type_template_id, alias])
            if qry[0] == True:
                last_id = self.db.getData("select max(id) from templates;")
                template_id =  last_id.record(0).value(0)
                
                print(qry, template_id)
                sql_ = "INSERT INTO template_has_plans_package (alias, template_id, plans_package_id) VALUES (?, ?, ?);"
                qry = self.db.insert(sql_, [alias, template_id, plans_package_id])
            self.tableTemplates(product_id)
            self.clearTemplates()
        except Exception as e:
            print(e)

    def clearTemplates(self):
        self.ui.template_name.clear()
        self.ui.template_txt.clear()

    def getPlansPackages(self):
        sql= "SELECT id, name FROM plans_packages;"
        query = self.db.getData(sql)
        return query 

    def getTypeTemplate(self):
        sql= "SELECT id, name FROM type_templates;"
        query = self.db.getData(sql)
        return query 

    def getPlanIdByName(self, name):
        sql = "SELECT id from plans_packages where name LIKE '%s'" % name
        print(name, sql)
        query = self.db.getSingleData(sql)
        id = query.record(0).value("id")
        return id
    
    def tableTemplates(self, product_id):
        sql = "SELECT templates.name as name, template, type_templates.name as type_template, templates.alias as alias FROM templates INNER JOIN template_has_plans_package on templates.id = template_has_plans_package.template_id  INNER JOIN plans_packages on template_has_plans_package.plans_package_id = plans_packages.id  INNER JOIN type_templates on templates.type_template_id = type_templates.id WHERE plans_packages.product_id = %d" % product_id 
        query = self.db.getData(sql)
        table = self.ui.tbl_templates
        self.fillTable(table, query) 

    def fillTable(self, table, model):
        model.setHeaderData(0, QtCore.Qt.Horizontal, QtCore.QObject.tr(model, "Name"))
        model.setHeaderData(1, QtCore.Qt.Horizontal, QtCore.QObject.tr(model, "Plantilla"))
        model.setHeaderData(2, QtCore.Qt.Horizontal, QtCore.QObject.tr(model, "Tipo de plantilla"))
        model.setHeaderData(3, QtCore.Qt.Horizontal, QtCore.QObject.tr(model, "Alias"))
        table.setModel(model)
        header = table.horizontalHeader()      
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        
    def getProducts(self):
        sql= "SELECT id, despcription FROM products;"
        query = self.db.getData(sql)
        return query    
    
    def setComboPlans(self, product_id):
        sql= "SELECT id, name FROM plans_packages where product_id = %d;" % product_id
        query = self.db.getData(sql)
        self.fillComboPackages(query)
    
    def changedProduct(self, value):
        sql_produts = "SELECT * FROM products where despcription = '%s';" % value
        qry_products = self.db.getSingleData(sql_produts)
        product_id = qry_products.record(0).value("id")
        print(product_id)
        self.setComboPlans(product_id)
        self.tableTemplates(product_id)
        
        
        
        
        
        