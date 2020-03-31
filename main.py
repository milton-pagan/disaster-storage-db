from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from api.handlers.product_handler import ProductHandler
from api.handlers.customer_handler import CustomerHandler
from api.handlers.user_handler import UserHandler
from api.handlers.request_handler import RequestHandler
from api.handlers.reservation_handler import ReservationHandler
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

@app.route("/disasterStorage/products", methods=["GET", "POST"])
def get_all_products():
    if request.method == "GET":
        if not request.args:
            return ProductHandler().get_all_products()

        else:
            return ProductHandler().search_products(request.args)

    elif request.method == "POST":
        return ProductHandler().insert_product(request.json)


@app.route("/disasterStorage/products/<string:category>")
def get_all_products_by_category(category):
    return ProductHandler().get_all_products_by_category(category)


@app.route(
    "/disasterStorage/products/<int:product_id>", methods=["GET", "PUT", "DELETE"]
)
def get_product_by_id(product_id):
    if request.method == "GET":
        return ProductHandler().get_product_by_id(product_id)

    elif request.method == "PUT":
        return ProductHandler().update_product(product_id, request.json)

    else:
        return ProductHandler().delete_product(product_id)


@app.route("/disasterStorage/products/<int:product_id>/details", methods=["GET", "PUT"])
def get_product_details(product_id):
    if request.method == "GET":
        return ProductHandler().get_detailed_product_by_id(product_id)
    else:
        return ProductHandler().update_product_category_info(product_id, request.json)


@app.route(
    "/disasterStorage/products/<int:product_id>/location", methods=["GET", "PUT"]
)
def get_product_location(product_id):
    if request.method == "GET":
        return ProductHandler().get_product_location(product_id)
    else:
        return ProductHandler().update_product_location(product_id, request.json)


### ORDERS ###

@app.route("/disasterStorage/orders", methods=["GET", "POST"])
def get_all_orders():
    if request.method == "GET":
        return OrderHandler().get_all_orders()
    if request.method == "POST":
        return OrderHandler().insert_order(request.json)

@app.route("/disasterStorage/orders/<int:order_id>", methods=["GET", "PUT", "DELETE"])
def get_order_by_id(order_id):
    if request.method == "GET":
        return OrderHandler().get_order_by_id(order_id)
    if request.method == "PUT":
        return OrderHandler().update_order(order_id, request.json)
    if request.method == "DELETE":
        return OrderHandler().delete_order(order_id)

@app.route("/disasterStorage/orders/products/<int:product_id>")
def get_orders_by_product(product_id):
    if request.method == "GET":
        return OrderHandler().get_orders_by_product_id(product_id)

@app.route("/disasterStorage/orders/customers/<int:customer_id>")
def get_orders_by_customer(customer_id):
    if request.method == "GET":
        return OrderHandler().get_orders_by_customer_id(customer_id)


### RESERVATIONS ###

@app.route("/disasterStorage/reservations", methods=["GET", "POST"])
def get_all_reservations():
    if request.method == "GET":
        return ReservationHandler().get_all_reservations()

    if request.method == "POST":
        return ReservationHandler().insert_reservation(request.json);


@app.route("/disasterStorage/reservations/<int:reservation_id>", methods=["GET", "PUT", "DELETE"])
def get_reservation_by_id(reservation_id):
    if request.method == "GET":
        return ReservationHandler().get_reservation_by_id(reservation_id)

    if request.method == "PUT":
        return ReservationHandler().update_reservation(reservation_id, request.json)

    if request.method == "DELETE":
        return ReservationHandler().delete_reservation(reservation_id)

@app.route("/disasterStorage/reservations/products/<int:product_id>")
def get_reservations_by_product(product_id):
    if request.method == "GET":
        return ReservationHandler().get_reservations_by_product_id(product_id)

@app.route("/disasterStorage/reservations/customers/<int:customer_id>")
def get_reservations_by_customer(customer_id):
    if request.method == "GET":
        return ReservationHandler().get_reservations_by_customer_id(customer_id)


### REQUESTS ###

@app.route("/disasterStorage/requests", methods=["GET", "POST"])
def get_all_requests():
    if request.method == "GET":
        if not request.args:
            return RequestHandler().get_all_requests()

        return RequestHandler().search_requests(request.args)

    if request.method == "POST":
        return RequestHandler().insert_request(request.json);


@app.route("/disasterStorage/requests/<int:request_id>", methods=["GET", "PUT", "DELETE"])
def get_request_by_id(request_id):
    if request.method == "GET":
        return RequestHandler().get_request_by_id(request_id)

    if request.method == "PUT":
        return RequestHandler().update_request(request_id, request.json)

    if request.method == "DELETE":
        return RequestHandler().delete_request(request_id)

@app.route("/disasterStorage/requests/products/<int:product_id>")
def get_requests_by_product_id(product_id):
    if request.method == "GET":
        return RequestHandler().get_requests_by_product_id(product_id)

@app.route("/disasterStorage/requests/customers/<int:customer_id>")
def get_requests_by_customer_id(customer_id):
    if request.method == "GET":
        return RequestHandler().get_requests_by_customer_id(customer_id)


if __name__ == "__main__":
    app.run()
