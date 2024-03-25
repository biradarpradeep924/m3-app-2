from ._anvil_designer import Form1Template
from anvil import *

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
      
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    user =text_box_1.text
    pass1=text_box_2.text
    count=0
    if user!="admin":
       count=1
    elif pass1!="Admin@12":
      count=2
    if count==1:
        alert("Please chech your username")
    if count==2:
        alert("Please check your password!!!")
    if count==0:
      alert("Successfully submited")
     
