from ._anvil_designer import StudentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Student(StudentTemplate):
  def __init__(self,arg1,**properties):
    # Set Form properties and Data Bindings.
    self.arg1=arg1
    
    self.init_components(**properties)
    super().__init__(**properties)
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")

  def button_2_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    class2=server.call('get_class2_by_name',self.arg1)
    open_form("Form1.Student.subject",class2,self.arg1)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    class3=server.call('get_class2_by_name',self.arg1)
    open_form("Form1.Student.Form3",self.arg1,class3)

  def button_2_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Research",self.arg1)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student.profile",arg2=self.arg1)

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    class2=server.call('get_class2_by_name',self.arg1)
    open_form("Form1.Student.SubjectRegistration",class2,arg2=self.arg1)

  def button_2_copy_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Magzines",self.arg1)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    class2=server.call('get_class2_by_name',self.arg1)
    open_form("Form1.Student.Placement",class2)
