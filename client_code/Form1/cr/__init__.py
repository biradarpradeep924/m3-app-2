from ._anvil_designer import crTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime
import requests  # for fetching documents from external URLs
import io  # for handling document content

class cr(crTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def text_area_1_change(self, **event_args):
    """This method is called when the text in this text area is edited"""
    pass
