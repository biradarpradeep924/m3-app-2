
from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
      
    # Any code you write here will run before the form opens.
  
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    username = self.text_box_1.text
    password = self.text_box_2.text
    role1=server.call('get_role_by_name', username)
    password2 = server.call('get_password_by_name', username)
    # if password ==password2 and role1=="Student":
    #           alert("successfully login") 
    #           open_form("Student1")
    # elif  password ==password2 and role1=="Teacher":
    #           alert("successfully login") 
    #           open_form("Teacher")
    # elif password ==password2 and role1=="Alumni":
    #           alert("successfully login") 
    #           open_form("Alumni")
    # elif password ==password2 and role1=="BR":
    #           alert("successfully login") 
    #           open_form("BR")
    # else:
    #          alert("Invalid username or password. Please try again.")
    if  password ==password2:
      if role1=="Student":
          alert("successfully login") 
          open_form("Form1.Student",arg1=username)
      elif role1=="Teacher":
           alert("successfully login") 
           open_form("Form1.Teacher",arg1=username)
      elif role1=="Alumni":
           alert("successfully login") 
           open_form("Form1.Alumni",arg1=username)
      elif role1=="CR":
           alert("successfully login") 
           open_form("Form1.CR",username)
      elif role1=="Admin":
        alert("Successfully login")
        open_form('Form1.Admin',username)
      else:alert("Role is not selected please sign-up!!!")  
    else: alert("Invalid username or password. Please try again.")
       
  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Form1.Form2")

 

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Call the server function to get the password
    name = self.text_box_1.text
    password = server.call('get_password_by_name', name)
    alert(password)
    

     
