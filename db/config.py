
import os

class Config:
   SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:mypassword123@localhost:5432/pizza_restaurant'
   SQLALCHEMY_TRACK_MODIFICATIONS = False