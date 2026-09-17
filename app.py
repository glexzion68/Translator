import streamlit as st
from google import genai

st.set_page_config(page_title="AI Translator", page_icon="🌐")
st.title("🌐 AI Language & Tone Translator")

API_KEY = "INSERT_GEMINI_API_KEY"  
client = genai.Client(api_key=API_KEY)

text = st.text_area("Enter text to translate:", placeholder="Type your text here...")

col1, col2 = st.columns(2)
with col1:
    target_lang = st.text_input("Target Language:", value="Spanish")
with col2:
    tone = st.text_input("Desired Tone:", value="Professional")

if st.button("Translate", type="primary"):
    if not text.strip():
        st.warning("Please enter text to translate.")
    else:
        prompt = (
            f"Translate the following text into {target_lang}.\n"
            f"Adjust the tone to be {tone}.\n"
            f"Provide ONLY the translated result without preamble.\n\n"
            f"Text: \"{text}\""
        )
        with st.spinner("Translating..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.1-flash-lite",
                    contents=prompt
                )
                st.success("Translation Complete!")
                st.text_area("Result:", value=response.text.strip(), height=120)
            except Exception as e:
                st.error(f"Error: {e}")