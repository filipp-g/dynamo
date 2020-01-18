# Import modules
from flask import Flask
import xmltodict
import urllib3

app = Flask(__name__)

url = 'http://reports.ieso.ca/public/RealtimeConstTotals/PUB_RealtimeConstTotals.xml'

http = urllib3.PoolManager()
response = http.request('GET', url)

data = xmltodict.parse(response.data)

@app.route('/')
def index():
    return(data)
