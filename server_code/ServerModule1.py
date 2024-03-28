import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
# server_module.py

@anvil.server.callable
def add_data_to_table(name, email, phone, password,role):
    try:
        # Access 'Table2' and insert data
        table2 = app_tables.table_2
        table2.add_row(name=name, Email=email, phone=phone, password=password,role=role)
        return "Data added successfully."
    except Exception as e:
        return "Error: " + str(e)
      
@anvil.server.callable
def get_password_by_name(username):
    # Search for the user by name
    user = app_tables.table_2.get(name=username)
    if user is not None:
        # Access the password column directly
        password = user['password']
        return password
    else:
        return None

@anvil.server.callable
def get_role_by_name(username):
    user = app_tables.table_2.get(name=username)
    if user is not None:
        # Access the password column directly
        password = user['role']
        return password
    else:
        return None

         
