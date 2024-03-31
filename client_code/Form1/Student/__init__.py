from ._anvil_designer import StudentTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Student(StudentTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")

  def button_2_copy_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Student.Form3")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.announce")

  def button_2_copy_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Research")
