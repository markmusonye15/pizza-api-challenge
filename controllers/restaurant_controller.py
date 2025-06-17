from flask import Blueprint, jsonify, request
from models.restaurant import Restaurant, RestaurantType
from models.restaurant_pizza import RestaurantPizza
from db.database import db

restaurant_bp = Blueprint('restaurants', __name__)

@restaurant_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{
        'id': r.id,
        'name': r.name,
        'address': r.address
    } for r in restaurants])

@restaurant_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    pizzas = [{
        'id': rp.pizza.id,
        'name': rp.pizza.name,
        'ingredients': rp.pizza.description,
        'price': rp.price
    } for rp in restaurant.restaurant_pizzas]
    
    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': pizzas
    })

@restaurant_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    
    try:
        # Cascading delete will handle RestaurantPizzas automatically
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500