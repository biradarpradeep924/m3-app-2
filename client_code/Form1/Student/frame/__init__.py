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
          h=4
        else:
            alert("No media found")
        if len(media)==1:
          self.label_1.visible = True
          self.button_1_copy.visible=False
          self.button_1_copy_copy.visible=False
          self.button_2.visible=False
          self.button_3.visible=False
          self.button_3_copy.visible=False
          self.button_5_copy.visible=False
          self.button_5.visible=False
          self.button_1.enabled=True

        if len(media)==2:
          self.label_1.visible = True
          self.label_2.visible=True
          self.button_1_copy.enabled=False
          self.button_1_copy.visible=False
          self.button_1_copy_copy.visible=False
          self.button_2.visible=True
          self.button_3.visible=False
          self.button_3_copy.visible=False
          self.button_5_copy.visible=False
          self.button_5.visible=False
          self.button_1.visible=True

        if len(media)==3:
          self.label_1.visible = True
          self.label_2.visible=True
          self.label_2_copy.visible=True
          self.button_1_copy.enabled=True
          self.button_1_copy_copy.visible=False
          self.button_2.enabled=True
          self.button_3.visible=False
          self.button_3_copy.visible=False
          self.button_5_copy.visible=False
          self.button_5.visible=False
          self.button_1.enabled=True

        if len(media)==4:
          self.label_1.visible = True
          self.label_2.visible=True
          self.label_1_copy.visible=True
          self.label_2_copy.visible=True
          self.button_1_copy.enabled=True
          self.button_1_copy_copy.enabled=True
          self.button_2.enabled=True
          self.button_3.visible=False
          self.button_3_copy.visible=False
          self.button_5_copy.visible=False
          self.button_5.visible=False
          self.button_1.enabled=True

        
          
        descriptions=server.call('get_desc1',self.sub,self.class2)
        i= enumerate(descriptions)
          
        for i, description in enumerate(descriptions):
    # Add 1 to i because enumerate starts from 0
           i += 1
           if i == 1:
              self.label_1.text = description
           elif i == 2:
              self.label_2.text = description
           elif i == 3:
              self.label_3.text = description
           elif i == 4:
             self.label_4.text = description
        
        

    def open_media(self, **event_args):
        # Use JavaScript to open the media link in a new window/tab
        js_code = f"window.open('{self.media_link}')"
        open_form("Form1.Student.blank")

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
      open_form("Form1.Student","E")

    def button_3_click(self, **event_args):
      """This method is called when the button is clicked"""
      media = anvil.server.call('retrieve_media_from_database', self.sub, self.class2)
      try:
       self.media_link = anvil.media.download(media[2])
       self.button_3.text = "Open Document"
       self.button_3.set_event_handler("click", self.open_media)
      except Exception as e:
        # Log any errors that occur
        print("Error retrieving data:", e)

    def button_5_click(self, **event_args):
      """This method is called when the button is clicked"""
      media = anvil.server.call('retrieve_media_from_database', self.sub, self.class2)
      try:
       self.media_link = anvil.media.download(media[3])
       self.button_3.text = "Open Document"
       self.button_3.set_event_handler("click", self.open_media)
      except Exception as e:
        # Log any errors that occur
        print("Error retrieving data:", e)
      
      
