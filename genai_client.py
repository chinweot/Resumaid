import os
import google.generativeai as genai
from input_cli import collect_data
from dotenv import load_dotenv
from pdf_generator import generate_pdf

"""
Generates both resume and cover letter content from LinkedIn input.
Return dictionary with resume and cover_letter keys.
"""

load_dotenv()
my_api_key = os.getenv("GENAIAPI_KEY") or os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=my_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_tailored_resume(about, experience, position, company):
    prompt = f"""
You are a resume and cover letter expert.

Create a professional resume and cover letter for someone applying to the position of {position} at {company}.

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


if __name__ == "__main__":
    data = collect_data()

    resume, cover_letter = generate_tailored_resume(
        about=data["about"],
        experience=data["exp"],
        position=data["position"],
        company=data["company"],
    )

    pdf_data = {
        "name": data["name"],
        "email": data["email"],
        "position": data["position"],
        "company": data["company"],
        "resume": resume,
        "cover_letter": cover_letter
    }

    generate_pdf(pdf_data)

    """
    print("\nTailored Resume:\n")
    print(resume)

    print("\nTailored Cover Letter:\n")
    print(cover_letter)
    """
