from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from api.handlers.product_handler import ProductHandler
from api.handlers.customer_handler import CustomerHandler
from api.handlers.user_handler import UserHandler
from api.handlers.order_handler import OrderHandler

app = Flask(__name__)
CORS(app)


@app.route("/")
def greet():
    return "Disaster Storage Database"


### USERS ###


@app.route("/disasterStorage/users", methods=["GET"])
def get_all_users():
    if request.method == "GET":
        return UserHandler().get_all_users()
    return


@app.route("/disasterStorage/users/<int:user_id>", methods=["GET", "PUT"])
def get_user_by_id(user_id):
    if request.method == "GET":
        return UserHandler().get_user_by_id(user_id)

    elif request.method == "PUT":
        return

    else:
        return


### CUSTOMERS ###


@app.route("/disasterStorage/users/customers", methods=["GET", "POST"])
def get_all_customers():
    return


@app.route("/disasterStorage/users/<int:customer_id>", methods=["GET", "PUT", "DELETE"])
def get_customer_by_id(customer_id):
    return


### SUPPLIERS ###


@app.route("/disasterStorage/users/suppliers")
def get_all_suppliers():
    return


@app.route("/disasterStorage/users/<int:supplier_id>")
def get_supplier_by_id(supplier_id):
    return


### REQUESTS ###


@app.route("/disasterStorage/requests", methods=["GET", "POST"])
def get_all_requests():
    return


@app.route("/disasterStorage/requests/products")
def get_all_requested_products():
    if not request.args:
        return "Req Prods"

    else:
        return "Keyword search"


### PRODUCTS ###


@app.route("/disasterStorage/products", methods=["GET", "POST"])
def get_all_products():
    if request.method == "GET":
        if not request.args:
            return ProductHandler().get_all_products()
        elif "d" in request.args:
            return ProductHandler().get_all_detailed_products()

    elif request.method == "POST":
        return ProductHandler().insert_product(request.json)


@app.route(
    "/disasterStorage/products/<int:product_id>", methods=["GET", "PUT", "DELETE"]
)
def get_product_by_id(product_id):
    if request.method == "GET":
        if "d" in request.args:
            return ProductHandler().get_detailed_product_by_id(product_id)
        else:
            return ProductHandler().get_product_by_id(product_id)

    elif request.method == "PUT":
        return ProductHandler().update_product(product_id, request.json)

    else:
        return ProductHandler().delete_product(product_id)


@app.route("/disasterStorage/products/available")
def get_available_products():
    if not request.args:
        return ProductHandler().get_available_products()

    else:
        if 'd' in request.args:
            return ProductHandler().get_detailed_available_products()
        else:
            return ProductHandler().search_available_product(request.args)


### ORDERS ###

@app.route("/disasterStorage/orders", methods=["GET", "POST"])
def get_all_orders():
    if request.method == "GET":
        if not request.args:
            return OrderHandler.get_all_orders()
        elif "d" in request.args:
            return OrderHandler.get_all_detailed_orders()

    elif request.method == "POST":
        return OrderHandler.insert_order(request.json);


@app.route("/disasterStorage/orders/<int:order_id>", methods=["GET", "PUT", "DELETE"])
def get_order_by_id(order_id):
    if request.method == "GET":
        if "d" in request.args:
            return OrderHandler().get_detailed_order_by_id(order_id)
        else:
            return OrderHandler().get_order_by_id(order_id)

    elif request.method == "PUT":
        return OrderHandler().update_order(order_id, request.json)

    else:
        return OrderHandler().delete_order(order_id)


if __name__ == "__main__":
    app.run()
