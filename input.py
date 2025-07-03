from database import save_info, print_db 
from linkedin_client import get_jobs
from pdf_generator import generate_pdf
from genai_client import generate_tailored_resume
import re 
import time 


programName = "Resumaid"
# THINGS TO ADD: 
        # turn getting all inputs w database into one command
    # need to add in 'DATABASE' command, can access whenever, 
    # and then continues off where you left it 

    # there could be a more efficient way of getting the data (name, exp, etc.)
    # 
def print_database():
    print("Accessing database...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")

    # TODO: get list from database 
    print_db()

def empty_input(info):
    while len(info) == 0: 
        print("Don't leave this portion blank! (ง •̀_•́)ง")
        info = input("> ").strip()
    return info 

def valid_email(email):
    email_regex = r'^[A-Za-z0-9_.]+@[a-z]+\.(com|org|net)$'
    while not re.match(email_regex, email): 
        print("Invalid email. (ง •̀_•́)ง Put in another one!")
        email = input("> ").strip()
    return email 

def get_input(prompt):
    while True:
        print(prompt)
        user_input = input("> ").strip()

        if user_input == "DATABASE":
            print_database()
            continue

        if prompt != "If applying to a specific company, insert its name; otherwise leave blank: ":
            user_input = empty_input(user_input)

        if prompt == "Insert email: ":
            user_input = valid_email(user_input)
        
        return user_input

def collect_data(): 

    dbCommand = "DATABASE"

    # display welcome message + user instructions 
    print(f"Hello! Welcome to {programName}! Answer the following questions to create your resume and cover letter.")
    print(f"If you want to access previous resumes/cover letters created, type in {dbCommand}")

    # collecting user data via input 
    name = get_input("Insert name: ")
    email = get_input("Insert email: ")
    position = get_input("Insert position that you're applying for: ")
    company = get_input("If applying to a specific company, insert its name; otherwise leave blank: ")
    about = get_input("Paste your LinkedIn 'About Me': ")
    exp = get_input("Paste your Linkedin 'Experience': ")

    user_data = {
        "position": position,
        "company": company,
        "name": name,
        "email": email,
        # info for cover letter, created w Google GenAI 
        "about": about,  
        # info for pdfMonkey resume 
        "exp": exp
    }

    return user_data

if __name__ == "__main__":
    loop = True 
    while loop: 
        # dict, organized new user data 
        dataList = collect_data() 
        resume, cover_letter = generate_tailored_resume(dataList["about"], dataList["exp"], dataList["position"], dataList["company"])
        
        
        print("Your data was saved successfully.")

        # print out link to resume pdf and cover letter 
        print("Creating your resume and cover letter...")
        print("...")
        time.sleep(1)

        #resume + cover letter PDFMonkey Link 
        generate_pdf(dataList, resume, cover_letter)

        print("Here is a list of jobs you can apply to!")
        try: 
            jobs = get_jobs(dataList['position'], dataList['company'])

        print("Would you like to save this resume + cover letter in the database? Y/N")
        saveCreation = input("> ").strip()
        if saveCreation == "Y":
            save_info(dataList) #replace dataList with resume and coverletter 

        # prompting for the user to create more  
        # create loop if does not fit in Y/N 
        print("Would you like to create another resume/letter? Y/N")
        ans = input("> ").strip()
        loop = False if ans == "N" else True 
    
    print(f"Thank you for using {programName}!!")
    print("We wish you success in your job search.")



