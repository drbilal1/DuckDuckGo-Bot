# Paste ALL your code here in order (imports first, then functions, then main app)
# Example:
from flask import Flask
import pandas as pd

def my_function():
    return "Hello World"

app = Flask(__name__)

@app.route('/')
def home():
    return my_function()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)