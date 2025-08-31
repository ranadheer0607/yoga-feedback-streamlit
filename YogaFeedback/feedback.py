import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime

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


# Step 2: Open your Google Sheet
sheet = client.open("Yoga Feedback").sheet1

# Check first row; if it's empty or wrong, add headers
existing_data = sheet.get_all_values()
expected_headers = ["Timestamp", "Name", "Rating", "Liked", "Suggestions", "Regular Attendance"]

if not existing_data or existing_data[0] != expected_headers:
    sheet.insert_row(expected_headers, 1)

# Streamlit UI
st.title("Ranadheer's Yoga Class Feedback")

st.set_page_config(page_title="Ranadheers Yoga Class Feedback", page_icon="🧘", layout="centered")

name = st.text_input("Your Name")
rating = st.slider("Rate today's session (1=Poor, 5=Excellent)", 1, 5, 3)
liked = st.multiselect("What did you like today?", ["Asanas", "Pranayama", "Meditation", "Relaxation", "Other"])
improvement = st.text_area("Any suggestions for improvement?")
regular = st.radio("Do you plan to attend regularly?", ["Yes", "No", "Maybe"])

# Step 3: Submit Feedback
if st.button("Submit Feedback"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sheet.append_row([timestamp, name, rating, ", ".join(liked), improvement, regular])
    st.success("Thank you for your feedback! 🙏")

