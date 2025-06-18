from main import app
from models.restaurant import Restaurant
from models.pizza import Pizza
from models.restaurant_pizza import RestaurantPizza
from db.database import db

def seed_database():
    with app.app_context():
        # Clear existing data
        db.session.query(RestaurantPizza).delete()
        db.session.query(Pizza).delete()
        db.session.query(Restaurant).delete()
        db.session.commit()

        # Create Restaurants
        restaurants = [
            Restaurant(name="Pizza Palace", address="123 Main St"),
            Restaurant(name="Italian Bistro", address="456 Oak Ave"),
            Restaurant(name="Slice of Heaven", address="789 Pine Rd"),
            Restaurant(name="Mamma Mia Pizzeria", address="101 Pizza St"),
            Restaurant(name="Cheesy Delight", address="202 Mozzarella Blvd")
        ]
        db.session.add_all(restaurants)
        db.session.commit()

        # Create Pizzas
        pizzas = [
            Pizza(name="Margherita", description="Tomato sauce, Mozzarella, Basil"),
            Pizza(name="Pepperoni", description="Tomato sauce, Mozzarella, Pepperoni"),
            Pizza(name="Vegetarian", description="Tomato sauce, Mozzarella, Bell peppers, Mushrooms, Onions"),
            Pizza(name="Hawaiian", description="Tomato sauce, Mozzarella, Ham, Pineapple"),
            Pizza(name="BBQ Chicken", description="BBQ sauce, Mozzarella, Chicken, Red onions"),
            Pizza(name="Four Cheese", description="Tomato sauce, Mozzarella, Parmesan, Gorgonzola, Ricotta"),
            Pizza(name="Meat Lovers", description="Tomato sauce, Mozzarella, Pepperoni, Sausage, Bacon, Ham"),
            Pizza(name="Mushroom Truffle", description="Cream sauce, Mozzarella, Mushrooms, Truffle oil")
        ]
        db.session.add_all(pizzas)
        db.session.commit()

        # Create RestaurantPizza associations
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=15, restaurant_id=2, pizza_id=2),
            RestaurantPizza(price=14, restaurant_id=2, pizza_id=3),
            RestaurantPizza(price=11, restaurant_id=3, pizza_id=1),
            RestaurantPizza(price=13, restaurant_id=3, pizza_id=3),
            RestaurantPizza(price=16, restaurant_id=4, pizza_id=4),
            RestaurantPizza(price=18, restaurant_id=4, pizza_id=5),
            RestaurantPizza(price=12, restaurant_id=5, pizza_id=6),
            RestaurantPizza(price=14, restaurant_id=5, pizza_id=7),
            RestaurantPizza(price=20, restaurant_id=1, pizza_id=8),  # Premium pizza
            RestaurantPizza(price=9, restaurant_id=3, pizza_id=2)    # Discount pepperoni
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()

        print("Database seeded successfully!")
        print(f"Created: {len(restaurants)} restaurants, {len(pizzas)} pizzas, {len(restaurant_pizzas)} restaurant-pizza associations")

if __name__ == '__main__':
    seed_database()