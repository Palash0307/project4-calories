from flask import request
from sqlalchemy import create_engine,text
import os
#added security to protect the password
db_connection_string = os.environ['db_connection'] #name to be added in environment 19thjan
engine = create_engine(db_connection_string,
                    connect_args={"ssl": { #to get from clouddb sources
                                            "ssl_ca":"/etc/ssl/cert.pem",
                                            
                                        }
                                    }
                                )


#to be used in job_item.html

#to execute a specific job details
# to be used in jobpage.html

       
        
        
        
def result(data):
    print(data)
    cursor = conn.cursor()
    
#going to retreive the data from our apply_to_job function in which the data object is taking our application inputs from application_submit which is linked to application_form
    with engine.connect() as conn:

        query = text("""
        INSERT INTO Applications (full_name, Age, weight, Calories,)
        VALUES ( :full_name, :Age, :weight, :Calories)
        """).bindparams(job_id=id,
                     full_name=request.form.get('full_name', ''),
                     Age=request.form.get('age', ''),
                     Height=request.form.get('height', ''),
                     Weight=request.form.get('weight', ''),
                     Calories=request.form.get('Calories', ''),
                     )
        conn.execute(query)

        cursor.execute("SELECT * FROM Result WHERE age = ? AND height = ? AND weight = ?  AND caloriest = ?",
                   (Age, Height, Weight,Calories))
        result = cursor.fetchall()
        return result
                     
        
        