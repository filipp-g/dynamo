# Import modules
from flask import Flask, render_template
import xmltodict
import urllib3

app = Flask(__name__)
http = urllib3.PoolManager()

url = 'http://reports.ieso.ca/public/RealtimeConstTotals/PUB_RealtimeConstTotals.xml'
response = http.request('GET', url)
data = xmltodict.parse(response.data)


@app.route('/')
def index():
    consumption = get_interval_demands()
    return render_template('index.html', consumption=consumption)


def get_interval_demands():
    demands = []
    intervals = data.get("Document").get("DocBody").get("Energies").get("IntervalEnergy")
    for interval in intervals:
        market_quant = interval.get("MQ")
        for mq in market_quant:
            if mq.get("MarketQuantity") == "ONTARIO DEMAND":
                demands.append(float(mq.get("EnergyMW")))
    return(demands)


if __name__ == '__main__':
    app.run(debug=True)
