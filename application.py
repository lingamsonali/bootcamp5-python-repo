from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return "Elastic Beanstalk Python App is running bootcampproject5!"

if __name__ == "__main__":
    application.run()
