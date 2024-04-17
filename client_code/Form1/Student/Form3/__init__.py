from ._anvil_designer import Form3Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form3(Form3Template):
  def __init__(self,name,class2, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.class2=class2
    self.name=name
    desc=server.call('get_description',self.class2)
    self.text_area_1.text=desc
    # Any code you write here will run before the form opens.
    descriptions = server.call('get_desc4', self.class2)
    if len(descriptions) >= 1:
     self.label_3.text = descriptions[0]
    if len(descriptions) >= 2:
     self.label_4.text = descriptions[1]
           
          

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student","")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    media = server.call('retrieve_media_from_database2', self.class2)
    if media[0] is not None:
        try:
            self.media_link = anvil.media.download(media[0])
            self.button_1.text = "Open Document"
            self.button_1.set_event_handler("click", self.open_media)
        except Exception as e:
            # Log any errors that occur
            print("Error downloading media:", e)
    else:
        print("Media is None, cannot download")

  def button_1_copyclick(self, **event_args):
    """This method is called when the button is clicked"""
    media = server.call('retrieve_media_from_database2', self.class2)
    if media[0] is not None:
        try:
            self.media_link = anvil.media.download(media[1])
            self.button_1.text = "Open Document"
            self.button_1.set_event_handler("click", self.open_media)
        except Exception as e:
            # Log any errors that occur
            print("Error downloading media:", e)
    else:
        print("Media is None, cannot download")
