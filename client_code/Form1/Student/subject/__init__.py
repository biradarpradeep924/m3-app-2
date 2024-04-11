from ._anvil_designer import subjectTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class subject(subjectTemplate):
  def __init__(self,arg1,arg2,**properties):
    # Set Form properties and Data Bindings.
    self.arg1=arg1
    self.arg2=arg2
    self.label_1.text=self.arg1
    self.label_4.text=self.arg1
    self.label_7.text=self.arg1
    self.label_10.text=self.arg1
    self.label_14.text=self.arg1
    self.label_17.text=self.arg1
    self.label_19.text=self.arg1
    subj1=server.call('get_sub_by_name',self.arg2,sub="sub1")
    self.label_2.text=subj1
    subj2=server.call('get_sub_by_name',self.arg2,sub="sub2")
    self.label_5.text=subj2
    subj3=server.call('get_sub_by_name',self.arg2,sub="sub3")
    self.label_8.text=subj3
    subj4=server.call('get_sub_by_name',self.arg2,sub="sub4")
    self.label_11.text=subj4
    subj5=server.call('get_sub_by_name',self.arg2,sub="sub5")
    self.label_15.text=subj5
    subj6=server.call('get_sub_by_name',self.arg2,sub="sub6")
    self.label_18.text=subj6
    subj7=server.call('get_sub_by_name',self.arg2,sub="sub7")
    self.label_19.text=subj7
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Student.frame',self.subj2)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Student.frame',self.subj1)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Student.frame',self.subj3)

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Student.frame',self.subj4)

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Student.frame',self.subj5)

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Student.frame',self.subj6)

  def button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1.Student.frame',self.subj7)
    
