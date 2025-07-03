# Resumaid Paired Project

Resumaid is a command-line tool that helps job seekers generate tailored resumes and cover letters using their LinkedIn profile content. It utilizes AI and the user's job data to streamline the job application process

---

## Features

- Uses Google GenAI (Gemini 1.5 Flash) to generate professional resume and cover letter content  
- Recommends live job openings using the LinkedIn Jobs API  
- Converts content into downloadable PDF resumes using PDFMonkey  
- Saves user input and generated files to a local SQLite database  
- Lets users view and reuse previous application history  

---

## Technologies & APIs Used

- Python 3.10+  
- SQLite (via SQLAlchemy)  
- Google Generative AI SDK – for resume and cover letter generation  
- LinkedIn Jobs API – to fetch job postings  
- PDFMonkey API – to create professional PDF documents  
- pandas, requests, dotenv – for data processing and configuration  

---

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/resumaid.git
    cd resumaid
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the project root and add your API keys:

    ```env
    GENAIAPI_KEY=your_google_genai_key
    PDFMONKEY_API_KEY=your_pdfmonkey_key
    PDFMONKEY_TEMPLATE_ID=your_template_id
    ```

---

## Usage

Run the app:

```bash
python main.py
```

## Follow Prompts to: 
- Enter Linkedin "About me" and "Experience"
- Provide the job position and company
- Generate a custom resume and cover letter
- View recommended jobs from LinkedIn Jobs API
- Save and download your resume as a PDF
- Type DATABASE when prompted to view saved entries

## Database Schema 
SQLite stores:
- User info (name, email)
- LinkedIn text inputs (About Me, Experience)
- Generated resume and cover letter
- Recommended jobs
- Application history and time taken 

# Contributions
- Annie Nyugen
- Chichi Otti
