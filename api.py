import src.getinfo as get
from flask import Flask, request
app = Flask(__name__)


@app.route('/<country>/<year>/<product>')
def allInfo(country,year,product):
    info = get.givenYear(country,year,product)
    return json.dumps(info)

























app.run("0.0.0.0", os.getenv("PORT"), debug=True)
