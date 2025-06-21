import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Set Gemini key
genai.configure(api_key=api_key)

# Supported Languages
languages = sorted([
    "Urdu", "French", "Spanish", "German", "Chinese", "Japanese", "Korean", "Arabic",
    "Portuguese", "Russian", "Hindi", "Bengali", "Turkish", "Italian", "Dutch", "Greek",
    "Polish", "Swedish", "Thai", "Vietnamese", "Hebrew", "Malay", "Czech", "Romanian", "Finnish"
])

# --- UI Setup ---
st.set_page_config(page_title="🌍 AI Translator", layout="centered")

# --- Custom CSS for style ---
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

# --- Title and Info ---
st.markdown("## 🌐 AI Translator")
st.markdown("Translate your English text into **25+ global languages** using Gemini AI.")
st.markdown("Created with ❤️ by **Maria Kousar** ")

st.markdown("---")

# --- Input Section ---
st.markdown("### 📝 Enter Text")
text = st.text_area("Enter English text:", height=140, placeholder="Type something like: Hello, how are you?")

st.markdown("### 🌍 Select Language")
lang = st.selectbox("Target language:", languages)

# --- Translate Button ---
btn = st.button("🔁 Translate")

# --- Output ---
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
