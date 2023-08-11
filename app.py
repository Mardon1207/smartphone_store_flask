from flask import Flask, request, jsonify
from db import SmartphoneDB


app = Flask(__name__)
db = SmartphoneDB('db.json')


## view all smartphone
@app.route('/smartphones', methods=['GET'])
def get_all_smartphones():
    """Returns all smartphones in the database"""
    pass


# view all brands
@app.route('/smartphones/brands', methods=['GET'])
def get_all_brands():
    """Returns all brands in the database"""
    html=f"""
    Salom o'zingizga yoqan brendni tanlang!<br>"""
    for i in db.brands():
        html=html+f"""\t<a href"">{i}</a>"""
    return html


# view all smartphones by brand
@app.route('/smartphones/<brand>', methods=['GET'])
def get_smartphone_by_brand(brand):
    """Returns all products by brand"""
    html = """<table border="1px">
    <tr>
        <th>Nomi</th>
        <th>Xotira</th>
        <th>Rangi</th>
        <th>Narxi</th>
    </tr>
    """
    data=db.get_smartphone_by_brand(brand)
    for i in data:
        name = i['name']
        color = i['color']
        price = i['price']
        memory = i['memory']
        ram=i['RAM']

        row = f"""<tr>
                    <td>{name}</td>
                    <td>{ram}/{memory}</td>
                    <td>{color}</td>
                    <td>{price}</td>
                 </tr>"""
        
        html += row
    
    html += "</table>"
    return html


# view smartphone by name
@app.route('/smartphones/name/<brand>/<name>', methods=['GET'])
def get_smartphone_by_name(brand,name):
    """Returns a product by name"""
    html = """<table border="1px">
    <tr>
        <th>Nomi</th>
        <th>Xotira</th>
        <th>Rangi</th>
        <th>Narxi</th>
    </tr>
    """
    data=db.get_smartphone_by_name(brand,name)
    for i in data:
        name = i['name']
        color = i['color']
        price = i['price']
        memory = i['memory']
        ram=i['RAM']

        row = f"""<tr>
                    <td>{name}</td>
                    <td>{ram}/{memory}</td>
                    <td>{color}</td>
                    <td>{price}</td>
                 </tr>"""
        
        html += row
    
    html += "</table>"
    return html


# view smartphone by price
@app.route('/smartphones/price/<brand>/<float:price>', methods=['GET'])
def get_smartphone_by_price(brand,price):
    """Returns a product by price"""
    html = """<table border="1px">
    <tr>
        <th>Nomi</th>
        <th>Xotira</th>
        <th>Rangi</th>
        <th>Narxi</th>
    </tr>
    """
    data=db.get_smartphone_by_price(brand,price)
    for i in data:
        name = i['name']
        color = i['color']
        price = i['price']
        memory = i['memory']
        ram=i['RAM']

        row = f"""<tr>
                    <td>{name}</td>
                    <td>{ram}/{memory}</td>
                    <td>{color}</td>
                    <td>{price}</td>
                 </tr>"""
        
        html += row
    
    html += "</table>"
    return html


# view add smartphone
@app.route('/smartphone/add', methods=['POST'])
def add_smartphone():
    """Adds a product to the database"""
    pass


# view delete smartphone
@app.route('/smartphone/delete/<doc_id>', methods=['DELETE'])
def delete_smartphone(doc_id):
    """Deletes a product from the database"""
    pass


if __name__ == '__main__':
    app.run(debug=True)