# 1. Import Flask
from flask import Flask, jsonify

# 2. Create an app
app = Flask(__name__)

# 3. Define index route
@app.route("/")
def home():
    return "Hello, Web"


# 4. Define the about route
@app.route("/about")
def normal():
    return str('Opy' 'flask' 'Austin')


# 5. Define the contact route
@app.route("/contact")
def jsonified_list():
    return jsonify(ope@yahoo.me)


# 6. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
