from ._anvil_designer import PlacementTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Placement(PlacementTemplate):
  def __init__(self,arg1, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.arg1=arg1
    media =server.call('retrieve_media_from_database56',self.arg1)
    if media is not None:
           # Convert the length of the media list to a string
          h=4
    else:
            alert("No media found")
    if len(media)==1:
          self.label_4.visible = True
          self.button_2.visible=False
          self.button_3.visible=False
          self.button_1.enabled=True
    descriptions=server.call('get_desc178',self.arg1)
    i=enumerate(descriptions)   
    for i, description in enumerate(descriptions):
    # Add 1 to i because enumerate starts from 0
           i += 1
           if i == 1:
              self.label_4.text = description
           elif i == 2:
              self.label_2.text = description
           elif i == 3:
              self.label_3.text = description
    # Any code you write here will run before the form opens.

  def open_media(self, **event_args):
        # Use JavaScript to open the media link in a new window/tab
        js_code = f"window.open('{self.media_link}')"
        anvil.js.call(js_code)
        

  def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      media =server.call('retrieve_media_from_database56',self.arg1)
      self.media_link = anvil.media.download(media[0])
      self.button_1.text = "Open Document"
      self.button_1.set_event_handler("click", self.open_media)

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1")
