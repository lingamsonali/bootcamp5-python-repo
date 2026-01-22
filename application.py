from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Hello from Flask on Elastic Beanstalk"
