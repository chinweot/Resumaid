import os
import google.generativeai as genai
from dotenv import load_dotenv
from pdf_generator import generate_pdf

"""
Generates both resume and cover letter content from LinkedIn input.
Return dictionary with resume and cover_letter keys.
"""

load_dotenv()
#my_api_key = os.getenv("GENAIAPI_KEY") or os.getenv("GOOGLE_API_KEY")
my_api_key= "AIzaSyCR-qlyruPuiR5X0Aj6zfM8RwbNSXkvOqw"
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_tailored_resume(about, experience, position, company):
    prompt = f"""
You are a resume and cover letter expert.

Create a professional resume and cover letter for someone applying to the position of {position} at {company}.
We have already created a HTML/CSS template for you for contact information. 
Therefore, you do not need to include their name/contact information at the top. It is already provided.  

Use the following inputs:
- LinkedIn "About Me": {about}
- LinkedIn Work Experience: {experience}

Instructions:
- Optimize resume bullet points to highlight 
most relevant skills, keywords, and experiences.
- Keep bullet points concise, results-driven, and in standard resume format (no labels like "customer focus").
- Avoid repeated phrasing.

Format the output like this:

Resume:
<resume content>

Cover Letter:
<cover letter content>
"""
    response = model.generate_content(prompt)
    text = response.text

    parts = text.split("Cover Letter:", 1)
    resume = parts[0].replace("Resume:", "").strip()
    cover_letter = parts[1].strip() if len(parts) > 1 else "Cover letter not generated."

    return resume, cover_letter

