
# Importing Flask modules for web application development
from flask import Flask, render_template, request

# Importing custom web scraping functions from 'scripts.co' module
import scripts.co.getpagecount as co_firstpage
import scripts.co.getHTMLfromPage as co_secondpage
import scripts.co.rename_folder as co_thirdpage
import scripts.co.scrap_website as co_fourpage

# Importing custom web scraping functions from 'scripts.srx' module
import scripts.srx.getpageCount as srx_firstpage
import scripts.srx.getHTMLfromPage as srx_secondpage
import scripts.srx.getdatafromHTML as srx_thirdpage

# Importing custom map plottinh functions from 'scripts.maplayput' module
import scripts.map_layout.chrolopleth_maps as mapsone

# Importing [PENDING] from 'scripts.algo' module
import scripts.algo.ToIntegrate as alogone

# Importing Mergering functions from 'scripts.merger_json' module
import scripts.merger_json.cleandata as clean_CO

# Importing Table Plotting functions from 'scripts.map_layout' module
import scripts.map_layout.table as table_d


# Create a Flask web application instance and set a secret key for session security
app = Flask(__name__)
app.secret_key = 'some key that you will never guess'


'''
    Initialize Init 
'''
user_input_page_count = 0
user_input_page_count_co = 0
user_input_page_count_prop = 0

mapbox_styles = [
    "open-street-map",
    "carto-positron",
    "carto-darkmatter",
    "stamen-terrain",
    "stamen-toner",
    "stamen-watercolor",
]


'''
    ---------- Initialize Root URL Route
'''


'''
    Route : /
    Description : Hello World Test
    Methods : GET & POST
'''


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print('Get Both Website Page Count')
    return render_template('index.html',valueFive=co_firstpage.main(), prop_value_page=srx_firstpage.main())


'''
    Route : /website
    Description : Get User Choice to chose which website to scrap
    Methods : GET & POST
'''


@app.route('/website', methods=['GET', 'POST'])
def website():
    if request.method == 'POST':
        # Get user choices
        selected_option = request.form['my_dropdown']
        # RENTinSINGAPORE
        if selected_option == '1':
            return render_template('index.html', valueFive=co_firstpage.main())
        elif selected_option == '2':
            return render_template('index.html', prop_value_page=srx_firstpage.main())


'''
    Route : /get_page_count_co
    Description : Store Selected Options into a Global Var for 99co Website 
    Methods : POST
'''


@app.route('/get_page_count_co', methods=['POST'])
def get_page_count_co():
    global user_input_page_count_co
    selected_option = request.form['my_page_co']
    user_input_page_count_co = selected_option
    print(selected_option)  # Print the selected option for debugging
    return render_template('index.html')


'''
    Route : /scrapping_co
    Description : Scrapping 99co Website 
    Methods : GET & POST
'''


@app.route('/scrapping_co', methods=['GET', 'POST'])
def scrapping_co():
    global user_input_page_count_co
    x = co_secondpage.main(int(user_input_page_count_co))
    co_thirdpage.renameFiles('centralized/99co/scrapping')
    co_fourpage.main('centralized/99co/scrapping')
    return render_template('index.html', valueSix=x)


'''
    Route : /get_page_count_prop
    Description : Store Selected Options into a Global Var for SRX Website 
    Methods : GET & POST
'''


@app.route('/get_page_count_prop', methods=['POST'])
def get_page_count_prop():
    global user_input_page_count_prop
    selected_option = request.form['my_page_prop']
    user_input_page_count_prop = selected_option
    print(selected_option)  # Print the selected option for debugging
    return render_template('index.html')


'''
    Route : /scrapping_prop
    Description : Scrapping SRX Website 
    Methods : GET & POST
'''


@app.route('/scrapping_prop', methods=['GET', 'POST'])
def scrapping_prop():
    global user_input_page_count_prop
    x = srx_secondpage.main(int(user_input_page_count_prop))
    srx_thirdpage.main('centralized/srx/scrapping')
    return render_template('index.html', prop_one=x)


'''
    Route : /formatCO
    Description : Clean & Format 99co JSON
    Methods : GET & POST
'''


@app.route('/formatCO', methods=['GET', 'POST'])
def formatCO():
    if request.method == 'POST':
        clean_CO.co_clean_data(
            'scripts/merger_json/data.csv', 'scripts/merger_json/clean_data.csv')
        return render_template('index.html')


'''
    Route : /merger_data
    Description : Merger 99co & SRX Excel togather 
    Methods : GET & POST
'''


@app.route('/merger_data', methods=['GET', 'POST'])
def merger_data():
    if request.method == 'POST':
        return render_template('index.html')


'''
    Route : /request_chart
    Description : Display Intrective Map from maplayout (folder)
    Methods : GET & POST
'''


@app.route('/request_chart', methods=['GET', 'POST'])
def request_chart():
    if request.method == 'POST':
        selected_option = request.form['my_dropdown_map']
        plot_div = mapsone.generate_plotly_chart(
            mapbox_styles[int(selected_option)])
        return render_template('charts.html', plot_div=plot_div)


'''
    Route : /display_table
    Description : Display Table from maplayout (folder)
    Methods : GET & POST
'''


@app.route('/display_table', methods=['GET', 'POST'])
def display_table():
    if request.method == 'POST':
        data = table_d.display_table()
        return render_template('charts.html', data=data)


'''
    Route : /run_logic
    Description : Run the Algo 
    Methods : GET & POST
'''


@app.route('/run_logic', methods=['GET', 'POST'])
def run_logic():
    if request.method == 'POST':
        alogone.algo()
        return render_template('charts.html')


'''
    Nav-Bar
'''
@app.route('/Charts')
def Charts():
    return render_template('charts.html')


@app.route('/scrapping')
def scrapping():
    return render_template('index.html')


'''
    Run the Flask application on the local server 
'''
if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)
