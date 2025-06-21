import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai



load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# --- Check if API key is available ---
if not api_key:
    st.error("⚠️ Gemini API key not found. Please add it to your `.env` file as `GEMINI_API_KEY`.")
    st.stop()

# --- Configure Gemini AI ---
try:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as model_err:
    st.error(f"❌ Failed to configure Gemini model: {model_err}")
    st.stop()

# --- List of Languages ---
languages = sorted([
    "Urdu", "French", "Spanish", "German", "Chinese", "Japanese", "Korean", "Arabic",
    "Portuguese", "Russian", "Hindi", "Bengali", "Turkish", "Italian", "Dutch", "Greek",
    "Polish", "Swedish", "Thai", "Vietnamese", "Hebrew", "Malay", "Czech", "Romanian", "Finnish"
])

# --- Streamlit Page Config ---
st.set_page_config(page_title="🌍 AI Translator", layout="centered")

# --- Custom Styles ---
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

# --- Title & Instructions ---
st.markdown("## 🌐 AI Translator")
st.markdown("Translate your English text into **25+ global languages** using Gemini AI.")
st.markdown("Created with ❤️ by **Maria Kousar** ")
st.markdown("---")

# --- Text Input ---
st.markdown("### 📝 Enter Text")
text = st.text_area("Enter English text:", height=140, placeholder="Type something like: Hello, how are you?")

# --- Language Selection ---
st.markdown("### 🌍 Select Language")
lang = st.selectbox("Target language:", languages)

# --- Translate Button ---
btn = st.button("🔁 Translate")

# --- Translation Output ---
if btn and text:
    try:
        with st.spinner("Translating... Please wait..."):
            prompt = f"Translate the following text to {lang}:\n\n{text}"
            response = model.generate_content(prompt)

        st.markdown("### ✅ Translation")
        st.success(f"Translated to **{lang}**:")
        st.markdown(
            f"<div style='font-size:20px; color:#1a1a1a; padding:10px; background-color:#eaf4ff; border-left: 4px solid #1f77b4; border-radius:4px'>{response.text}</div>",
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error(f"❌ Translation Error: {str(e)}")
