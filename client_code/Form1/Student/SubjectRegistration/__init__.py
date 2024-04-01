from ._anvil_designer import SubjectRegistrationTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class SubjectRegistration(SubjectRegistrationTemplate):
  def __init__(self,class2,arg2, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.class2=class2
    self.arg2=arg2
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
    super().__init__(**properties)
                    
    # Any code you write here will run before the form opens.

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Student.profile',self.arg2)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.check_box_1.checked:
          sub1=self.check_box_1.text;
    else:
          sub1="None"

    if self.check_box_2.checked:
          sub2=self.check_box_2.text;
    else:
          sub2="None"

    if self.check_box_3.checked:
          sub3=self.check_box_3.text;
    else:
          sub3="None"

    if self.check_box_4.checked:
          sub4=self.check_box_4.text;
    else:
          sub4="None"

    if self.check_box_5.checked:
          sub5=self.check_box_5.text;
    else:
          sub5="None"

    if self.check_box_6.checked:
          sub6=self.check_box_6.text;
    else:
          sub6="None"
    if self.check_box_7.checked:
          sub7=self.check_box_7.text;
    else:
          sub7="None"
    
    response = server.call('add_data_to_table1',self.arg2,self.class2,sub1,sub2,sub3,sub4,sub5,sub6,sub7)
    print(response)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student",self.arg2)
    
