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

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Student",self.arg1)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1",self.arg1)
  def open_media(self, **event_args):
        # Use JavaScript to open the media link in a new window/tab
        js_code = f"window.open('{self.media_link}')"
        anvil.js.call(js_code)

  def button_1_copy_click(self, **event_args):
      """This method is called when the button is clicked"""
      media =server.call('retrieve_media_from_database', self.sub, self.class2)
      self.media_link = anvil.media.download(media[0])
      self.button_1_copy.text = "Open Document"
      self.button_1.set_event_handler("click", self.open_media)