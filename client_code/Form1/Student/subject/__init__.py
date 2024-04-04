from ._anvil_designer import subjectTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class subject(subjectTemplate):
  def __init__(self,arg1,arg2, **properties):
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
    subj=server.call('get_sub_by_name',self.arg2,sub="sub1")
    self.label_2.text=subj
    subj=server.call('get_sub_by_name',self.arg2,sub="sub2")
    self.label_5.text=subj
    subj=server.call('get_sub_by_name',self.arg2,sub="sub3")
    self.label_8.text=subj
    subj=server.call('get_sub_by_name',self.arg2,sub="sub4")
    self.label_11.text=subj
    subj=server.call('get_sub_by_name',self.arg2,sub="sub5")
    self.label_15.text=subj
    subj=server.call('get_sub_by_name',self.arg2,sub="sub6")
    self.label_18.text=subj
    subj=server.call('get_sub_by_name',self.arg2,sub="sub6")
    self.label_19.text=subj
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
