from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World!'
@app.route("/index")
def index():
    return 'index'
@app.route("/hello")
def helloworld():
    return 'Hello World!'
@app.route("/user/paul")
def userpaul():
    return 'user paul'
@app.route("/post/80")
def post80():
    return 'post 80'

if __name__ == "__main__":
	app.run(host='0.0.0.0',	port=8080,debug=True)	
