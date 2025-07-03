from dotenv import load_dotenv
import os
import requests

load_dotenv()

#PDFMONKEY_API_KEY = os.getenv("PDFMONKEY_API_KEY")
#PDFMONKEY_TEMPLATE_ID = os.getenv("PDFMONKEY_TEMPLATE_ID")

PDFMONKEY_API_KEY = "key"
PDFMONKEY_TEMPLATE_ID = "key-key-key-key-key"

def generate_pdf(data, resume, cover_letter):
    url = "https://api.pdfmonkey.io/api/v1/documents"
    headers = {
        "Authorization": f"Bearer {PDFMONKEY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "document": {
            "document_template_id": PDFMONKEY_TEMPLATE_ID,
            "payload": {
                "name": data["name"],
                "email": data["email"],
                "position": data["position"],
                "company": data["company"],
                "resume": resume,
                "cover_letter": cover_letter
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        json_resp = response.json()
        document = json_resp.get("data") or json_resp.get("document")
        if document:
            doc_id = document.get("id", "unknown")
            preview_url = document.get("preview_url", "N/A")
            print("PDF is being generated.")
            print("Document ID:", doc_id)
            print("Preview URL:", preview_url)
        else:
            print("Document data missing. Response:", json_resp)
    else:
        print("Failed to generate PDF:", response.status_code)
        print("Response content:", response.json())

"""
if __name__ == "__main__":
    test_data = {
        "name": "Jane Doe",
        "email": "jane@example.com",
        "position": "Product Designer",
        "company": "Figma",
        "resume": "Jane’s resume content goes here...",
        "cover_letter": "Jane’s cover letter goes here..."
    }
    generate_pdf(test_data)
"""