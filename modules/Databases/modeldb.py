


from modules.Databases.database import Database
from modules.Data.data import getDolar


class modelDb():
    def __init__(self):
        super(modelDb, self).__init__()
        self.db = Database()
        self.dolar = getDolar()

    def getData(self, sql):
        qry = self.db.getQuery(sql)
        return qry

    def getSingleData(self, sql):
        qry = self.db.getSingleQuery(sql)
        return qry

    def insert(self, sql, args):
        qry = self.db.createQuery(sql, args)
        return qry

    def getPricePlansPackage(self, alias):
        sql = "SELECT price_ves, price_usd FROM plans_packages WHERE alias = '%s'" % alias
        response = self.getPrices(sql)
        return response

    def getPricePlansPackageByName(self, name):
        sql = "SELECT price_ves, price_usd FROM plans_packages WHERE name LIKE '%s'" % name
        response = self.getPrices(sql)
        return response

    def getPrices(self, sql):
        model = self.getSingleData(sql)
        price_ves_ = model.record(0).value("price_ves")
        price_usd_ = model.record(0).value("price_usd")
        price_ves_ = str(price_ves_)
        price_usd_ = str(price_usd_)
        price_ves = float(price_ves_.replace(',', ''))
        price_usd = float(price_usd_.replace(',', ''))
        response = {"price_ves": price_ves, "price_usd": price_usd}
        return response

    def getPriceUSD(self, price_ves, price_usd):
        if price_usd == 0 or price_usd == 0.0:
            total_usd = (float(price_ves) / self.dolar)
        else: 
            total_usd = float(price_usd)
        return total_usd

    def getPriceVES(self, price_ves, price_usd):
        if price_ves == 0 or price_ves == 0.0:
            if price_usd == 0 or price_usd == 0.0:
                total_ves = 0
            else:
                total_ves = (float(price_usd) * self.dolar)
        else: 
            total_ves = float(price_ves)
        return total_ves
    
    def getProductsByIdAndTypeProduct(self, product_id, type_product):
        sql = "SELECT * FROM plans_packages where product_id ='%d' and type_product_id ='%d';" % (product_id, type_product)
        query = self.getData(sql)
        return query