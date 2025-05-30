import streamlit as st # type: ignore
import requests
import os
from dotenv import load_dotenv # type: ignore

# Load environment variables (for local development)
load_dotenv()

# Try to get API key from environment or Streamlit secrets
API_KEY = os.getenv("OPENROUTER_API_KEY")

# OpenRouter API URL
OPENROUTER_CHAT_URL = "https://openrouter.ai/api/v1/chat/completions"

# ------------------------
# OpenRouter Chat Function
# ------------------------
def ask_openrouter(prompt):
    if not API_KEY:
        return "❌ Error: OPENROUTER_API_KEY is missing."

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json',
        'HTTP-Referer': 'http://localhost',
        'X-Title': 'solar-app'
    }

    body = {
        "model": "meta-llama/llama-3-70b-instruct",
        "messages": [
            {
                "role": "system",
                "content": "You are a solar energy expert. Provide ROI estimates and recommendations based on user input."
            },
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(OPENROUTER_CHAT_URL, headers=headers, json=body)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as http_err:
        return f"❌ HTTP error occurred: {http_err} - {response.text}"
    except Exception as e:
        return f"❌ Failed to get response from AI: {e}"

# ------------------------
# Streamlit App Interface
# ------------------------
def main():
    st.set_page_config(page_title="Solar ROI Estimator (AI)", layout="centered")
    st.title("🔆 Solar ROI Estimator (AI-Powered)")

    with st.form("solar_form"):
        st.subheader("🏠 Enter Rooftop Details")
        location = st.text_input("Location (City, Country)", "Pune, India")
        roof_area = st.number_input("Roof Area (sq ft)", min_value=50, max_value=10000, value=1000)
        electricity_rate_inr = st.number_input("Electricity Rate (INR/kWh)", min_value=1.0, value=8.0, step=0.5)
        budget_inr = st.number_input("Budget (INR)", min_value=10000, value=800000, step=5000)
        uploaded_file = st.file_uploader("Upload rooftop image (optional)", type=["png", "jpg", "jpeg"])
        submitted = st.form_submit_button("Estimate Solar ROI")

    if submitted:
        with st.spinner("🧠 Analyzing with AI..."):
            prompt = (
                f"I have a rooftop in {location} with {roof_area} sq ft area. "
                f"My electricity rate is ₹{electricity_rate_inr:.2f}/kWh and my budget is ₹{budget_inr:.2f}. "
                "Estimate how much solar I can install, the expected annual energy production, savings, and payback period. "
                "Also give me friendly advice if it's worth it or not."
            )
            if uploaded_file:
                prompt += " I have also uploaded an image of the rooftop for additional context."

            response = ask_openrouter(prompt)
            st.subheader("🤖 AI Response")
            st.write(response)

            if uploaded_file:
                st.subheader("📷 Rooftop Image")
                st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    st.markdown("---")
    st.caption("⚡ Powered by OpenRouter & Streamlit")

if __name__ == "__main__":
    main()
