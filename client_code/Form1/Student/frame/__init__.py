from ._anvil_designer import frameTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.media

class frame(frameTemplate):
  def __init__(self,sub, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.sub=sub
    media=server.call('get_media_by_name',self.sub)
    image_media = anvil.media.from_url(media[0])
    self.button_1.media = image_media
    #self.button_1.media=media[0]
    # self.button_2.icon=media[1]
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
