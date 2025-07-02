
def collect_data(): 
    programName = ""
    dbCommand = "DATABASE"

    # display welcome message + user instructions 
    print(f"Hello! Welcome to {programName}! Answer the following questions to create your resume and cover letter.")
    print(f"If you want to access previous resumes/cover letters created, type in {dbCommand}")

    # collecting user data via input 
    print("Insert name: ")
    name = input("> ").strip()

    print("Insert email: ")
    email = input("> ").strip()

    print("Insert position that you're applying for: ")
    position = input("> ").strip()

    print("If applying to a specific company, insert its name; otherwise leave blank: ")
    company = input("> ").strip()

    print("Paste your LinkedIn 'About Me': ")
    about = input("> ").strip()

    print("Paste your Linkedin 'Experience': ")
    exp = input("> ").strip()

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
    dataList = collect_data() # dict DS 

