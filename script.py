from flask import Flask,render_template
from covid import get_covid_info
app = Flask(__name__)
@app.route('/')
def index():
    return 'hello world'
@app.route('/covid')
def getcovid():
    obj = get_covid_info()
    captions = ["Country","NewConfirmed","TotalConfirmed","TotalRecovered"]
    for caption in captions:
        print(caption,obj[caption])
    return render_template('template.htm',data=obj,capts=captions)
app.run(host='0.0.0.0',port=81)