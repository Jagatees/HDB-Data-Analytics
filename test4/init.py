# Stuff to fix
# 1) auto create the page_scrape folder (99co)
# 2) fix big on renting room deep crawl only get 115 page even those got 1k rooms seems werid
# 5) merger the two json file into one big one , RIS + 99co (merger scrapping / deep crawling)
# 6) loading bar on website
# 7) add docker so everyone can run the project due to selium

from flask import Flask, render_template, request

# RentInSingapore - Scrapping (asyncio) & Deep Crawling (multiprocessing)
import backup.rentingSingpoare.main_page_scrapping as mainone
import backup.rentingSingpoare.scraperr_multi_threading as maintwo

# 99co - Scrapping (threading)
import scripts.co.getpagecount as co_firstpage
import scripts.co.getHTMLfromPage as co_secondpage
import scripts.co.rename_folder as co_thirdpage
import scripts.co.scrap_website as co_fourpage

# Propnex
import scripts.propnex.getpageCount as propnex_firstpage
import scripts.propnex.getHTMLfromPage as propnex_secondpage
import scripts.propnex.getdatafromHTML as propnex_thirdpage

# Deep Crawling 
import scripts.dcpropnex.getHTMLfromWebsite as dc_prop_one
import scripts.dcpropnex.getdatafromHTML as dc_prop_two

# Map
import scripts.map_layout.chrolopleth_maps as mapsone

# Algo
import scripts.algo.ToIntegrate as alogone


app = Flask(__name__)
app.secret_key = 'some key that you will never guess'


# Variable for use 
user_input_page_count = 0
timer_scrapping_ris = ''
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


# DO NOT DELETE THIS HELLO WORLD
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    print('Welcome to ICT1001 Porgramming A1')
    return render_template('index.html')

# Get Value from dropdown
@app.route('/website', methods=['GET', 'POST'])
def website():
    if request.method == 'POST':
        # Get user choices
        selected_option = request.form['my_dropdown']
        # RENTinSINGAPORE
        if selected_option == '1':
            return render_template('index.html', valueFive=co_firstpage.main())
        elif selected_option == '2':
            return render_template('index.html', prop_value_page = propnex_firstpage.main())
        
# 99co
@app.route('/get_page_count_co', methods=['POST'])
def get_page_count_co():
    global user_input_page_count_co
    selected_option = request.form['my_page_co']
    user_input_page_count_co = selected_option
    print(selected_option)  # Print the selected option for debugging
    return render_template('index.html')

@app.route('/scrapping_co', methods = ['GET', 'POST'])
def scrapping_co():
    global user_input_page_count_co
    x = co_secondpage.main(int(user_input_page_count_co))
    co_thirdpage.renameFiles('page_scrape')
    co_fourpage.main('page_scrape')
    return render_template('index.html', valueSix = x)

# PropNet

# Get Page Count from User Choice
@app.route('/get_page_count_prop', methods=['POST'])
def get_page_count_prop():
    global user_input_page_count_prop
    selected_option = request.form['my_page_prop']
    user_input_page_count_prop = selected_option
    print(selected_option)  # Print the selected option for debugging
    return render_template('index.html')

# Scrapp prop page 
@app.route('/scrapping_prop', methods = ['GET', 'POST'])
def scrapping_prop():
    global user_input_page_count_prop
    x = propnex_secondpage.main(int(user_input_page_count_prop))
    propnex_thirdpage.main('propnex_scrapped_html')
    return render_template('index.html', prop_one = x)

# Deep Crawling prop page 
@app.route('/dc_scrapping_prop', methods = ['GET', 'POST'])
def dc_scrapping_prop():
    x = dc_prop_one.main()
    dc_prop_two.main('deep_crawling_propnex_scrapped_html')
    return render_template('index.html', prop_two = x)


# Charts Display 
@app.route('/get_options', methods = ['GET', 'POST'])
def get_options():
    option_to_image = {
        '1': 'static/99co.png',
        '2': 'static/ris.png',
        '3': 'static/99co.png',
        '4': 'static/ris.png'
    }

    selected_option = request.form.get('options')
    image_value = option_to_image.get(selected_option, None)
    return render_template('index.html', imagevalue=image_value)


@app.route('/Charts')
def Charts():
    return render_template('charts.html')

@app.route('/scrapping')
def scrapping():
    return render_template('index.html')

# Interactive Chart
@app.route('/request_chart', methods = ['GET', 'POST'])
def request_chart():
    if request.method == 'POST':
        selected_option = request.form['my_dropdown_map']
        plot_div = mapsone.generate_plotly_chart(mapbox_styles[int(selected_option)])
        return render_template('charts.html', plot_div=plot_div)
    

# Logic
@app.route('/run_logic', methods = ['GET', 'POST'])
def run_logic():
    if request.method == 'POST':
        alogone.algo()
        return render_template('charts.html')
    
    


if __name__ == "__main__":
    app.run('127.0.0.1', 5012, debug=True)




