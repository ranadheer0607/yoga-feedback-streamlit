import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Define the scopes for Google Sheets & Drive API
scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

# Load credentials from Streamlit secrets
creds = Credentials.from_service_account_info(
    st.secrets["gcp_service_account"], scopes=scope
)

# Authorize client
client = gspread.authorize(creds)

# Open the spreadsheet and sheet
spreadsheet = client.open("Yoga Feedback")  # Replace with your sheet name
sheet = spreadsheet.sheet1  # Use .worksheet("SheetName") if multiple sheets

# Example: Write something to the sheet
sheet.append_row(["Name", "Feedback", "Date"])

# Example: Read data from sheet
data = sheet.get_all_records()
st.write("Current Data in Sheet:")
st.write(data)
