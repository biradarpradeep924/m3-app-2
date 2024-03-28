from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name1=self.text_box_1.text
    email1=self.text_box_2.text
    phone1=self.text_box_3.text
    no = int(phone1)
    password1=self.text_box_4.text
    response = server.call('add_data_to_table', name1, email1,no, password1)
    print(response)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    self.dropdown_1.items = ["Option 1", "Option 2", "Option 3"]

    
    
    
