from tinydb import TinyDB, Query


class SmartphoneDB:
    def __init__(self, db_path):
        self.db = TinyDB(db_path, indent=4)
        self.query = Query()
    
    def brands(self):
        """Returns all brands in the database"""
        return self.db.tables()
    
    def get_smartphone_by_brand(self, brand):
        """Returns all products by brand"""
        return self.db.table(brand).all()
    
    def get_smartphone_by_name(self, brand,name):
        """Returns a product by name"""
        return self.db.table(brand).search(Query().name==name)

    def get_smartphone_by_price(self,brand, price):
        """Returns a product by price"""
        return self.db.table(brand).search(Query().price==price)
    
    def add_smartphone(self, smartphone, brand):
        """Adds a product to the database"""
        self.db.table(brand).insert(smartphone)
    
    def delete_smartphone(self, doc_id:int, brand):
        """Deletes a product from the database"""
        print(brand)
        self.db.table(brand).remove(doc_ids=[doc_id])
    
