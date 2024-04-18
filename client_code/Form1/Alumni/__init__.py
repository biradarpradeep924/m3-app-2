from ._anvil_designer import AlumniTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Alumni(AlumniTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.drop_down_1.items = ["SY-IT","SY-CO"]
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    class2=self.drop_down_1.selected_value
    document_bytes = self.file_loader_1.file.get_bytes()  # Get the bytes of the uploaded file
    content_type = self.file_loader_1.file.get_content_type()  # Get the content type of the uploaded file
    document=anvil.BlobMedia(content_type, document_bytes) 
    desc=self.text_area_1.text
    selected_value = self.radio_buttons_1.selected_value
        if selected_value is not None:
            type=self.radio_buttons_1.selected_value
        else:
           type=self.radio_buttons_2.selected_value
            
    response = server.call('add_data_to_table31',class2,document,desc,type)
    print(response)

