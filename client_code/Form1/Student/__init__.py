from ._anvil_designer import StudentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Student(StudentTemplate):
  def __init__(self,arg1, **properties):
    # Set Form properties and Data Bindings.
    self.arg1=arg1
    alert("welcome "+arg1)
    self.init_components(**properties)
    super().__init__(**properties)
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")

  def button_2_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student.subject")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.announce")

  def button_2_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Research")

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student.profile",arg2=self.arg1)

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    class2=server.call('get_class2_by_name',self.arg1)
    open_form("Form1.Student.SubjectRegistration",class2,arg2=self.arg1)
