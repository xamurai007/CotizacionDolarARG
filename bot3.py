import tweepy
import time
import requests

#Authenticate to Twitter
CONSUMER_KEY = 'xxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

#Setting up connection
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user= api.me()

URL = 'https://mercados.ambito.com/'
dolar_dict = {
  "Dólar Oficial": "/dolar/oficial",
  "Dólar Turista": "/dolarturista",
  "Dólar Blue": "/dolar/informal",
  "Dólar Contado con Liqui": "/dolarrava/cl",
  "Dólar MEP": "/dolarrava/mep"
}

try:
 for dolar in dolar_dict:
   URL_FINAL = URL + dolar_dict[dolar] + "/variacion"
   json = requests.get(URL_FINAL).json()
   api.update_status(dolar + " - Compra: $" + json['compra'] + " / Venta: $" + json['venta'] + " - Variación: " +json['variacion'] + " #Dolar #DolarHoy #DolarBlue " + json['fecha'])
   time.sleep(15)
except:
  print("An exception occurred")
