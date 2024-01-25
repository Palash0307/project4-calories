from flask import Flask,render_template,jsonify,request
from sqlalchemy import text

app =Flask(__name__)

# @ decorater /-path to be deployed(right now its a home page)
@app.route("/")
def hello():
    return render_template('home.html')


@app.route("/calories",methods=['GET','POST'])

# Store this in the database
# Display an acknowledgment, to show the template after receiving from application_form which is taken by request.form
        
def result(data):
    if request.method == 'POST':
        # Handling POST request
        data = request.form
        
        result(data)
        # Store this in the database
        # Display an acknowledgment, to show the template after receiving from application_form which is taken by request.form
        return render_template('result.html', result=data)
    elif request.method == 'GET':
        # Handling GET request
        
        return render_template('result.html', result=data)
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)