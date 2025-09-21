# Sahara 💬

**A confidential and empathetic AI wellness companion for youth.**

Sahara is a prototype developed for the **Google Cloud Gen AI Exchange Hackathon 2025**. It's an AI-powered chatbot designed to provide a safe, anonymous, and non-judgmental space for young adults in India to discuss their mental health concerns.


## 🌟 About The Project

Mental health remains a significant taboo in India, creating a formidable barrier for students seeking support. Amidst intense academic and social pressures, young adults often lack a confidential outlet to address their concerns.

**Sahara** aims to be that first step. By leveraging the power of Google's Gemini API, it acts as an empathetic listener, helping to break the stigma and guiding users toward self-reflection and reliable resources.

## ✨ Key Features

- **Empathetic Conversational AI:** Provides supportive, human-like responses powered by the Gemini 1.0 Pro model.
- **Guided Journaling:** Asks gentle, reflective questions to help users explore and understand their feelings.
- **Curated Resource Hub:** Offers contextual links to verified wellness resources like breathing exercises and Indian mental health helplines.
- **Complete Anonymity:** No login or personal data is required, ensuring user privacy and trust.

## 🏗️ Project Architecture

The application operates on a simple and effective client-server model:

1.  **Frontend (Client):** A clean, calming web interface built with HTML, CSS, and JavaScript. It captures user input and displays the conversation.
2.  **Backend (Server):** A lightweight Python server built with Flask. It serves as a bridge between the frontend and the AI.
3.  **AI Core:** The backend communicates with the **Google Gemini API** to generate intelligent and empathetic responses.

## 🛠️ Tech Stack

- **AI & Cloud:** Google Cloud (Gemini 1.0 Pro API)
- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Python Libraries:** `google-generativeai`, `Flask-Cors`, `python-dotenv`

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- Python 3.8 or higher installed on your system.
- A Google Gemini API Key. You can get one from [Google AI Studio](https://aistudio.google.com/).

### Installation & Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/sahara.git](https://github.com/your-username/sahara.git)
    cd sahara
    ```

2.  **Create a `requirements.txt` file:**
    Create a new file named `requirements.txt` and add the following lines to it:
    ```
    Flask
    Flask-Cors
    google-generativeai
    python-dotenv
    ```

3.  **Install the required Python packages:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a new file in the root directory named `.env` and add your Gemini API key:
    ```
    GEMINI_API_KEY=YOUR_API_KEY_HERE
    ```

## 🏃‍♀️ Usage

This project requires two terminals to run concurrently: one for the backend and one for the frontend.

1.  **Start the Backend Server (Terminal 1):**
    Open your first terminal in the project directory and run:
    ```sh
    python app.py
    ```
    This will start the Flask server on `http://127.0.0.1:5000`.

2.  **Start the Frontend Server (Terminal 2):**
    Open a **second terminal** in the same project directory and run:
    ```sh
    python -m http.server 8000
    ```
    This will serve your `index.html` file on `http://localhost:8000`.

3.  **Open the Application:**
    Open your web browser and navigate to **`http://localhost:8000`**. You can now interact with the Sahara chatbot!

## 🗺️ Project Roadmap

-   [ ] **Phase 2: Refinement & User Feedback:**
    -   Improve the AI's conversational context memory.
    -   Conduct a private beta test with student volunteers to gather feedback.
-   [ ] **Phase 3: Feature Expansion:**
    -   Introduce mood tracking and guided breathing exercises.
    -   Partner with university wellness centers to expand the resource hub.
-   [ ] **Phase 4: Scaling & Launch:**
    -   Deploy as a lightweight Progressive Web App (PWA) for mobile access.
    -   Ensure backend scalability using Google Cloud Run.

## 🤝 Team

This project was built by **Team Tensor Troupe**.
- Vinitha Kurapati
- Manaswini Nimmakanti
