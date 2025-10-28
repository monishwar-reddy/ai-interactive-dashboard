# 🧠 AI Tutor — Interactive Educational Web App

**AI Tutor** is an educational web application designed to demonstrate the power of **AI-assisted learning**.  
Users can paste code, problems, or any text content and receive **instant, step-by-step explanations** powered by Google’s **Gemini AI model**.  
The system simplifies complex topics into clear, structured, and easy-to-understand insights — all deployed seamlessly on **Google Cloud Run**.

---
🌐 Live Project Link
🔗 Try it Out:
https://ai-interactive-dashboard-834196002468.asia-south1.run.app

## 🚀 Features

- 🧩 **AI-Powered Explanations**  
  Users can input text, code, or concepts, and the system generates meaningful explanations using Google AI Studio (Gemini API).

- 💬 **Interactive Learning Interface**  
  Clean, minimal, and responsive UI for both text and image analysis.

- 📸 **AI Image Understanding (optional)**  
  Upload images (like handwritten notes or diagrams) for AI-based description or summarization.

- ☁️ **Serverless Deployment**  
  Fully deployed using **Google Cloud Run**, ensuring scalability, reliability, and cost-efficiency.

- 📊 **Cloud Logging (Optional Integration)**  
  User actions or queries can be logged into **Google Cloud Storage** for analysis and insights.

---

## 🧰 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask / FastAPI) or Node.js |
| **AI Model** | Google Gemini (via AI Studio) |
| **Deployment** | Google Cloud Run |
| **Cloud Integrations** | Cloud Storage (for logging / image data) |
| **Version Control** | GitHub |
| **License** | MIT License |

---

## 🏗️ Architecture Diagram

```plaintext
┌────────────────────────────┐
│         User UI            │
│  (Browser: HTML + JS)      │
└─────────────┬──────────────┘
              │ Input (text/image)
              ▼
┌────────────────────────────┐
│     Backend API Server     │
│ (Flask / Node.js on Cloud  │
│          Run)              │
└─────────────┬──────────────┘
              │ Calls Gemini API
              ▼
┌────────────────────────────┐
│   Google AI Studio (Gemini)│
│ Generates explanations or  │
│     content summaries      │
└─────────────┬──────────────┘
              │ (Optional)
              ▼
┌────────────────────────────┐
│ Google Cloud Storage Bucket│
│  Logs user data or images  │
└────────────────────────────┘

##🧩 AI Studio Prompt (Used in Development)
Prompt Example:

"Explain the following code step-by-step for a beginner. Highlight the main logic and key functions."

AI Studio was used to generate the backend logic, refine prompt templates, and help structure explanations before integration into the deployed Cloud Run app.

##🧩 Repository Structure
app.py
index.html
.env.example
requirements.txt
README.md
LICENSE

##🧠 Future Improvements
Add real-time student progress tracking

Integrate Firestore for saving session history

Use BigQuery for learning pattern analytics

Add a quiz and feedback generator module
📄 License
This project is created for hackathon demonstration purposes.

