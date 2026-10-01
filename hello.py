from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello World!</h1>"

# Example 2-2: Added a dynamic route to say hello to a custom username string
@app.route("/user/<name>")
def user(name):
  return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
  app.run(debug=True)
