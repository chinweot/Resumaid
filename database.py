import pandas as pd 
import sqlalchemy as db 
import json 

engine = db.create_engine('sqlite:///resumaid.db')

def init_db():
    with engine.connect() as connection:
        connection.execute(db.text("""
            CREATE TABLE IF NOT EXISTS resumes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pdf TEXT,
                jobs TEXT
            );
            """))

def save_info(data):
    df = pd.DataFrame.from_dict({k:[v] for k,v in data.items()})
    df.to_sql('resumes', con=engine, if_exists='append', index=False)

def print_db(): # printing all contents from database 
    with engine.connect() as connection: 
        result = connection.execute(db.text("SELECT * FROM resumes;")).fetchall()

    if result:
        columns = result[0]._fields if hasattr(result[0], '_fields') else ['pdf', 'jobs']
        df = pd.DataFrame(result, columns=columns)

        print("\n====DATABASE ENTRIES====")
        for index, row in df.iterrows():
            print(f"\nEntry #{index+1}")
            print('-' * 30)
            print(f"PDF Link:\n{row['pdf']}")
            print('\nJobs:')
            jobs_text = row['jobs']
            for job in jobs_text.split("at"):
                job = job.strip()
                if job:
                    print(f"- {job} at")

    else: 
        print("Database empty.")

init_db()