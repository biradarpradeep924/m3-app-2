from ._anvil_designer import Form4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form4.Form5")

  def button_1_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form4.Form5")

  def button_1_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form4.Form5")

  def button_1_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form4.Form5")

  def button_1_copy_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form4.Form5")




