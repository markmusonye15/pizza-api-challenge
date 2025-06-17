from flask import Flask, jsonify
from flask_migrate import Migrate
from db.database import db
from db.config import Config

# Initialize Flask application
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS

# Initialize extensions
db.init_app(app)
migrate = Migrate(app, db)

# Import models (needed for migrations)
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza

# Import controllers
from controllers.restaurant_controller import restaurant_bp
from controllers.pizza_controller import pizza_bp
from controllers.restaurant_pizza_controller import restaurant_pizza_bp

# Register blueprints
app.register_blueprint(restaurant_bp)
app.register_blueprint(pizza_bp)
app.register_blueprint(restaurant_pizza_bp)

@app.route('/')
def welcome():
    """Root endpoint that welcomes users to the API"""
    return jsonify({
        "message": "Welcome to Pizza Restaurant API",
        "endpoints": {
            "restaurants": {
                "GET /restaurants": "List all restaurants",
                "GET /restaurants/<id>": "Get restaurant details",
                "DELETE /restaurants/<id>": "Delete a restaurant"
            },
            "pizzas": {
                "GET /pizzas": "List all pizzas"
            },
            "restaurant_pizzas": {
                "POST /restaurant_pizzas": "Create a new restaurant-pizza association"
            }
        }
    })

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "database": "connected" if db.session.bind else "disconnected"
    })

if __name__ == '__main__':
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
    app.run(debug=True)