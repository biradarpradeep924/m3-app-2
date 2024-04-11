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
def get_media_by_name(sub1):
    media_records = app_tables.table_3.search(sub=sub1)

    # List to store fetched media files
    media_files = []

    # Iterate through each record and retrieve the media file
    for record in media_records:
        media_files.append(record['document'])

    return media_files