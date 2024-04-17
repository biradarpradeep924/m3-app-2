from ._anvil_designer import CRTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
# import requests  
# import io  

class CR(CRTemplate):
  def __init__(self,name, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name=name
    # Any code you write here will run before the form opens.


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    desc=self.text_area_1.text
    desc2=self.text_area_2.text
    document_bytes = self.file_loader_1.file.get_bytes()  # Get the bytes of the uploaded file
    content_type = self.file_loader_1.file.get_content_type()  # Get the content type of the uploaded file
    document=anvil.BlobMedia(content_type, document_bytes) 
    class3=server.call('get_class_by_name_',self.name)
    response = server.call('add_data_to_table5',class3,desc,desc2,document)
    print(response)
