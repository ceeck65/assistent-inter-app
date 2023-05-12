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
from modules.Settings.prices_ui import Ui_Dialog
from modules.Databases.modeldb import modelDb
from PyQt5 import QtCore
import string

class Prices(QDialog):
    def __init__(self):
        super(Prices, self).__init__()
        self.db = modelDb()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.onlyDouble = QDoubleValidator()
        self.ui.price_ves.setValidator(self.ui.onlyDouble)
        self.ui.price_usd.setValidator(self.ui.onlyDouble)
        self.ui.price_ves_cable.setValidator(self.ui.onlyDouble)
        self.ui.price_usd_cable.setValidator(self.ui.onlyDouble)
        self.ui.price_ves_dth.setValidator(self.ui.onlyDouble)
        self.ui.price_usd_dth.setValidator(self.ui.onlyDouble)
        self.ui.price_ves_fibrahogar.setValidator(self.ui.onlyDouble)
        self.ui.price_usd_fibrahogar.setValidator(self.ui.onlyDouble)

        self.ui.save.clicked.connect(self.savePriceInternetHfc)
        self.ui.save_prices_cable.clicked.connect(self.savePriceCableHfc)
        self.ui.save_prices_dth.clicked.connect(self.savePriceDth)
        self.ui.save_prices_fibrahogar.clicked.connect(
            self.savePriceFibrahogar)

        self.ui.update.setVisible(False)
        self.ui.update_prices_cable.setVisible(False)
        self.ui.update_prices_dth.setVisible(False)
        self.ui.update_prices_fibrahogar.setVisible(False)

        self.ui.update.clicked.connect(self.updateInternet)
        self.ui.update_prices_cable.clicked.connect(self.updateCable)
        self.ui.update_prices_dth.clicked.connect(self.updateDth)
        self.ui.update_prices_fibrahogar.clicked.connect(self.updateFibrahogar)

        self.ui.clear.clicked.connect(self.clear)
        self.ui.clear_cable.clicked.connect(self.clear)
        self.ui.clear_dth.clicked.connect(self.clear)
        self.ui.clear_fibrahogar.clicked.connect(self.clear)

        self.tablePricesInternetHfc()
        self.tablePricesTvHfc()
        self.tablePricesDth()
        self.tablePricesFibrahogar()
        self.fillTypeProduct()
        self.ui.tblPriceInternetHfc.doubleClicked.connect(self.editInternetHfc)
        self.ui.tblPricesTvHfc.doubleClicked.connect(self.editTvHfc)
        self.ui.tblPricesFibrahogar.doubleClicked.connect(self.editFibrahogar)
        self.ui.tblPricesDth.doubleClicked.connect(self.editDth)
        self.current_id = ""

    def products(self):
        sql = "SELECT id, name FROM products;"
        query = self.db.getData(sql)
        products = []
        for i in range(0, query.rowCount()):
            print(query.record(i).value("name"))
        return query

    def savePriceInternetHfc(self):
        name = self.ui.plan.text()
        price_ves = self.ui.price_ves.text()
        price_usd = self.ui.price_usd.text()
        description = self.ui.plan.text()
        type_product_id = self.ui.type_product.currentIndex()
        product_id = 2
        insert = self.insertPrice(
            name, description, product_id, price_ves, price_usd, type_product_id)
        if insert == True:
            self.ui.plan.clear()
            self.ui.price_usd.clear()
            self.ui.price_ves.clear()
            self.tablePricesInternetHfc()

    def savePriceCableHfc(self):
        name = self.ui.plan_cable.text()
        price_ves = self.ui.price_ves_cable.text()
        price_usd = self.ui.price_usd_cable.text()
        description = self.ui.plan_cable.text()
        type_product_id = self.ui.type_product_cable.currentIndex()
        product_id = 3
        insert = self.insertPrice(
            name, description, product_id, price_ves, price_usd, type_product_id)
        if insert == True:
            self.ui.plan_cable.clear()
            self.ui.price_usd_cable.clear()
            self.ui.price_ves_cable.clear()
            self.tablePricesTvHfc()

    def savePriceDth(self):
        name = self.ui.plan_dth.text()
        price_ves = self.ui.price_ves_dth.text()
        price_usd = self.ui.price_usd_dth.text()
        description = self.ui.plan_dth.text()
        type_product_id = self.ui.type_product_dth.currentIndex()
        product_id = 1
        insert = self.insertPrice(
            name, description, product_id, price_ves, price_usd, type_product_id)
        if insert == True:
            self.ui.plan_dth.clear()
            self.ui.price_usd_dth.clear()
            self.ui.price_ves_dth.clear()
            self.tablePricesDth()

    def savePriceFibrahogar(self):
        name = self.ui.plan_fibrahogar.text()
        price_ves = self.ui.price_ves_fibrahogar.text()
        price_usd = self.ui.price_usd_fibrahogar.text()
        description = self.ui.plan_fibrahogar.text()
        type_product_id = self.ui.type_product_fibrahogar.currentIndex()
        product_id = 5
        insert = self.insertPrice(
            name, description, product_id, price_ves, price_usd, type_product_id)
        if insert == True:
            self.ui.plan_fibrahogar.clear()
            self.ui.price_usd_fibrahogar.clear()
            self.ui.price_ves_fibrahogar.clear()
            self.tablePricesFibrahogar()

    def insertPrice(self, name, description, product_id, price_ves, price_usd, type_product_id):
        temp = name.lower()
        alias = temp.replace("/", "_")
        alias = alias.replace(" ", "_")
        alias = "%s_%s" % (alias, product_id)
        name = string.capwords(name)
        description = string.capwords(description)
        price_ves = 0 if price_ves == "" else float(price_ves)
        price_usd = 0 if price_usd == "" else float(price_usd)
        type_product_id = type_product_id + 1

        sql = "INSERT INTO plans_packages (name, description, product_id, price_ves, price_usd, alias, type_product_id) \
                 VALUES (?, ?, ?, ?, ?, ?, ?);"
        qry = self.db.insert(
            sql, [name, description, product_id, price_ves, price_usd, alias, type_product_id])
        print(name, description, product_id,
              price_ves, price_usd, type_product_id)
        return qry[0]

    def tablePricesInternetHfc(self):
        model = self.getPriceProducts(2)
        table = self.ui.tblPriceInternetHfc
        self.fillTable(table, model)

    def tablePricesTvHfc(self):
        model = self.getPriceProducts(3)
        table = self.ui.tblPricesTvHfc
        self.fillTable(table, model)

    def tablePricesDth(self):
        model = self.getPriceProducts(1)
        table = self.ui.tblPricesDth
        self.fillTable(table, model)

    def tablePricesFibrahogar(self):
        model = self.getPriceProducts(5)
        table = self.ui.tblPricesFibrahogar
        self.fillTable(table, model)

    def fillTable(self, table, model):
        model.setHeaderData(0, QtCore.Qt.Horizontal,
                            QtCore.QObject.tr(model, "ID"))
        model.setHeaderData(1, QtCore.Qt.Horizontal,
                            QtCore.QObject.tr(model, "Planes y Paquetes"))
        model.setHeaderData(2, QtCore.Qt.Horizontal,
                            QtCore.QObject.tr(model, "Tipo de producto"))
        model.setHeaderData(3, QtCore.Qt.Horizontal,
                            QtCore.QObject.tr(model, "Precio Bs."))
        model.setHeaderData(4, QtCore.Qt.Horizontal,
                            QtCore.QObject.tr(model, "Precio Dólar"))
        table.setModel(model)
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)

    def getPriceProducts(self, product):
        sql = "SELECT plans_packages.id as id,  plans_packages.name as name, type_products.name as type_product, price_ves, price_usd FROM products \
                INNER JOIN plans_packages on plans_packages.product_id = products.id \
                INNER JOIN type_products on plans_packages.type_product_id = type_products.id \
                WHERE products.id = %d" % product
        query = self.db.getData(sql)
        return query

    def fillTypeProduct(self):
        sql = "SELECT * FROM type_products"
        combo_hfc = self.ui.type_product
        combo_cable = self.ui.type_product_cable
        combo_dth = self.ui.type_product_dth
        combo_fibrahogar = self.ui.type_product_fibrahogar
        model = self.db.getData(sql)

        combo_hfc.setModel(model)
        combo_hfc.setModelColumn(1)
        combo_cable.setModel(model)
        combo_cable.setModelColumn(1)
        combo_dth.setModel(model)
        combo_dth.setModelColumn(1)
        combo_fibrahogar.setModel(model)
        combo_fibrahogar.setModelColumn(1)

    def editInternetHfc(self):
        self.ui.save.setVisible(False)
        self.ui.update.setVisible(True)
        rows = {index.row() for index in self.ui.tblPriceInternetHfc.selectionModel(
        ).selectedIndexes()}
        data = ""
        for row in rows:
            row_data = []
            for column in range(self.ui.tblPriceInternetHfc.model().columnCount()):
                index = self.ui.tblPriceInternetHfc.model().index(row, column)
                row_data.append(index.data())
            data = row_data

        sql = "SELECT id, name FROM type_products;"
        query = self.db.getData(sql)
        for i in range(0, query.rowCount()):
            if data[2] == query.record(i).value("name"):
                self.ui.type_product.setCurrentIndex(i)
        self.current_id = data[0]
        self.ui.plan.setText(data[1])
        self.ui.price_ves.setText(str(data[3]))
        self.ui.price_usd.setText(str(data[4]))

    def editTvHfc(self):
        self.ui.save_prices_cable.setVisible(False)
        self.ui.update_prices_cable.setVisible(True)
        rows = {index.row()
                for index in self.ui.tblPricesTvHfc.selectionModel().selectedIndexes()}
        data = ""
        for row in rows:
            row_data = []
            for column in range(self.ui.tblPricesTvHfc.model().columnCount()):
                index = self.ui.tblPricesTvHfc.model().index(row, column)
                row_data.append(index.data())
            data = row_data

        sql = "SELECT id, name FROM type_products;"
        query = self.db.getData(sql)
        for i in range(0, query.rowCount()):
            if data[2] == query.record(i).value("name"):
                self.ui.type_product_cable.setCurrentIndex(i)
        self.current_id = data[0]
        self.ui.plan_cable.setText(data[1])
        self.ui.price_ves_cable.setText(str(data[3]))
        self.ui.price_usd_cable.setText(str(data[4]))

    def editDth(self):
        self.ui.save_prices_dth.setVisible(False)
        self.ui.update_prices_dth.setVisible(True)
        rows = {index.row()
                for index in self.ui.tblPricesDth.selectionModel().selectedIndexes()}
        data = ""
        for row in rows:
            row_data = []
            for column in range(self.ui.tblPricesDth.model().columnCount()):
                index = self.ui.tblPricesDth.model().index(row, column)
                row_data.append(index.data())
            data = row_data

        sql = "SELECT id, name FROM type_products;"
        query = self.db.getData(sql)
        for i in range(0, query.rowCount()):
            if data[2] == query.record(i).value("name"):
                self.ui.type_product_dth.setCurrentIndex(i)
        self.current_id = data[0]
        self.ui.plan_dth.setText(data[1])
        self.ui.price_ves_dth.setText(str(data[3]))
        self.ui.price_usd_dth.setText(str(data[4]))

    def editFibrahogar(self):
        self.ui.save_prices_fibrahogar.setVisible(False)
        self.ui.update_prices_fibrahogar.setVisible(True)
        rows = {index.row() for index in self.ui.tblPricesFibrahogar.selectionModel(
        ).selectedIndexes()}
        data = ""
        for row in rows:
            row_data = []
            for column in range(self.ui.tblPricesFibrahogar.model().columnCount()):
                index = self.ui.tblPricesFibrahogar.model().index(row, column)
                row_data.append(index.data())
            data = row_data

        sql = "SELECT id, name FROM type_products;"
        query = self.db.getData(sql)
        for i in range(0, query.rowCount()):
            if data[2] == query.record(i).value("name"):
                self.ui.type_product_fibrahogar.setCurrentIndex(i)
        self.current_id = data[0]
        self.ui.plan_fibrahogar.setText(data[1])
        self.ui.price_ves_fibrahogar.setText(str(data[3]))
        self.ui.price_usd_fibrahogar.setText(str(data[4]))

    def updateInternet(self):
        name = self.ui.plan.text()
        price_ves = self.ui.price_ves.text()
        price_usd = self.ui.price_usd.text()
        type_product_id = self.ui.type_product.currentIndex()
        product_id = 2
        id = self.current_id
        self.update(id, name, product_id, price_ves,
                    price_usd, type_product_id)

    def updateCable(self):
        name = self.ui.plan_cable.text()
        price_ves = self.ui.price_ves_cable.text()
        price_usd = self.ui.price_usd_cable.text()
        type_product_id = self.ui.type_product_cable.currentIndex()
        product_id = 3
        id = self.current_id
        self.update(id, name, product_id, price_ves,
                    price_usd, type_product_id)

    def updateDth(self):
        name = self.ui.plan_dth.text()
        price_ves = self.ui.price_ves_dth.text()
        price_usd = self.ui.price_usd_dth.text()
        type_product_id = self.ui.type_product_dth.currentIndex()
        product_id = 1
        id = self.current_id
        self.update(id, name, product_id, price_ves,
                    price_usd, type_product_id)

    def updateFibrahogar(self):
        name = self.ui.plan_fibrahogar.text()
        price_ves = self.ui.price_ves_fibrahogar.text()
        price_usd = self.ui.price_usd_fibrahogar.text()
        type_product_id = self.ui.type_product_fibrahogar.currentIndex()
        product_id = 5
        id = self.current_id
        self.update(id, name, product_id, price_ves,
                    price_usd, type_product_id)

    def update(self, id, name, product_id, price_ves, price_usd, type_product_id):
        price_ves = 0 if price_ves == "" else float(price_ves)
        price_usd = 0 if price_usd == "" else float(price_usd)
        type_product_id = type_product_id + 1
        sql = "UPDATE plans_packages SET name=?, product_id=?, price_ves=?, price_usd=?, type_product_id=? WHERE id=?"
        qry = self.db.update(
            sql, [name, product_id, price_ves, price_usd, type_product_id, id])
        print(name, product_id, price_ves, price_usd, type_product_id, id, qry)
        if qry == True:
            if product_id == 2:
                self.tablePricesInternetHfc()
            if product_id == 3:
                self.tablePricesTvHfc()
            if product_id == 1:
                self.tablePricesDth()
            if product_id == 5:
                self.tablePricesFibrahogar()
            self.clear()

    def clear(self):
        self.ui.plan.clear()
        self.ui.price_usd.clear()
        self.ui.price_ves.clear()
        self.ui.plan_cable.clear()
        self.ui.price_usd_cable.clear()
        self.ui.price_ves_cable.clear()
        self.ui.plan_dth.clear()
        self.ui.price_usd_dth.clear()
        self.ui.price_ves_dth.clear()
        self.ui.plan_fibrahogar.clear()
        self.ui.price_usd_fibrahogar.clear()
        self.ui.price_ves_fibrahogar.clear()
        self.ui.save.setVisible(True)
        self.ui.update.setVisible(False)
        self.ui.save_prices_cable.setVisible(True)
        self.ui.update_prices_cable.setVisible(False)
        self.ui.save_prices_dth.setVisible(True)
        self.ui.update_prices_dth.setVisible(False)
        self.ui.save_prices_fibrahogar.setVisible(True)
        self.ui.update_prices_fibrahogar.setVisible(False)
