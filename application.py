from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)

# Health check route for ALB
@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

# Main route
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 80))  # Use PORT from EB env or default 80
    app.run(host="0.0.0.0", port=port)

