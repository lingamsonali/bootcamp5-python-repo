from flask import Flask, render_template

# AWS EB looks for 'application' variable by default
application = Flask(__name__)
app = application 

@app.route("/")
def home():
    # Flask automatically looks inside the /templates folder
    return render_template("index.html")

if __name__ == "__main__":
    application.run(debug=True)