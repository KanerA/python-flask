from flask import Flask
app = Flask(__name__)

x = 'hello'

@app.route('/')
def home():
    return "Home"



if __name__ == "__main__":
    app.run()

