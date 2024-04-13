from ._anvil_designer import frameTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.media

class frame(frameTemplate):
    def __init__(self, sub, class2, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.class2 = class2
        self.sub = sub
        media =server.call('retrieve_media_from_database', self.sub, self.class2)
        if media is not None:
           # Convert the length of the media list to a string
            media_count = str(len(media))
            alert(media_count + " Media Uploaded")
        else:
            alert("No media found")
       
        descriptions=server.call('get_desc1',self.sub,self.class2)
        self.label_1.text=descriptions[0]
        self.label_2.text=descriptions[1]
      
        
        

    def open_media(self, **event_args):
        # Use JavaScript to open the media link in a new window/tab
        js_code = f"window.open('{self.media_link}')"
        anvil.js.call(js_code)

    def button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      media =server.call('retrieve_media_from_database', self.sub, self.class2)
      self.media_link = anvil.media.download(media[0])
      self.button_1.text = "Open Document"
      self.button_1.set_event_handler("click", self.open_media)

    def button_2_click(self, **event_args):
      """This method is called when the button is clicked"""
      media = anvil.server.call('retrieve_media_from_database', self.sub, self.class2)
      self.media_link = anvil.media.download(media[1])
      self.button_2.text = "Open Document"
      self.button_2.set_event_handler("click", self.open_media)
      

    def button_4_click(self, **event_args):
      """This method is called when the button is clicked"""
      open_form("Form1.Student","c")
