from ._anvil_designer import TeacherTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Teacher(TeacherTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_1.items = ["SY-IT","SY-CO"]
    # Any code you write here will run before the form opens.
    if self.drop_down_1.selected_value=="SY-IT":
      self.drop_down_2.items=["Computer Network","Probability And Statistics","Data Structure and File","Universal Human Values","Software Engineering","IT- Workshop2","Soft Skills"]
    else:
      self.drop_down_2.items=["Computer Network2","Probability And Statistics2","Data Structure and File2","Universal Human Values2","Software Engineering2","IT- Workshop2","Soft Skills2"]
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1") 
    

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
  
