from flask import Blueprint

import controllers

products = Blueprint("products", __name__)


@products.route("/product", methods=["POST"])
def create_product():
    return controllers.create_product()

@products.route("/product/<product_id>", methods=["GET"])
def read_product_by_id(product_id):
    return controllers.read_product_by_id(product_id)

@products.route("/products", methods=["GET"])
def get_all_products():
    return controllers.get_all_products()

@products.route("/product/<product_id>", methods=['PUT'])
def update_product_by_id(product_id):
    return controllers.update_product_by_id(product_id)

@products.route("/product/active/<product_id>", methods=["PATCH"])
def update_active_field(product_id):
    return controllers.update_active_field(product_id)

@products.route("/product/delete/<product_id>", methods=["DELETE"])
def delete_product_by_id(product_id):
    return controllers.delete_product_by_id(product_id)