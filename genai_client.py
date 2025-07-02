import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv("GENAIAPI_KEY") or os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=my_api_key)

if not my_api_key:
    raise Exception("No API key found. Set GENAI_KEY or GOOGLE_API_KEY.")


model = genai.GenerativeModel("gemini-1.5-flash")

def generate_resume_text(linkedin_about, work_experience, position, company):
    prompt = f"""
    Create a professional resume for the position of {position} at {company}.
    Use this LinkedIn 'About Me' section:
    {linkedin_about}

    And the following work experience:
    {work_experience}

    Format it as clean professional resume content.
    """
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    sample_about = "I’m a product-focused software engineer who builds delightful AI tools."
    sample_experience = "Software Engineer at Google (2020–2023)\nIntern at Microsoft (2019)"
    text = generate_resume_text(sample_about, sample_experience, "AI Engineer", "OpenAI")
    print(text)

