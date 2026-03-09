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

        favorite_hobby = request.form.get("favorite_hobby")
        favorite_color = request.form.get("favorite_color")
        favorite_game = request.form.get("favorite_game")
        favorite_food = request.form.get("favorite_food")
        
        # count points
        points = 0
        if(favorite_hobby == 'Videogames'):
                points += 1
        if(favorite_color == 'Olive_Green'):
                points += 1
        if(favorite_game == 'Terreria'):
                points += 1
        if(favorite_food == 'Burritos'):
                points += 1

        
        return render_template("results.html", points=points)


        
        



if __name__ == '__main__':
        
        app.run(host='0.0.0.0', port=5000, debug=True)


