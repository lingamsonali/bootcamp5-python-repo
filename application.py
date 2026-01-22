from flask import Flask

application = Flask(__name__)  # <-- Must be named 'application'

@application.route("/")
def home():
    return "Hello from Flask on Elastic Beanstalk!"

if __name__ == "__main__":
    # For local development only
    application.run(host="0.0.0.0", port=8080, debug=True)
