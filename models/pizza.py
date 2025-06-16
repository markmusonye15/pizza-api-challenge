from db.database import db
from dataclasses import dataclass
from typing import Optional

@dataclass
class PizzaType:
    id: Optional[int] 
    name: str 
    description: str 

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    
    # Relationship
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')
    
    def create_pizza(self: PizzaType):
        if not self.name:
            raise ValueError("Pizza name cannot be empty")
            
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        print(f"Pizza {self.name} has been added successfully!")
        return self
    
    def update(self: PizzaType):
        if hasattr(self, 'name') and not self.name:
            raise ValueError("Pizza name cannot be empty")
            
        db.session.commit()
        db.session.refresh(self)
        print(f"Pizza {self.name} has been updated successfully!")
        return self

    def delete(self: PizzaType):
        db.session.delete(self)
        db.session.commit()
        print(f"Pizza {self.name} has been deleted successfully!")
        return self