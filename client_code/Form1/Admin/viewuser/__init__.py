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
  
    for user in users:
            if isinstance(user, dict):  # Check if user is a dictionary
                # Create a label for each user
                label = Label(text=user.get('name', ''))  # Get user's name from dictionary
            
                # Add the label to the panel in your Anvil app
                self.xy_panel_1.add_component(label)
            else:
                print("User data is not in expected format:", user)
 
