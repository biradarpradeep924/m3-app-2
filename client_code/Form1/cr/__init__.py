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

@anvil.server.callable
def create_announcement(announcement_text, document_link=None):
    # Save announcement to data table
    AnnouncementTable.add_row(
        announcement_text=announcement_text,
        date_time=datetime.now(),
        document_link=document_link
    )

@anvil.server.callable
def get_announcements():
    # Fetch announcements sorted by date/time
    announcements = sorted(app_tables.Announcements.search(), key=lambda x: x['date_time'], reverse=True)
    return announcements

@anvil.server.callable
def fetch_document(document_link):
    # Function to fetch document based on document link
    # Implement logic to fetch document from storage or external link
    if document_link:
        # Check if the document link is an external URL or a file stored in Anvil
        if document_link.startswith("http"):
            # If the document link is an external URL
            try:
                response = requests.get(document_link)
                if response.status_code == 200:
                    document_content = response.content  # Fetch document content from the URL
                    return document_content
                else:
                    return None  # Unable to fetch document
            except Exception as e:
                print("Error fetching document:", e)
                return None
        else:
            # If the document link is stored in Anvil's file system
            try:
                with open(document_link, "rb") as file:
                    document_content = file.read()  # Read document content from the file
                    return document_content
            except Exception as e:
                print("Error fetching document:", e)
                return None
    else:
        return None  # No document link provided
    return document_content  # Return document content