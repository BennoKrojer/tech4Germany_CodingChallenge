from flask import Flask, redirect
from flask_table import Table, Col
import acces_api
import config
app = Flask(__name__)


class ItemTable(Table):
    station = Col('Messstelle')
    level = Col('Wasserstand in cm')
    trend = Col('Trend des Wasserstands')
    warnings = Col('Meldungen')


@app.route("/")
def home():
    # redirecting to the default city 'passau'
    return redirect(f'/{config.default_city}')


@app.route("/<city>")
def city_status(city):
    items = acces_api.get_city_status(url=config.url, city=city.upper())
    table = ItemTable(items, border=True)
    print(items)
    return table.__html__()


if __name__ == "__main__":
    app.run()