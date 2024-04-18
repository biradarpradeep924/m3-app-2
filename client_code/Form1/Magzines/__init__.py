from ._anvil_designer import MagzinesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Magzines(MagzinesTemplate):
  def __init__(self,arg1, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.arg1=arg1
    class4=server.call('find_class',self.arg1)
    media =server.call('retrieve_media_from_database4',class4)
    if media is not None:
           # Convert the length of the media list to a string
            media_count = str(len(media))
            alert(media_count + " Media Uploaded")
    else:
            alert("No media found")
    # Any code you write here will run before the form opens.
    descriptions=server.call('get_desc12',class4)
    i= enumerate(descriptions)
          
    for i, description in enumerate(descriptions):
    # Add 1 to i because enumerate starts from 0
           i += 1
           if i == 1:
              self.label_3.text = description
           elif i == 2:
              self.label_3_copy.text = description
           elif i == 3:
              self.label_3_copy_2.text = description
           elif i == 4:
             self.label_3_copy_4.text = description
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student",self.arg1)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")
    
  def open_media(self, **event_args):
        # Use JavaScript to open the media link in a new window/tab
        js_code = f"window.open('{self.media_link}')"
        anvil.js.call(js_code)

  def button_3_click(self, **event_args):
      """This method is called when the button is clicked"""
      class4=server.call('find_class',self.arg1)
      media =server.call('retrieve_media_from_database4',class4)
      self.media_link = anvil.media.download(media[0])
      self.button_3.text = "Open Document"
      self.button_3.set_event_handler("click", self.open_media)

  def button_4_click(self, **event_args):
      """This method is called when the button is clicked"""
      class4=server.call('find_class',self.arg1)
      media =server.call('retrieve_media_from_database4',class4)
      self.media_link = anvil.media.download(media[1])
      self.button_4.text = "Open Document"
      self.button_4.set_event_handler("click", self.open_media)
    
  def button_5_click(self, **event_args):
      """This method is called when the button is clicked"""
      class4=server.call('find_class',self.arg1)
      media =server.call('retrieve_media_from_database4',class4)
      self.media_link = anvil.media.download(media[2])
      self.button_5.text = "Open Document"
      self.button_5.set_event_handler("click", self.open_media)   
