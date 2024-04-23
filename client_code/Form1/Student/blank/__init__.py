from ._anvil_designer import blankTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class blank(blankTemplate):
  def __init__(self,js_code,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.js_code=js_code
    anvil.js.call(js_code)
    # Any code you write here will run before the form opens.
