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
    intervals = data.get("Document").get("DocBody").get("Energies").get("IntervalEnergy")
    intervals_len = str(len(intervals))
    for item in intervals:
        if item.get("Interval") == intervals_len:
            market_quant = item.get("MQ")
            for mq in market_quant:
                if mq.get("MarketQuantity") == "ONTARIO DEMAND":
                    return mq.get("EnergyMW")
    return("Not found")
