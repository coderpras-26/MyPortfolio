+   # Portfolio Website

A minimalist portfolio website capable of answering questions about the portfolio owner using an AI assistant. Built with Flask and Groq.

## Features

- **Resume Interaction**: Chat with an AI assistant that knows the details of the resume.
- **Minimalist Design**: Clean and responsive UI.
- **Resume Download**: Link to download the full resume PDF.

## Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd portfolio2
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    - Create a `.env` file in the root directory.
    - Add your Groq API key:
      ```
      GROQ_API_KEY=your_groq_api_key_here
      ```

5.  **Run the application:**
    ```bash
    python app.py
    ```
    The app will be available at `http://127.0.0.1:5000`.

## Deployment on Render

1.  Create a new Web Service on Render.
2.  Connect your repository.
3.  Set the **Build Command** to:
    ```bash
    pip install -r requirements.txt
    ```
4.  Set the **Start Command** to:
    ```bash
    gunicorn app:app
    ```
5.  Add the `GROQ_API_KEY` in the **Environment Variables** section of your Render dashboard.
