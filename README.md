# 🧠 AI Tutor — Interactive Educational Web App

**AI Tutor** is an educational web application demonstrating the power of **AI-assisted learning**. Users paste code, problems, or any text content and receive **instant, step-by-step explanations** powered by Google’s **Gemini AI model**. The app simplifies complex topics into clear, structured, and easy-to-understand explanations — deployed on **Google Cloud Run**.

---

## 🌐 Live Project

**Try it out:**

[https://ai-interactive-dashboard-834196002468.asia-south1.run.app](https://ai-interactive-dashboard-834196002468.asia-south1.run.app)

---

## 🚀 Features

* 🧩 **AI-Powered Explanations** — Input text, code, or concepts; receive beginner-friendly, step-by-step explanations via Google AI Studio (Gemini API).
* 💬 **Interactive Learning Interface** — Clean, responsive UI for text and optional image analysis.
* 📸 **AI Image Understanding (optional)** — Upload images (handwritten notes, diagrams) for automatic description or summarization.
* ☁️ **Serverless Deployment** — Hosted on **Google Cloud Run** for easy scalability and reliability.
* 📊 **Cloud Logging (Optional)** — User actions/queries can be persisted to **Google Cloud Storage** for analytics.

---

## 🧰 Tech Stack

| Component              | Technology Used                             |
| ---------------------- | ------------------------------------------- |
| **Frontend**           | HTML, CSS, JavaScript                       |
| **Backend**            | Python (Flask / FastAPI) or Node.js         |
| **AI Model**           | Google Gemini (via AI Studio / Gemini API)  |
| **Deployment**         | Google Cloud Run                            |
| **Cloud Integrations** | Google Cloud Storage (logging / image data) |
| **Version Control**    | GitHub                                      |
| **License**            | MIT License                                 |

---

## 📁 Repository Structure

```
app.py
index.html
.env.example
requirements.txt
README.md
LICENSE
```

---

## 🧩 AI Studio Prompt (Used in Development)

**Prompt example:**

> Explain the following code step-by-step for a beginner. Highlight the main logic and key functions.

AI Studio (Gemini) was used to generate backend logic snippets, refine prompt templates, and shape the explanation flow before integration with the Cloud Run service.

---

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/<your-username>/ai-tutor.git
cd ai-tutor

2️⃣ Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # Mac/Linux
venv\Scripts\activate       # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set up your environment variables

Create a file named .env and add:

GOOGLE_API_KEY=your_gemini_api_key
GCS_BUCKET_NAME=your_bucket_name
FLASK_SECRET=your_secret_key

5️⃣ Run locally
python app.py


Access it locally at: http://127.0.0.1:5000

☁️ Deploying to Google Cloud Run

1️⃣ Enable Cloud Run and Cloud Build APIs in Google Cloud Console.

2️⃣ Authenticate with your Google account:

gcloud auth login


3️⃣ Build and deploy:

gcloud run deploy ai-tutor \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated


Your app will be hosted at a link like:

https://ai-tutor-xxxxxx.asia-south1.run.app
## ☁️ Deploy (High-level — Google Cloud Run)

1. Build container (Google Cloud Build / Docker)
2. Push to Google Container Registry or Artifact Registry
3. Deploy to Cloud Run, attach service account with required permissions
4. (Optional) Configure Cloud Storage bucket for logs and image assets

---

## 🔭 Future Improvements

* Real-time student progress tracking
* Integrate Firestore to save session history & user profiles
* Use BigQuery for learning-pattern analytics
* Add a quiz & feedback generator module

---

## 📄 License

This project is created for hackathon demonstration purposes and is released under the **MIT License**.

---

## ✉️ Contact

For questions or contributions, contact me through mail monishwar26413@gmail.com.
