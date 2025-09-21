
# app.py

import os
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # This enables Cross-Origin Resource Sharing

# Configure the generative AI model
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
except Exception as e:
    print(f"Error configuring Generative AI: {e}")
    model = None

# This is the detailed instruction for our AI chatbot
SYSTEM_PROMPT = """
You are 'Sahara,' a supportive and empathetic mental wellness chatbot for young adults in India.
Your tone is always calm, non-judgmental, gentle, and reassuring.
You MUST NOT give medical advice or act as a therapist.
Your primary goals are:
1.  Listen actively to the user's concerns and validate their feelings.
2.  Gently guide them to reflect on their thoughts and feelings.
3.  Provide simple, actionable, and safe wellness techniques (e.g., breathing exercises, grounding techniques).
4.  If the user mentions serious distress, self-harm, or severe issues, you must gently guide them to seek professional help and provide reliable Indian helpline resources.
5.  Maintain a culturally sensitive and understanding perspective relevant to Indian youth.

Do not use overly complex or clinical language. Keep your responses concise, warm, and easy to understand.
"""

@app.route('/chat', methods=['POST'])
def chat():
    if model is None:
        return jsonify({"error": "Generative AI model not configured"}), 500

    data = request.get_json()
    user_message = data.get('message')

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Combine the system prompt with the user's message for context
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_message}\nSahara:"
        
        response = model.generate_content(
            full_prompt,
            generation_config=genai.types.GenerationConfig(
                # Controls randomness. Lower is less random.
                temperature=0.7,
            )
        )
        
        ai_response = response.text
        
        # A simple check for providing helpline info
        keywords = ['help me', 'so sad', 'depressed', 'anxious', 'scared']
        if any(keyword in user_message.lower() for keyword in keywords):
            helpline_info = (
                "\n\n*It's brave to talk about these feelings. If you feel you need to speak with someone, "
                "reaching out to a professional can be a really helpful step. You can connect with Vandrevala Foundation at +91 9999666555.*"
            )
            ai_response += helpline_info

        return jsonify({"reply": ai_response})

    except Exception as e:
        print(f"Error during AI generation: {e}")
        return jsonify({"error": "Failed to generate AI response"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
