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
    demands = []
    for interval in intervals:
        market_quant = interval.get("MQ")
        for mq in market_quant:
            if mq.get("MarketQuantity") == "ONTARIO DEMAND":
                demands.append(mq.get("EnergyMW"))
    return(str(demands))
