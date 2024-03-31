from ._anvil_designer import profileTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class profile(profileTemplate):
  def __init__(self,arg2, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.arg2=arg2
    self.label_1.text=arg2
    role1=server.call('get_role_by_name',self.arg2)
    mono=server.call('get_mono_by_name',self.arg2)
    class2=server.call('get_class2_by_name',self.arg2)
    mail=server.call('get_mail_by_name',self.arg2)
    self.label_5.text=mail
    self.label_7.text=class2
    self.label_10.text=mono
    self.label_3.text=role1
    
    
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1","hii")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student","hii")
