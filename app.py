import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("🤖 GenAI Code Error Explainer")

error = st.text_area("Paste your error message:")

if st.button("Explain"):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Explain code errors in simple English."},
            {"role": "user", "content": error}
        ]
    )
    st.write(response.choices[0].message.content)
