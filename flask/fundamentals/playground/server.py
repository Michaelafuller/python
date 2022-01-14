
from flask import Flask, render_template  
app = Flask(__name__)                     
    
@app.route('/play')                           
def index():
    return render_template('index.html', num=3, color="blue")  

@app.route('/play/<int:num>')
def box_multiplier(num):
    return render_template('index.html', num=num, color ="blue")


@app.route('/play/<int:num>/<string:color>')
def box_color_mult(num, color):
    return render_template('index.html', num=num, color=color)


