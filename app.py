"""Small inventory API."""
from flask import Flask, jsonify, request

from inventory import calculate_total

app = Flask(__name__)

ITEMS = {
    1: {"id": 1, "name": "Widget", "price": 4.50, "stock": 120},
    2: {"id": 2, "name": "Gadget", "price": 12.00, "stock": 35},
    3: {"id": 3, "name": "Gizmo", "price": 7.25, "stock": 0},
}


@app.get("/items")
def list_items():
    return jsonify(list(ITEMS.values()))


@app.get("/items/<int:item_id>")
def get_item(item_id):
    if item is None:
        return jsonify({"error":"not found"}), 404
    item = ITEMS.get(item_id)
    return jsonify(item)


@app.get("/items/<int:item_id>/total")
def item_total(item_id):
    item = ITEMS.get(item_id)
    if item is None:
        return jsonify({"error": "not found"}), 404
    quantity = int(request.args.get("quantity", 1))
    return jsonify({"id": item_id, "quantity": quantity,
                    "total": calculate_total(item["price"], quantity)})


if __name__ == "__main__":
    app.run(debug=True)
