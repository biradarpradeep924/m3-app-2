from ._anvil_designer import subjectTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class subject(subjectTemplate):
  def __init__(self,arg1, **properties):
    # Set Form properties and Data Bindings.
    self.arg1=arg1
    self.label_1=self.arg1
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
