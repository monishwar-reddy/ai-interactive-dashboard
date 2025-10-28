# app.py
from flask import Flask, render_template, request, jsonify, session
import google.generativeai as genai
import os
from dotenv import load_dotenv
import uuid
from datetime import datetime
import json

# NEW IMPORT
from google.cloud import storage  

# -----------------------
# Initial Setup
# -----------------------
load_dotenv()
app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.getenv("FLASK_SECRET", str(uuid.uuid4()))

# Configure API key (put GOOGLE_API_KEY=value in .env)
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    raise RuntimeError("Put GOOGLE_API_KEY in .env")
genai.configure(api_key=API_KEY)

MODEL_NAME = "models/gemini-2.5-flash"

# -----------------------
# Google Cloud Storage Setup
# -----------------------
storage_client = storage.Client()
bucket_name = "ai-interactive-dashboard-data"  # replace with your bucket name

def log_to_gcs(user_input, model_output, endpoint):
    """Logs input/output to GCS as JSON for transparency and hackathon bonus."""
    try:
        bucket = storage_client.bucket(bucket_name)
        blob_name = f"logs/{endpoint}_{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
        blob = bucket.blob(blob_name)
        
        data = {
            "timestamp": datetime.now().isoformat(),
            "endpoint": endpoint,
            "input": user_input,
            "output": model_output
        }
        blob.upload_from_string(json.dumps(data, indent=2), content_type="application/json")
        print(f"✅ Logged interaction to {blob_name}")
    except Exception as e:
        print(f"⚠️ Logging to GCS failed: {e}")

# -----------------------
# AI Model Helper
# -----------------------
def model_generate(prompt_contents):
    model = genai.GenerativeModel(MODEL_NAME)
    return model.generate_content(prompt_contents)

@app.route("/")
def index():
    return render_template("index.html")

# -----------------------
# Chat API
# -----------------------
@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json() or {}
    user_text = data.get("text", "").strip()
    if not user_text:
        return jsonify({"ok": False, "error": "Empty input"}), 400

    convo = session.get("convo", [])
    convo.append({"role": "user", "text": user_text})

    system_preamble = (
        "You are an expert, concise and clear AI Study Buddy. Provide structured answers with headings, "
        "bullet lists where useful, and a short summary at the end. If user asks follow-up, keep context."
    )

    prompt_list = [system_preamble]
    for t in convo[-10:]:
        role = "User" if t["role"] == "user" else "Assistant"
        prompt_list.append(f"{role}: {t['text']}")
    prompt_list.append("Assistant:")

    try:
        resp = model_generate(prompt_list)
        text = resp.text if hasattr(resp, "text") else str(resp)
        log_to_gcs(user_text, text, endpoint="chat")  # <-- Log interaction
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

    convo.append({"role": "assistant", "text": text})
    session["convo"] = convo
    return jsonify({"ok": True, "reply": text})

@app.route("/api/clear", methods=["POST"])
def api_clear():
    session["convo"] = []
    return jsonify({"ok": True})

# -----------------------
# Grammar Correction API
# -----------------------
@app.route("/api/correct", methods=["POST"])
def api_correct():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"ok": False, "error": "Empty input"}), 400

    prompt = (
        "Correct grammar, spelling, punctuation, and improve clarity of the following text. "
        "Return only the corrected version, and after that provide a one-line summary labeled 'Summary:'.\n\n"
        f"Text: {text}"
    )
    try:
        resp = model_generate(prompt)
        log_to_gcs(text, resp.text, endpoint="correct")  # <-- Log correction
        return jsonify({"ok": True, "corrected": resp.text})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

# -----------------------
# Summarization API
# -----------------------
@app.route("/api/summarize", methods=["POST"])
def api_summarize():
    data = request.get_json() or {}
    text = data.get("text", "").strip()
    if not text:
        return jsonify({"ok": False, "error": "Empty input"}), 400

    prompt = [
        "Summarize the following text at three lengths: (1) one-sentence summary, (2) short paragraph (3-4 lines), (3) key bullet points (3 bullets). Label each section.",
        f"Text: {text}"
    ]
    try:
        resp = model_generate(prompt)
        log_to_gcs(text, resp.text, endpoint="summarize")  # <-- Log summary
        return jsonify({"ok": True, "summary": resp.text})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

# -----------------------
# Image Insight API
# -----------------------
@app.route("/api/image", methods=["POST"])
def api_image():
    try:
        image_file = request.files.get("image")
        if not image_file:
            return jsonify({"ok": False, "error": "no file uploaded"}), 400

        tmp_path = "upload_tmp.jpg"
        image_file.save(tmp_path)
        with open(tmp_path, "rb") as f:
            img_bytes = f.read()

        prompt = [
            "Analyze this image deeply and return a structured report with sections: Description, Objects Detected (list), Visual Cues (lighting, colors, mood), Insights (interpretation, possible context), Possible Applications.",
            {"mime_type": "image/jpeg", "data": img_bytes}
        ]
        resp = model_generate(prompt)
        log_to_gcs("image uploaded", resp.text, endpoint="image")  # <-- Log image analysis
        return jsonify({"ok": True, "result": resp.text})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

# -----------------------
# List Models API
# -----------------------
@app.route("/api/models", methods=["GET"])
def api_models():
    try:
        models = genai.list_models()
        names = [m.name for m in models]
        return jsonify({"ok": True, "models": names})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
