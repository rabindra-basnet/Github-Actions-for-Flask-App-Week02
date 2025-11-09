
from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello From CI/CD pipeline with github Actions! and Presidential"

if __name__ == "__main__":
    app.run("0.0.0.0",debug=True)
