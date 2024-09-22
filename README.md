**Motor World CLI**
A command-line interface (CLI) program for managing products, sales, and counters in a motor dealership application. This program allows administrators to add, delete, and view products and sales, as well as manage counter usernames.

**Features**
**Manage Products:**

Add new products with a name and price.
Delete existing products by ID.
View a list of all products.

**Manage Sales:**
Record sales of products by counters.
View all recorded sales.

**Manage Counters:**
Add new counters (users).
Delete existing counters by username.
View a list of all counters.

**Requirements**
Python 3.8 or higher
SQLAlchemy
Click
Alembic

**Installation**

1. Clone the repository:
bash
git clone https://github.com/yourusername/motor_world_CLI.git
cd motor_world_CLI

2. Create and activate a virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

3. Install the required packages:
pip install -r requirements.txt

4. Set up the database with Alembic:
alembic upgrade head

**Usage**
To start the CLI program, run:
python cli.py
Follow the on-screen prompts to manage products, sales, and counters.

**Menu Options**
**Main Menu:**

1. Manage Products
2. Manage Sales
3. Manage Counters
4. Exit

**Product Management:**

1. Add Product: Enter the product name, price, and admin password.
2. Delete Product: Enter the product ID and admin password.
3. View Products: Displays a list of all products.

**Sale Management:**

1. Add Sale: Enter product ID and counter username.
2. View Sales: Displays a list of all sales.

**Counter Management:**

1. Add Counter: Enter the username and admin password.
2. Delete Counter: Enter the username and admin password.
3. View Counters: Displays a list of all counters.

**Contributions**

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

**Author**
Hannington Owiti