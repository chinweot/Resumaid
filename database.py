import pandas as pd 
import sqlalchemy as db 

engine = db.create_engine('sqlite:///resumaid.db')

def save_info(data):
    # change this to created resumes
    df = pd.DataFrame.from_dict({k: [v] for k,v in data.items()})
    df.to_sql('resumes', con=engine, if_exists='append', index=False)

def print_db(): # printing all contents from database 
    with engine.connect() as connection: 
        result = connection.execute(db.text("SELECT * FROM resumes;")).fetchall()
    if result:
        columns = result[0]._fields if hasattr(result[0], '_fields') else list(data.keys())
        print(pd.DataFrame(result, columns=columns))
    else: 
        print("Database empty.")