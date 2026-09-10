from flask import Flask
from routes.university import university_bp

app = Flask(__name__)

# Secret key for flash messages
app.secret_key = "sahyogsetu-secret-key"

# Register University Module
app.register_blueprint(university_bp)


@app.route("/")
def home():
    return "SahyogSetu is running!"


if __name__ == "__main__":
    app.run(debug=True)