from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("table.html")

@app.route('/about')
def about():
    return render_template("about.html")

# MONGO DB Connection
# client = MongoClient("mongodb+srv://bdatprojecttest:passwordbdat@clusterbdat.wzvxq.mongodb.net/CAD_USD_Rates?ssl=true&ssl_cert_reqs=CERT_NONE")
# db = client.get_database('CAD_USD_Rates')
# records = db.forex

@app.route('/google-charts/line-chart_2017')
def google_line_chart_2017():
    data = {'Date' : 'Price', 'January':0.7580, 'February' :0.7629, 'March':0.7470, 'April':0.7440, 'May':0.7349, 'June':0.7520, 'July':0.7882, 'August':0.7933, 'September':0.8142, 'October':0.7934, 'November':0.7831, 'December':0.7830}
    return render_template('2017.html', data=data)

@app.route('/google-charts/line-chart_2018')
def google_line_chart_2018():
    data = {'Date' : 'Price', 'January':0.7989, 'February' :0.8138, 'March':0.7781, 'April':0.7747, 'May':0.7772, 'June':0.7714, 'July':0.7602, 'August':0.7691, 'September':0.7586, 'October':0.7811, 'November':0.7641, 'December':0.7581}
    return render_template('2018.html', data=data)

@app.route('/google-charts/line-chart_2019')
def google_line_chart_2019():
    data = {'Date' : 'Price', 'January':0.7353, 'February' :0.7637, 'March':0.7541, 'April':0.7498, 'May':0.7454, 'June':0.7424, 'July':0.7625, 'August':0.7566, 'September':0.7495, 'October':0.7551, 'November':0.7601, 'December':0.752}
    return render_template('2019.html', data=data)

@app.route('/google-charts/line-chart_2020')
def google_line_chart_2020():
    data = {'Date' : 'Price', 'January':0.7697, 'February' :0.7533, 'March':0.7487, 'April':0.7034, 'May':0.7109, 'June':0.7337, 'July':0.7361, 'August':0.7478, 'September':0.766, 'October':0.7523, 'November':0.7543, 'December':0.7721}
    return render_template('2020.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)