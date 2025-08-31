import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

# Set page config
st.set_page_config(page_title="Yoga Feedback Form", page_icon="🧘", layout="centered")

# Load credentials from Streamlit secrets
creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"])
client = gspread.authorize(creds)

# Open your Google Sheet
sheet = client.open("Yoga Feedback").sheet1

# Streamlit Form
st.title("Yoga Feedback Form")
st.write("Please fill in the details below")

with st.form("feedback_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    feedback = st.text_area("Your Feedback")
    rating = st.slider("Rate the class (1-5)", 1, 5, 3)
    submit = st.form_submit_button("Submit")

    if submit:
        sheet.append_row([name, email, feedback, rating])
        st.success("Thank you for your feedback!")
