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
                'name': request.form.get('name'),
                'age': request.form.get('age'),
                'hobby': request.form.get('favorite_hobby'),
                'color': request.form.get('favorite_color'),
                'lucky': request.form.get('lucky_number')
        }

        return render_template("results.html", form_data=form_data)

if __name__ == '__main__':
        
        app.run(host='0.0.0.0', port=5000, debug=True)
