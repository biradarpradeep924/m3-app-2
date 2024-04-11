import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
# server_module.py

@anvil.server.callable
def add_data_to_table(name, email, phone, password,role,class2):
    try:
        # Access 'Table2' and insert data
        table2 = app_tables.table_2
        table2.add_row(name=name, Email=email, phone=phone, password=password,role=role,sclass=class2)
        return "Data added successfully."
    except Exception as e:
        return "Error: " + str(e)
      
@anvil.server.callable
def get_password_by_name(username):
    # Search for the user by name
    user = app_tables.table_2.get(name=username)
    if user is not None:
        # Access the password column directly
        password = user['password']
        return password
    else:
        return None

@anvil.server.callable
def get_role_by_name(username):
    user = app_tables.table_2.get(name=username)
    if user is not None:
        # Access the password column directly
        password = user['role']
        return password
    else:
        return None
@anvil.server.callable
def get_mono_by_name(username):
    user = app_tables.table_2.get(name=username)
    if user is not None:
        # Access the password column directly
        password = user['phone']
        return password
    else:
        return None

@anvil.server.callable
def get_mail_by_name(username):
    user = app_tables.table_2.get(name=username)
    if user is not None:
        # Access the password column directly
        password = user['Email']
        return password
    else:
        return None

@anvil.server.callable
def get_class2_by_name(username):
    user = app_tables.table_2.get(name=username)
    if user is not None:
        # Access the password column directly
        password = user['sclass']
        return password
    else:
        return None
         
@anvil.server.callable
def add_data_to_table1(name,class2,sub1,sub2,sub3,sub4,sub5,sub6,sub7):
    try:
        # Access 'Table2' and insert data
        table1 = app_tables.table_1
        table1.add_row(class2=class2,name=name,sub1=sub1,sub2=sub2,sub3=sub3,sub4=sub4,sub5=sub5,sub6=sub6,sub7=sub7)
        return "Data added successfully."
    except Exception as e:
        return "Error: " + str(e)
      
@anvil.server.callable    
def get_sub_by_name(name,sub):
    user1= app_tables.table_1.get(name=name)
    if user1 is not None:
        subject = user1[sub]
        return subject
    else:
        return None


@anvil.server.callable
def add_data_to_table3(name,class2,stored_document,desc,sub,date):
  try:
    table1 = app_tables.table_3
    table1.add_row(name=name,class2=class2,document=stored_document,desc=desc,sub=sub,date=date)
    return "Data added successfully."
  except Exception as e:
        return "Error: " + str(e)

@anvil.server.callable
def retrieve_media_from_database(sub1,class2):
  try:
    row = app_tables.table_3.get(sub=sub1,class2=class2)
    if row is None:
        return None
    media=row['document']
    return media
  except Exception as e:
        print("Error retrieving data:", e)
        return None

    
@anvil.server.callable
def get_desc1(sub1,class2):
   try:
    row = app_tables.table_3.get(sub=sub1,class2=class2)
    if row is None:
        return None
      
        # Append the media file (stored in the 'document' column) to the list
    desc1_values=row['desc']
    return desc1_values
   except Exception as e:
        print("Error retrieving data:", e)
        return None
     
@anvil.server.callable
def get_description(class2):
    try:
        # Query the Anvil Data Table to retrieve all rows matching the given condition
        rows = app_tables.table_4.search(Class3=class2)
        
        # Initialize an empty list to store the descriptions
        desc_values = " "
        
        # Iterate over all matched rows
        for i, row in enumerate(rows):
            desc_values+=row['Announcement']+'\n'
            
            # Check if it's not the last row
           
        return desc_values
    except Exception as e:
        print("Error retrieving data:", e)
        return None