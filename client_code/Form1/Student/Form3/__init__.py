from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form3(Form3Template):
  def __init__(self,name,class2, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.class2=class2
    self.name=name
    desc=server.call('get_description',self.class2)
    self.text_area_1.text=desc
    # Any code you write here will run before the form opens.
    descriptions=server.call('get_desc4',self.class2)
    i= enumerate(descriptions)
          
    for i, description in enumerate(descriptions):
    # Add 1 to i because enumerate starts from 0
           i += 1
           if i == 1:
              self.label_3.text = description
           elif i == 2:
              self.label_4.text = description
          

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student","")
