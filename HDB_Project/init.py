
# Importing Flask modules for web application development
from flask import Flask, render_template, request

# Importing custom web scraping functions from 'scripts.co' module
import scripts.ninety_nine_co.getpagecount as co_getPageCount
import scripts.ninety_nine_co.getHTMLfromPage as co_extractHTMLfromPages
import scripts.ninety_nine_co.rename_folder as co_Renamefolder
import scripts.ninety_nine_co.scrap_website as co_Scrapewebsite
# Importing custom web scraping functions from 'scripts.srx' module
import scripts.srx.getpageCount as srx_getPageCount
import scripts.srx.getHTMLfromPage as srx_extractHTMLfromPages
import scripts.srx.getdatafromHTML as srx_GetDatafromHTML
# Importing algo from 'scripts.algo' module
import scripts.algo.ToIntegrate as logic_caculation
# Importing Mergering functions from 'scripts.merger_json' module
import scripts.merger_json.convert_co as convertCo
import scripts.merger_json.clean_co as cleanCo
# Importing Mergering functions from 'scripts.merger_json' module
import scripts.merger_json.convert_srx as convertSRX
import scripts.merger_json.clean_srx as cleanSRX
# Importing Merger Function from 'scripst.merger_json' module
import scripts.merger_json.merger as merger_csv
# Importing custom map plottinh functions from 'scripts.maplayput' module
import scripts.plotting.chrolopleth_maps as plotMap
# Importing Table Plotting functions from 'scripts.map_layout' module
import scripts.plotting.different_plot as plotCharts
# Importing Clearning for Area from 'scripts.filter' 
import scripts.filter_area.Area as areaCleaning 

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
    return render_template('index.html')


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
            return render_template('index.html', valueFive=co_getPageCount.main())
        elif selected_option == '2':
            return render_template('index.html', prop_value_page=srx_getPageCount.main())


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
    x = co_extractHTMLfromPages.main(int(user_input_page_count_co))
    co_Renamefolder.renameFiles('centralized/99co/scrapping')
    co_Scrapewebsite.main('centralized/99co/scrapping')
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
    x = srx_extractHTMLfromPages.main(int(user_input_page_count_prop))
    srx_GetDatafromHTML.main('centralized/srx/scrapping')
    return render_template('index.html', prop_one=x)


'''
    Route : /formatCO
    Description : Clean & Format 99co JSON
    Methods : GET & POST
'''


@app.route('/formatCO', methods=['GET', 'POST'])
def formatCO():
    if request.method == 'POST':
        # Add File Path here later
        convertCo.convert_csv('centralized/99co/json/nintynine_scrap.json', 'centralized/99co/json/99co_excel.csv')
        cleanCo.clean_co('centralized/99co/json/99co_excel.csv', 'centralized/99co/json/99co_final.csv')
        return render_template('index.html')
    
'''
    Route : /formatCO
    Description : Clean & Format 99co JSON
    Methods : GET & POST
'''


@app.route('/formatRSX', methods=['GET', 'POST'])
def formatRSX():
    if request.method == 'POST':
        convertSRX.convert_csv('centralized/srx/json/srx_scrapping.json', 'centralized/srx/json/srx_excel.csv')
        cleanSRX.clean_co('centralized/srx/json/srx_excel.csv', 'centralized/srx/json/srx_final.csv')
        return render_template('index.html')


'''
    Route : /merger_data
    Description : Merger 99co & SRX Excel togather 
    Methods : GET & POST
'''


@app.route('/merger_data', methods=['GET', 'POST'])
def merger_data():
    if request.method == 'POST':
        merger_csv.meger_csv('centralized/99co/json/99co_final.csv', 
                             'centralized/srx/json/srx_final.csv',
                             'centralized/merger/csv_merged_final.csv')
        areaCleaning.area_cleaning()
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
        selected_option_area = request.form['drop_down_area']
        selected_option_type = request.form['drop_down_room_type']
        plot_div = plotMap.generate_plotly_chart(
            mapbox_styles[int(selected_option)], selected_option_area, selected_option_type)
        return render_template('charts.html', plot_div=plot_div[0], map_query = plot_div[1])


'''
    Route : /display_table
    Description : Display Table from maplayout (folder)
    Methods : GET & POST
'''


@app.route('/display_table', methods=['GET', 'POST'])
def display_table():
    if request.method == 'POST':
        # data = plotCharts.display_table()
        data = plotCharts.heatmap()
        return render_template('charts.html', data=data)


'''
    Route : /run_logic
    Description : Run the Algo 
    Methods : GET & POST
'''


@app.route('/run_logic', methods=['GET', 'POST'])
def run_logic():
    if request.method == 'POST':       
        user_hospital = request.form['my_dropdown_hospital']
        user_area = request.form['drop_down_area']
        user_mrt = request.form['drop_down_mrt']
        user_supermarket = request.form['drop_down_supermarket']
        user_park = request.form['drop_down_parks']

        logic_caculation.algo(int(user_hospital), int(user_area), int(user_mrt), int(user_supermarket), int(user_park))
        logic_caculation.predicition_for_percentage()
        logic_caculation.get_data_from_million_door_file()
        logic_caculation.profit()
        return render_template('charts.html' )
    

'''
    Route : /which_chart
    Description : Chose which chart to plot
    Methods : GET & POST
'''


@app.route('/which_chart', methods=['GET', 'POST'])
def which_chart():
    if request.method == 'POST':       
        userchoice = request.form['my_dropdown_plot']

        if userchoice == "0":
            data = plotCharts.display_table_test()
        elif userchoice == "1":
            data = plotCharts.heatmap()

        return render_template('charts.html', data = data)
    

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
    app.run('127.0.0.1', 5001, debug=True)
