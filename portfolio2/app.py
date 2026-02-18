import os
from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# Resume Data
resume_data = {
    "name": "Prasana Kumar Mohapatra",
    "title": "Student & Creative Professional",
    "contact": {
        "phone": "+91 63371147433",
        "email": "prasanakumarmohapatra393@gmail.com",
        "location": "India"
    },
    "education": [
        {
            "institution": "NIST University",
            "degree": "Bachelor of Technology",
            "year": "2024 - 2028"
        },
        {
            "institution": "K.C. Public School",
            "degree": "Higher Secondary (X, XI & XII)",
            "year": "Completed" 
        }
    ],
    "experience": [
        {
            "role": "Video Editor & Photographer",
            "skills": ["CapCut", "Lightroom", "Color Grading", "Video Enhancing"],
            "description": "Specialized in mobile videography and photography. Proficient in editing and enhancing visual content."
        }
    ],
    "skills": [
        "Time Management",
        "Communication",
        "Calendar Management",
        "Videography",
        "Cinematography",
        "Languages: Odia, Hindi, English, Spanish"
    ],
    "about": "Aspiring technologist and creative professional with a passion for videography and photography. Currently pursuing a B.Tech at NIST University while honing skills in visual storytelling and editing."
}

# Groq Client Initialization
# In a production environment, use environment variables!
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq Client Initialization
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set")
    
client = Groq(api_key=GROQ_API_KEY)

def get_system_prompt():
    """Generates the system prompt using resume data."""
    context = f"""
    You are an AI assistant for Prasana Kumar Mohapatra's portfolio website.
    Your goal is to answer questions about Prasana based strictly on his resume data provided below.
    Be professional, concise, and helpful. If the answer is not in the resume, state that you don't have that information but can provide contact details.
    
    Resume Data:
    Name: {resume_data['name']}
    Title: {resume_data['title']}
    Contact: {resume_data['contact']}
    About: {resume_data['about']}
    Education: {resume_data['education']}
    Experience: {resume_data['experience']}
    Skills: {resume_data['skills']}
    """
    return context

@app.route('/')
def index():
    return render_template('index.html', resume=resume_data)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": get_system_prompt()},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=150,
            top_p=1,
            stream=False,
            stop=None,
        )
        ai_response = completion.choices[0].message.content
        return jsonify({"response": ai_response})
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        return jsonify({"error": "Failed to generate response"}), 500

if __name__ == '__main__':
    app.run(debug=True)
