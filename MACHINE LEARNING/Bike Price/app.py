from flask import Flask , url_for , request
app = Flask(__name__)
@app.route('/')
def home():
    return "HELLO WORLD "
@app.route('/bio')
def intro():
    return "Hello my name is mahipal "
if __name__=="__main__":
    app.run(debug=True)