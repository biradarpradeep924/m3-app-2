from ._anvil_designer import SeniorTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Senior(SeniorTemplate):
  def __init__(self,name, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_1.items = ["SY-IT","SY-CO"]
    self.name=name
    
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    item1 = self.drop_down_1.selected_value
    desc=self.text_area_1.text
    document_bytes = self.file_loader_1.file.get_bytes()  # Get the bytes of the uploaded file
    content_type = self.file_loader_1.file.get_content_type()  # Get the content type of the uploaded file
    document=anvil.BlobMedia(content_type, document_bytes)
    response = server.call('add_data_to_table32',item1,desc,document)
    print(response)

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")
    
    
