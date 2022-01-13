from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello(name):
    print(name)
    return 'Hi, ' + str(name)

@app.route('/repeat/<num>/<word>')
def repeater(num, word):
    print((str(word) + '\n') * int(num))
    return ((str(word) + '\n') * int(num))
#this is no different than return word * int(num)

@app.route('/<other>')
def no_response(other):
    if other != dojo or repeater:
        print('Sorry! No response. Try again.')
        return 'Sorry! No response. Try again'

if __name__ == '__main__':
    app.run(debug=True)