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

URL = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
json = requests.get(URL).json()

try:
 for dolar in json:
  if dolar['casa']['nombre'] not in ["Argentina","Dolar","Dolar Soja","Dolar Contado con Liqui","Bitcoin","Dolar turista"]:
   api.update_status(dolar['casa']['nombre'] + " - Compra: $"+ dolar['casa']['compra'] + " / Venta: $"+ dolar['casa']['venta'] + " #Dolar #DolarHoy #DolarBlue")
   time.sleep(15)
except:
  print("An exception occurred")
