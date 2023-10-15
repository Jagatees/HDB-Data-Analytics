
# Importing Flask modules for web application development
from flask import Flask, render_template, request
# Importing custom web scraping functions from 'scripts.co' module


app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')



if __name__ == "__main__":
    app.run('127.0.0.1', 5012, debug=True)
