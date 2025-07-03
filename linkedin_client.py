from urllib.parse import quote
import requests
import os

def get_jobs(position, company=None):
    API_KEY = ""
    job_str = ""

    title_filter = quote(f'"{position}"')
    location_filter = quote('"United States"')

    url = ( f"https://linkedin-job-search-api.p.rapidapi.com/active-jb-24h?limit=4&offset=0&title_filter={title_filter}&location_filter={location_filter}" )

    headers = {
        "x-rapidapi-host": "linkedin-job-search-api.p.rapidapi.com",
        "x-rapidapi-key": API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200: 
        jobs = response.json()
        if not jobs:
            print("No jobs avaliable...")
            return 
    
        print(f"Top 5 job listings for {position}")
        for idx, job in enumerate(jobs[:5], 1):
            print(f"{idx}. {job.get('title', 'N/A')} at {job.get('company_name', 'Unkown Company')}")
            job_str += job.get('title', 'N/A') + ' at ' + job.get('company_name', 'Unkown Company')
            print(f"Apply here: {job.get('job_url', 'N/A')}")
        return job_str
    else: 
        print("Failed to fetch jobs. Try again later.")
        print(f"Status code: {response.status_code}")
        print("response content: ", response.text)
    return ''
