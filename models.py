from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base class for all models, Tables will inherit from this
Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    # Define columns for the products table
    id = Column(Integer, primary_key=True)  # Primary key for the product
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False) 


    # sales = relationship("Sale", back_populates="product")


class Sale(Base):
    __tablename__ = 'sales'

   
    id = Column(Integer, primary_key=True)  # Primary key for the sale
    product_id = Column(Integer, ForeignKey('products.id'))  # Foreign key to the products table
    counter_id = Column(Integer, ForeignKey('counters.id'))  # Foreign key to the counters table

    # Define relationships to link sale to product and counter
    product = relationship("Product")  # Each sale is related to one product
    counter = relationship("Counter")  # Each sale is related to one counter



class Counter(Base):
    __tablename__ = 'counters'


    id = Column(Integer, primary_key=True)  # Primary key for the counter
    username = Column(String, unique=True)  # Counter's username (must be unique)

    # Define relationship to link counters to sales
    # sales will be a list of all Sale instances associated with this Counter
    sales = relationship("Sale", back_populates="counter")
