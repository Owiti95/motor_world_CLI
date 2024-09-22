# cli.py

import click
from helpers import (
    add_product, delete_product, view_products,
    add_sale, view_sales,
    add_counter, delete_counter, view_counters
)

@click.group()
def cli():
    """Main CLI for Sales Management."""
    pass

# Main menu loop
@cli.command()
def main_menu():
    """Main menu for the CLI."""
    while True:
        click.echo("\nMain Menu:")
        click.echo("1. Manage Products")
        click.echo("2. Manage Sales")
        click.echo("3. Manage Counters")
        click.echo("4. Exit")
        choice = click.prompt("Choose an option", type=int)

        if choice == 1:
            manage_products()
        elif choice == 2:
            manage_sales()
        elif choice == 3:
            manage_counters()
        elif choice == 4:
            click.echo("Exiting the program.")
            break
        else:
            click.echo("Invalid option. Please try again.")

# Product Management
def manage_products():
    """Manage products in a loop."""
    while True:
        click.echo("\nProduct Management:")
        click.echo("1. Add Product")
        click.echo("2. Delete Product")
        click.echo("3. View Products")
        click.echo("4. Go Back to Main Menu")
        choice = click.prompt("Choose an option", type=int)

        if choice == 1:
            name = click.prompt("Enter product name")
            price = click.prompt("Enter product price", type=int)
            password = click.prompt("Enter admin password", hide_input=True)
            result = add_product(name, price, password)
            click.echo(result)
        elif choice == 2:
            product_id = click.prompt("Enter product ID to delete", type=int)
            password = click.prompt("Enter admin password", hide_input=True)
            result = delete_product(product_id, password)
            click.echo(result)
        elif choice == 3:
            products = view_products()
            if isinstance(products, list):
                for product in products:
                    click.echo(product)
            else:
                click.echo(products)
        elif choice == 4:
            break
        else:
            click.echo("Invalid option. Please try again.")

# Sale Management
def manage_sales():
    """Manage sales in a loop."""
    while True:
        click.echo("\nSale Management:")
        click.echo("1. Add Sale")
        click.echo("2. View Sales")
        click.echo("3. Go Back to Main Menu")
        choice = click.prompt("Choose an option", type=int)

        if choice == 1:
            product_id = click.prompt("Enter product ID for sale", type=int)
            username = click.prompt("Enter counter username")
            result = add_sale(product_id, username)
            click.echo(result)
        elif choice == 2:
            sales = view_sales()
            if isinstance(sales, list):
                for sale in sales:
                    click.echo(sale)
            else:
                click.echo(sales)
        elif choice == 3:
            break
        else:
            click.echo("Invalid option. Please try again.")

# Counter Management
def manage_counters():
    """Manage counters in a loop."""
    while True:
        click.echo("\nCounter Management:")
        click.echo("1. Add Counter")
        click.echo("2. Delete Counter")
        click.echo("3. View Counters")
        click.echo("4. Go Back to Main Menu")
        choice = click.prompt("Choose an option", type=int)

        if choice == 1:
            username = click.prompt("Enter counter username")
            password = click.prompt("Enter admin password", hide_input=True)
            result = add_counter(username, password)
            click.echo(result)
        elif choice == 2:
            username = click.prompt("Enter counter username to delete")
            password = click.prompt("Enter admin password", hide_input=True)
            result = delete_counter(username, password)
            click.echo(result)
        elif choice == 3:
            counters = view_counters()
            if isinstance(counters, list):
                for counter in counters:
                    click.echo(counter)
            else:
                click.echo(counters)
        elif choice == 4:
            break
        else:
            click.echo("Invalid option. Please try again.")

if __name__ == '__main__':
    main_menu()
