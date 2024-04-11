from ._anvil_designer import frameTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.media

class frame(frameTemplate):
  def __init__(self,sub,class2, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.class2=class2
    self.sub=sub
    media1=server.call('retrieve_media_from_database',self.sub,self.class2)
    desc1=server.call('get_desc1',self.sub,self.class2)
    self.label_1.text=desc1
    self.button_1.media=media1
    # image_media = anvil.media.from_url(media[0])
    # self.button_1.media = image_media
    #self.button_1.media=media[0]
    # self.button_2.icon=media[1]
   
    # Any code you write here will run before the form opens.

 
    
    
