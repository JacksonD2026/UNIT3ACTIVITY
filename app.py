from flask import Flask
from flask import render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app route decorator to map the URL  

@app.route("/")
def index():
       
        
        return render_template("index.html")    


@app.route("/submit", methods=['POST'])
def submit():
        form_data = {
                'middle_name': request.form.get('middle_name'),
        }

        return render_template("results.html", form_data=form_data)

if __name__ == '__main__':
        
        app.run(host='0.0.0.0', port=5000, debug=True)
