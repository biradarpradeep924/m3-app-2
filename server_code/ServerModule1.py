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
def add_data_to_table(name, email, phone, password):
    try:
        # Access 'Table2' and insert data
        table2 = app_tables.Table2
        table2.add_row(name=name, email=email, phone=phone, password=password)
        return "Data added successfully."
    except Exception as e:
        return "Error: " + str(e)
