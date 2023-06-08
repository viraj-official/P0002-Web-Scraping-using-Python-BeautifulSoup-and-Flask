from flask import Flask,render_template
import socket
import pandas as pd
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return ('server up and running')

@app.route('/cripto/<date>')
def cripto(date):
    url = 'https://coinmarketcap.com/historical/%s/' % date
    webpage = requests.get(url)

    soup = BeautifulSoup(webpage.text, 'html.parser')
    rows = soup.find_all('tr', attrs={'class':'cmc-table-row'})

    crypto = []
    for row in rows:
        # Store name of the crypto currency            
        name_col = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name'})
        if name_col == None:
          break
        
        # Crypto currency name
        cryptoname = name_col.find('a', attrs={'class':'cmc-table__column-name--name cmc-link'}).text.strip()

        # Market cap
        marketcap = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap'}).text.strip()

        # Price
        crytoprice = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price'}).text.strip()

        # Circulating supply and symbol            
        circulatingSupplySymbol = row.find('td', attrs={'class':'cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply'}).text.strip()
        supply = circulatingSupplySymbol.split(' ')[0]
        sym = circulatingSupplySymbol.split(' ')[1]
        
        # append the data
        crypto.append({"name":cryptoname, "marketCap":marketcap, "price":crytoprice, "circulatingSupply":supply, "symbol":sym})

    return crypto


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
