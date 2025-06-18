from flask import Blueprint, jsonify, request
from models.restaurant_pizza import RestaurantPizza
from models.restaurant import Restaurant
from models.pizza import Pizza
from db.database import db
from sqlalchemy.orm import joinedload

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)

# Handle both with and without trailing slash
@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['GET'])
@restaurant_pizza_bp.route('/restaurant_pizzas/', methods=['GET'])
def get_restaurant_pizzas():
    """Get all restaurant-pizza associations"""
    try:
        associations = db.session.query(RestaurantPizza)\
            .options(
                joinedload(RestaurantPizza.pizza),
                joinedload(RestaurantPizza.restaurant)
            )\
            .all()

        return jsonify([{
            'id': rp.id,
            'price': rp.price,
            'pizza': {
                'id': rp.pizza.id,
                'name': rp.pizza.name,
                'ingredients': rp.pizza.description
            },
            'restaurant': {
                'id': rp.restaurant.id,
                'name': rp.restaurant.name,
                'address': rp.restaurant.address
            }
        } for rp in associations])

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Handle both with and without trailing slash
@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
@restaurant_pizza_bp.route('/restaurant_pizzas/', methods=['POST'])
def create_restaurant_pizza():
    """Create a new restaurant-pizza association"""
    data = request.get_json()

    # Validate input
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    required_fields = ['price', 'pizza_id', 'restaurant_id']
    if missing := [f for f in required_fields if f not in data]:
        return jsonify({'error': f'Missing fields: {", ".join(missing)}'}), 400

    try:
        price = int(data['price'])
        if not 1 <= price <= 30:
            return jsonify({'error': 'Price must be between 1 and 30'}), 400
    except ValueError:
        return jsonify({'error': 'Price must be an integer'}), 400

    restaurant = Restaurant.query.get(data['restaurant_id'])
    pizza = Pizza.query.get(data['pizza_id'])

    if not restaurant or not pizza:
        return jsonify({'error': 'Restaurant or Pizza not found'}), 404

    try:
        new_assoc = RestaurantPizza(
            price=price,
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        db.session.add(new_assoc)
        db.session.commit()

        return jsonify({
            'id': new_assoc.id,
            'price': new_assoc.price,
            'pizza': {
                'id': pizza.id,
                'name': pizza.name,
                'ingredients': pizza.description
            },
            'restaurant': {
                'id': restaurant.id,
                'name': restaurant.name,
                'address': restaurant.address
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500