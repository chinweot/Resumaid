import re 

# THINGS TO ADD: 
        # turn getting all inputs w database into one command
    # need to add in 'DATABASE' command, can access whenever, 
    # and then continues off where you left it 

    # there could be a more efficient way of getting the data (name, exp, etc.)
    # 
def print_database():
    print("Accessing database...")
    time.sleep(1)


def empty_input(info):
    while len(info) == 0: 
        print("Don't leave this portion blank! (ง •̀_•́)ง")
        info = input("> ").strip()

def valid_email(email):
    email_regex = r'^[A-Za-z0-9_.]+@[a-z]+\.(com|org|net)$'
    while not re.match(email_regex, email): 
        print("Invalid email. (ง •̀_•́)ง Put in another one!")
        email = input("> ").strip()

def collect_data(): 
    programName = "[name]"
    dbCommand = "DATABASE"

    # display welcome message + user instructions 
    print(f"Hello! Welcome to {programName}! Answer the following questions to create your resume and cover letter.")
    print(f"If you want to access previous resumes/cover letters created, type in {dbCommand}")

    # collecting user data via input 
    print("Insert name: ")
    name = input("> ").strip()
    empty_input(name)

    print("Insert email: ")
    email = input("> ").strip()
    empty_input(email)
    valid_email(email)

    print("Insert position that you're applying for: ")
    position = input("> ").strip()
    empty_input(position)

    print("If applying to a specific company, insert its name; otherwise leave blank: ")
    company = input("> ").strip()
    empty_input(company)

    print("Paste your LinkedIn 'About Me': ")
    about = input("> ").strip()
    empty_input(about)

    print("Paste your Linkedin 'Experience': ")
    exp = input("> ").strip()
    empty_input(exp)

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

        # print out link to resume pdf and cover letter 


        # prompting for the user to create more  
        print("Would you like to create another resume/letter? Y/N")
        ans = input("> ").strip()
        loop = False if ans == "N" else True 
    
    print(f"Thank you for using {programName}!!")
    print("We wish you success in your job search.")



