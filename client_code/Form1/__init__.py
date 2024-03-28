from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
      
    # Any code you write here will run before the form opens.
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    username = self.text_box_1.text
    password = self.text_box_2.text

    if username == "admin" and password == "admin123":
              alert("successfully login") 
              open_form("Form1.Home")
    else:
             alert("Invalid username or password. Please try again.")

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Form2")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    name1= self.text_box_1.text
    rows = app_tables.table_2.search(name=name1)
    for row in rows:
     print(row)
    

     
