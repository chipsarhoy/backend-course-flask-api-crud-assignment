from flask import jsonify, request

from db import product_records


def create_product():
    post_data = request.form if request.form else request.json

    product = {}

    product['product_id'] = int(post_data['product_id'])
    product["name"] = post_data["name"]
    product["description"] = post_data["description"]
    product["price"] = float(post_data["price"])

    product_records.append(product)

    return jsonify({"message": "product created", "result": product}), 201


def read_product_by_id(product_id):
    try:    
        for product in product_records:
            if product['product_id'] == int(product_id):
                return jsonify({"message": "product found",
                                "result": product}), 200
    except:
        return jsonify({"message": "product id is required"}), 400

    return jsonify({"messasge": "product not found"}), 404

def get_all_products():
    return jsonify({"message": "products found", "results": product_records})


def update_product_by_id(product_id):
    post_data = request.form if request.form else request.json

    product = {}

    product["product_id"] = int(product_id)

    if not product["product_id"]:
        return jsonify({"message": "product id is required"}), 400

    for record in product_records:
        if record["product_id"] == product["product_id"]:
            product = record
            product_records.remove(record)

    try:
        product["name"] = post_data.get("name", product["name"])
        product["description"] = post_data.get("description", product["description"])
        product["price"] = post_data.get("price", product["price"])
    except:
        return jsonify({"message": "product not found"}), 404

    product_records.append(product)

    return jsonify({"message": "product updated", "result": product}), 200


def update_active_field(product_id):
    try:
        for record in product_records:
            if record["product_id"] == int(product_id):
                record["active"] = not record["active"]
                return jsonify({"message": "product updated", "result": record}), 200
    except:
        return jsonify({"message": "product id is required"}), 400

    return jsonify({"message": "product not found"}), 404


def delete_product_by_id(product_id):
    try:
        for record in product_records:
            if record["product_id"] == int(product_id):
                product_records.remove(record)
                return jsonify({"message": "product deleted"}), 200
    except:
        return jsonify({"message": "product id is required"}), 400
    
    return jsonify({"message": "product not found"}), 404