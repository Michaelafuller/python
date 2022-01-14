from flask import Flask, render_template  
app = Flask(__name__)   

@app.route('/')
def index(num=4):
    return render_template('index.html', num=num)

@app.route('/<int:height>')
def board_height(height):
    return render_template('index.html', height=height)

@app.route('/<int:height>/<int:width>')
def multiplier(height, width):
        return render_template('index.html', height=height, width=width)


if __name__=="__main__":
    app.run(debug=True)                   