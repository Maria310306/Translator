# 

import os
import streamlit as st
# from dotenv import load_dotenv # Option 1: Comment out if using st.secrets exclusively
import google.generativeai as genai

# --- API Key Configuration ---
# On Streamlit Cloud, st.secrets is the recommended way to handle sensitive info.
# You need to add your GEMINI_API_KEY to your Streamlit app's secrets.toml
# (or directly in the Streamlit Cloud app settings under "Secrets").
#
# Example content for Streamlit Cloud's "Secrets" text area (TOML format):
# GEMINI_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY_HERE"
#
# If you are still developing locally and using a .env file:
# load_dotenv() # Uncomment this line if you are running locally with a .env file

try:
    # Attempt to get the API key from Streamlit secrets (for deployed apps)
    api_key = st.secrets["GEMINI_API_KEY"]
except KeyError:
    # Fallback to os.getenv (for local development with .env or if directly set in system env)
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("GEMINI_API_KEY not found! Please set it in Streamlit Secrets or a .env file.")
        st.stop() # Stop the app if API key is not found

genai.configure(api_key=api_key)

# --- Rest of your Streamlit App Code ---

languages = sorted([
    "Urdu", "French", "Spanish", "German", "Chinese", "Japanese", "Korean", "Arabic",
    "Portuguese", "Russian", "Hindi", "Bengali", "Turkish", "Italian", "Dutch", "Greek",
    "Polish", "Swedish", "Thai", "Vietnamese", "Hebrew", "Malay", "Czech", "Romanian", "Finnish"
])

st.set_page_config(page_title="🌍 AI Translator", layout="centered")


st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextArea textarea {
            font-size: 16px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 0.6em 1.5em;
            border: none;
            border-radius: 5px;
            font-size: 16px;
        }
        .stSelectbox div[data-baseweb="select"] {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)


st.markdown("## 🌐 AI Translator")
st.markdown("Translate your English text into **25+ global languages** using Gemini AI.")
st.markdown("Created with ❤️ by Maria Kousar")

st.markdown("---")


st.markdown("### 📝 Enter Text")
text = st.text_area("Enter English text:", height=140, placeholder="Type something like: Hello, how are you?")

st.markdown("### 🌍 Select Language")
lang = st.selectbox("Target language:", languages)

btn = st.button("🔁 Translate")


if btn and text:
    try:
        with st.spinner("Translating... Please wait..."):
            model = genai.GenerativeModel('gemini-1.5-flash')
            prompt = f"Translate the following text to {lang}:\n\n{text}"
            response = model.generate_content(prompt)

        st.markdown("### ✅ Translation")
        st.success(f"Translated to **{lang}**:")
        st.markdown(f"<div style='font-size:20px; color:#1a1a1a; padding:10px; background-color:#eaf4ff; border-left: 4px solid #1f77b4; border-radius:4px'>{response.text}</div>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")