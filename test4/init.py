from flask import Flask, render_template, request
import scripts.rentingSingpoare.main_page_scrapping as mainone
import scripts.rentingSingpoare.scraperr_multi_threading as maintwo

# Add in scrapping renting in singapore (DONE)
# Add in deep crawling for renting in singapore (PENDING)
# Add in scrapping form 99co (PENDING)
# Add in deep crawling from 99co (PENDING)


app = Flask(__name__)
app.secret_key = 'some key that you will never guess'

user_input_page_count = 0
timer_scrapping_ris = ''

# DO NOT DELETE THIS HELLO WORLD
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print('hello world')
    return render_template('index.html')

# Get Value from dropdown
@app.route('/website', methods=['GET', 'POST'])
def website():
    if request.method == 'POST':
        # Get user choices
        selected_option = request.form['my_dropdown']
        # RENTinSINGAPORE
        if selected_option == '1':
            return render_template('index.html', value=mainone.pageCount())
        
# Get Number from Dropdown 
@app.route('/get_page_count', methods=['POST'])
def get_page_count():
    global user_input_page_count
    selected_option = request.form['my_page']
    user_input_page_count = selected_option
    print(selected_option)  # Print the selected option for debugging
    return render_template('index.html')

# Scrapp Rent in Singapore
@app.route('/scrappingRIS', methods = ['GET', 'POST'])
def scrap_ris():
    global user_input_page_count
    global timer_scrapping_ris
    x = mainone.main(int(user_input_page_count))
    timer_scrapping_ris = x
    return render_template('index.html', valueTwo = x)

# Deep Crawling Rent in Singapore
@app.route('/deepcrawlingRIS', methods = ['GET', 'POST'])
def deepcrawl_ris():
    return render_template('index.html', valueTwo = timer_scrapping_ris, valueThree = maintwo.main())


if __name__ == "__main__":
    app.run('127.0.0.1', 5002, debug=True)
