from sqlalchemy.exc import IntegrityError
from database import Session
from models import Product, Sale, Counter

ADMIN_PASSWORD = "admin123"

VALID_COUNTERS = ("counter1", "counter2")


# Product Management Functions

def add_product(name, price, password):
    if password != ADMIN_PASSWORD:
        return "Incorrect admin password."

    session = Session()
    new_product = Product(name=name, price=price)  #create a new Product object
    session.add(new_product)
    try:
        session.commit()  #commit changes to the database
        return f"Product {name} added."
    except IntegrityError: #I will consider removing this error checker
        session.rollback()  # Rollback changes if there's an error
        return "the product may already exist."
    finally:
        session.close()


def delete_product(product_id, password):
    if password != ADMIN_PASSWORD:
        return "Incorrect password."

    session = Session()  # Start database session
    try:
        # Find the product by its ID
        product = session.query(Product).filter_by(id=product_id).first()
        if product:  # If product is found
            session.delete(product)  # Delete the product from the session
            session.commit()  # Commit changes to the database
            return f"Product ID {product_id} deleted."
        else:
            return "Product not found."
    finally:
        session.close()  # Ensure the session is always closed

# Function to view all products
def view_products():
    session = Session()  # Start database session
    try:
        products = session.query(Product).all()  # Query all products
        if not products:  # If no products found
            return "No products found."
        # Return a list of products with formatted details
        return [f"ID: {product.id}, Name: {product.name}, Price: {product.price}" for product in products]
    finally:
        session.close()  # Ensure the session is always closed


# Sale Management Functions


# Function to add a sale, requires a valid counter username
def add_sale(product_id, username):
    if username not in VALID_COUNTERS:  # Check if the counter username is valid
        return "Invalid counter username."

    session = Session()  # Start database session
    try:
        sale = Sale(product_id=product_id)  # Create a new Sale object

        # Check if the counter exists in the database
        counter = session.query(Counter).filter_by(username=username).first()
        if not counter:  # If counter doesn't exist, create a new one
            counter = Counter(username=username)
            session.add(counter)  # Add new counter to session

        sale.counter = counter  # Assign the counter to the sale
        session.add(sale)  # Add the sale to the session

        session.commit()  # Commit changes to the database
        return f"Sale for product ID {product_id} added by {username}."  # Return success message
    except IntegrityError:
        session.rollback()
        return "Error adding sale."
    finally:
        session.close()

# Function to view all sales
def view_sales():
    session = Session()  # Start database session
    try:
        sales = session.query(Sale).all()  #query all sales
        if not sales:  # If no sales are found
            return "No sales found."
        # Return a list of sales with formatted details
        return [f"Sale ID: {sale.id}, Product ID: {sale.product_id}, Counter ID: {sale.counter_id}, Counter Name: {sale.counter.username}" for sale in sales]
    finally:
        session.close()  # Ensure the session is always closed


# Counter Management Functions


# Function to add a counter which alsorequires admin password
def add_counter(username, password):
    if password != ADMIN_PASSWORD:
        return "Incorrect admin password."

    session = Session()
    new_counter = Counter(username=username)  # Create a new Counter object
    session.add(new_counter)  # Add the counter to the session

    try:
        session.commit()  # Commit changes to the database
        return f"Counter {username} added."
    except IntegrityError:  #catch IntegrityError
        session.rollback()  #rollback changes if theres an error
        return "Error adding counter. The counter may already exist."
    finally:
        session.close()  # close the session

# function that deletes a counter by username and also needs admin password
def delete_counter(username, password):
    if password != ADMIN_PASSWORD:
        return "Incorrect admin password."

    session = Session()
    try:
        #find the counter by its username
        counter = session.query(Counter).filter_by(username=username).first()
        if counter:  # If counter is found
            session.delete(counter)  #deleting the counter from the session
            session.commit()  # Commit changes to the database
            return f"Counter {username} deleted."
        else:
            return "Counter not found."
    finally:
        session.close()



def view_counters():
    session = Session()
    try:
        counters = session.query(Counter).all()  #ask for all counters
        if not counters:
            return "No counters found."
        return [f"ID: {counter.id}, Username: {counter.username}" for counter in counters]
    finally:
        session.close()
