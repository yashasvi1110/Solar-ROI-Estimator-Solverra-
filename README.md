# Solar-ROI-Estimator(Solverra)

An **AI-powered assistant** that estimates solar installation potential, savings, and return on investment based on user-provided rooftop details and optionally an image (for visual context only). This tool is designed for both homeowners and solar professionals in the Indian market. https://huggingface.co/spaces/llama-yash/Solverra

🚀 **Powered by OpenRouter API** and built with **Streamlit** for a user-friendly interface.

---

## 🛠 Features

* 🧠 **LLM-Based Solar Analysis**: Uses OpenRouter’s LLM to simulate system sizing, savings, and ROI.
* 🏠 **User-Friendly Inputs**: Enter location, roof area, electricity rate (INR), and budget (INR).
* 🖼 **Image Upload Support**: Users can optionally upload a rooftop image (not analyzed, used for context only).
* 🛡 **Secure Key Handling**: API key is stored via `.env` using `python-dotenv`.
* 🎨 **Streamlit Interface**: Interactive and responsive UI.

---

## 📌 Installation & Setup (Local Development)

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/Solar_AI_Assistant.git
   cd Solar_AI_Assistant
   ```
2. **Create & Activate Virtual Environment**

   ```bash
   python -m venv venv
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   source venv/bin/activate
   ```
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure API Key**

   * Create a `.env` file in the root directory:

     ```env
     OPENROUTER_API_KEY=your_openrouter_api_key_here
     ```
   * Don’t forget to add `.env` to `.gitignore`.
5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   * The app will open in your browser at `http://localhost:8501`

---

## 🔍 Example Usage

1. Enter your **location**, **roof area**, **electricity rate (INR/kWh)**, and **budget (INR)**.
2. Optionally, upload a rooftop image (just for visual context).
3. Click **Estimate Solar ROI**.
4. Read the AI-generated recommendations and projected ROI.

---

## 📄 Implementation Details

* **LLM Integration**: `ask_openrouter()` sends structured prompts to the OpenRouter API using the `meta-llama/llama-3-70b-instruct` model.
* **Secure Config**: API key is accessed via `dotenv` and `os.getenv()`.
* **Form Inputs**: Streamlit form captures location, area, and pricing data.
* **Optional Image Upload**: Image is displayed for user reference; not processed or analyzed.
* **Error Handling**: Graceful error messages for missing keys or API failures.

---

## 🔄 Future Improvements

* 🎯 Integrate Google Solar API for rooftop and irradiance analysis
* 📏 Use vision models like Segment Anything for image-based roof segmentation
* 🗺 Add geolocation mapping and tilt/orientation estimation
* 📊 Enable data export or report download
* 🌐 Add Hindi/Marathi UI support

---

## 🚀 Deployment Options

* **Hugging Face Spaces**

  1. Create a new space (Streamlit SDK)
  2. Upload `app.py`, `requirements.txt`
  3. Add API key in Secrets panel

* **Streamlit Community Cloud**

  1. Push to GitHub
  2. Connect repo in Streamlit Cloud dashboard
  3. Set OPENROUTER\_API\_KEY as a secret

* **Local ZIP Package**
  Include the following files:

  * `app.py`
  * `requirements.txt`
  * `.env.example`
  * `README.md`

---

✨ Empowering solar adoption through AI-driven insight ☀
