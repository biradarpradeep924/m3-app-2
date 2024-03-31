from ._anvil_designer import SubjectRegistrationTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SubjectRegistration(SubjectRegistrationTemplate):
  def __init__(self,class2, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.class2=class2
    alert(self.class2)
    if self.class2=="SY-IT":
      self.check_box_1.text="Computer Network"
      self.check_box_2.text="Probability And Statistics"
      self.check_box_3.text="Data Structure and File"
      self.check_box_4.text="Universal Human Values"
      self.check_box_5.text="Software Engineering"
      self.check_box_6.text="IT- Workshop2"
      self.check_box_7.text="Soft Skills"
    elif  self.class2=="SY-IT":
      self.check_box_1.text="Computer Network2"
      self.check_box_2.text="Probability And Statistics2"
      self.check_box_3.text="Data Structure and File2"
      self.check_box_4.text="Universal Human Values2"
      self.check_box_5.text="Software Engineering2"
      self.check_box_6.text="IT- Workshop2"
      self.check_box_7.text="Soft Skills2"

                    
    # Any code you write here will run before the form opens.
