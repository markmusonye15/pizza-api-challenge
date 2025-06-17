from flask import Blueprint, jsonify
from models.pizza import Pizza, PizzaType

pizza_bp = Blueprint('pizzas', __name__)

@pizza_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{
        'id': p.id,
        'name': p.name,
        'ingredients': p.description
    } for p in pizzas])