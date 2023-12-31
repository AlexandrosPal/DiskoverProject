from random import choice, randint
from datetime import datetime as dt
import sys

# Files
sys.path.append("/home/ec2-user/DiskoverProject")
from MongoDB.BuildScript.build_db_script import DiskoverDB


def generate(object):
    # For price
    if object.startswith("D") == True:
        price = DiskoverDB.products.find({"_id": object}, {"_id": 0, "price": 1})
        
        return int(list(price)[0]["price"])

    # For order
    if object == "order":
        db_orders = list(DiskoverDB.sales.find({}, {"_id": 0, "order_id": 1}))
        orders = []
        for order in db_orders:
            orders.append(order["order_id"])

        while True:
            order = f"O{randint(0, 999):03d}"
            if order in orders:
                pass
            else:
                return order

    # For product
    elif object == "product":
        db_products = list(DiskoverDB.products.find({}, {"_id": 1}))
        products = []
        for product in db_products:
            products.append(product["_id"])

        return choice(products)
        
    # For quantity
    elif object == "quantity":
        return randint(1, 10)

def get_records():
    sales = []
    for _ in range(randint(20, 50)):
        sale = {
            "order_id": generate("order"),
            "product_id": generate("product"),
            "quantity": generate("quantity")
        }

        sale["price"] = generate(sale["product_id"])
        sale["revenue"] = sale["quantity"] * sale["price"]
        sale["date"] = dt.now()
        sales.append(sale)

    return sales