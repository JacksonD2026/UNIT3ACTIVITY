from flask import Flask
from flask import render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app route decorator to map the URL  

@app.route("/")
def index():
        name_data = 'Jackson'
        year_data = 2026
        favorites_list = ['Stardew Valley', 'The Sims', 'BG3', 'Pokemon']
        ratings_dict = {
                        'The Sims':'great',
                        'BG3':'good',
                        'Stardew Valley':'solid',
                        'Pokemon': 'okay',
        }
        return render_template("index.html", name=name_data, year=year_data, favorites=favorites_list, ratings=ratings_dict )    


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
