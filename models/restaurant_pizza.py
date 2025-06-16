from db.database import db
from dataclasses import dataclass
from typing import Optional

@dataclass
class RestaurantPizzaType:
    id: Optional[int]
    price: int
    pizza_id: int
    restaurant_id: int

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    
    # Relationships
    pizza = db.relationship('Pizza', back_populates='restaurant_pizzas')
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    
    def create_restaurant_pizza(self: RestaurantPizzaType):
        if not 1 <= self.price <= 30:
            raise ValueError("Price must be between 1 and 30")
            
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        print(f"RestaurantPizza (${self.price}) has been added successfully!")
        return self
    
    def update(self: RestaurantPizzaType):
        if hasattr(self, 'price') and not 1 <= self.price <= 30:
            raise ValueError("Price must be between 1 and 30")
            
        db.session.commit()
        db.session.refresh(self)
        print(f"RestaurantPizza (${self.price}) has been updated successfully!")
        return self

    def delete(self: RestaurantPizzaType):
        db.session.delete(self)
        db.session.commit()
        print(f"RestaurantPizza (${self.price}) has been deleted successfully!")
        return self