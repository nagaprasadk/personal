import streamlit as st
import requests

# Title of the app
st.title("FastAPI Client with Streamlit")

# FastAPI backend URL (adjust if running in Docker or different host)
FASTAPI_URL = "http://127.0.0.1:8000"

# Button to call the root endpoint
if st.button("Get Message"):
    with st.spinner("Fetching data from FastAPI..."):
        try:
            response = requests.get(f"{FASTAPI_URL}/")
            if response.status_code == 200:
                data = response.json()
                st.success(f"Message: {data['message']}")
            else:
                st.error("Failed to fetch data")
        except requests.exceptions.ConnectionError:
            st.error("Connection error. Is the FastAPI server running?")
        except Exception as e:
            st.error(f"An error occurred: {e}")
