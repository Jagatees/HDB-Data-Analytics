import matplotlib

import scripts.main_page_scrapping 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
from flask import Flask, render_template,jsonify
from flask import request

app = Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    scripts.main_page_scrapping.main_scrapping()
    return render_template('index.html')
   
@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get_scrap', methods=['POST'])
def get_scrap():
	if request.method == 'POST':
		# this return the index of the array 
		selected_option = request.form['my_dropdown']
		selected_page = request.form['my_page']
		print(f'Selected option: {selected_page}') 
		if selected_option == '1':
			print("https://www.w3schools.com/html/default.asp")
		if selected_option == '2':
			print("https://www.youtube.com/")

		return render_template('index.html')
	else:
		return render_template('index.html')
	
app.secret_key = 'some key that you will never guess'

#Run the app on localhost port 5000
if __name__ == "__main__":
    app.run('127.0.0.1', 5002, debug = True)