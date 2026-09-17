import warnings
warnings.filterwarnings("ignore")

import os
from google import genai

def translate_and_adjust_tone(text, target_language, tone):

    API_KEY = "INSERT_GEMINI_API_KEY" 
    
    client = genai.Client(api_key=API_KEY)

    prompt = (
        f"Translate the following text into {target_language}.\n"
        f"Adjust the tone to be {tone}.\n"
        f"Provide ONLY the translated result without preamble or extra commentary.\n\n"
        f"Text: \"{text}\""
    )

    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=prompt,
        )
        return response.text.strip()
    except Exception as e:
        return f"Error connecting to AI API: {e}"

def main():
    print("=== AI Language & Tone Translator ===")
    
    text = input("\nEnter text to translate: ").strip()
    target_lang = input("Target language (e.g., Spanish, Japanese, Tagalog): ").strip()
    tone = input("Desired tone (e.g., Formal Business, Casual, Academic, Professional): ").strip()

    if not text or not target_lang:
        print("Text and Target Language cannot be empty.")
        return

    if not tone:
        tone = "Natural and Neutral"

    print("\nTranslating with AI...\n")
    translated_result = translate_and_adjust_tone(text, target_lang, tone)
    
    print("--- Result ---")
    print(translated_result)

if __name__ == "__main__":
    main()
