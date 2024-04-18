from ._anvil_designer import viewuserTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class viewuser(viewuserTemplate):
  def __init__(self,name, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name=name
    class4=server.call("get_class",self.name)
    users=server.call("get_user",class4)
    

# Iterate over the users
    x_position = 40
    y_position = 10

# Iterate over the users
    for user in users:
     print("x_position:", x_position, "y_position:", y_position)
     label = Label(text=user)
     label.x = x_position
     label.y = y_position
     self.xy_panel_1.add_component(label)
     y_position += 30 
     x_position += 100




  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Admin',"")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")
 
