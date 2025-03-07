from ._anvil_designer import Form2Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form2(Form2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.drop_down_1.items = ["Student", "Teacher", "CR","Alumni"]
    self.init_components(**properties)
    if self.drop_down_1.selected_value == "Student" or self.drop_down_1.selected_value == "CR":
      self.text_box_5.visible = True
    else:
      self.text_box_5.visible = False
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name1=self.text_box_1.text
    email1=self.text_box_2.text
    phone1=self.text_box_3.text
    no = int(phone1)
    item = self.drop_down_1.selected_value
    password1=self.text_box_4.text
    class1=self.text_box_5.text
    response = server.call('add_data_to_table', name1, email1,no,password1,item,class1)
    print(response)

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1')

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    selected_item = self.drop_down_1.selected_value
    print("Selected item:", selected_item)

  # def text_box_2_pressed_enter(self, **event_args):
  #   """This method is called when the user presses Enter in this text box"""
  #   email=self.text_box_2.text
  #   pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9\.]+$'
    
  #   # Check if the email matches the pattern
  #   if re.match(pattern, email):
  #       alert("CORRECT")
  #   else:
  #       alert("Incorrect format")

# Define event handling function for TextBox change event
def validate_email_change(text_box_2, **event_args):
    """This method is called when the text in the TextBox changes"""
    
    # Retrieve the current text entered in the TextBox
    form = Form2()
    entered_email = text_box_2.text
    pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9\.]+$'
    
    # Check if the email matches the pattern
    # Check if the entered email matches the pattern
    if pattern == entered_email:
        # label_error.text = ""# Clear any previous error message
        alert("")
    else:
        alert("Invalid email format") # Show error message to the user
    
# Bind the event handler to the TextBox component
form = Form2()
form.text_box_2.set_event_handler("change", validate_email_change)

    
    
    
