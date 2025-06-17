from db.database import db
from dataclasses import dataclass
from typing import Optional

@dataclass
class RestaurantType:
    id: Optional[int]
    name: str
    address: str

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(200), nullable=False)
    
    # Relationship with cascade delete
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', 
                                      cascade='all, delete-orphan')
    
    def create_restaurant(self: RestaurantType):
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        print(f"Restaurant {self.name} has been added successfully!")
        return self
    
    def update(self: RestaurantType):
        db.session.commit()
        db.session.refresh(self)
        print(f"Restaurant {self.name} has been updated successfully!")
        return self

    def delete(self: RestaurantType):
        db.session.delete(self)
        db.session.commit()
        print(f"Restaurant {self.name} has been deleted successfully!")
        return self