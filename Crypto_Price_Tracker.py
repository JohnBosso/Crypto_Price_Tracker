from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pandas as pd
import os
from time import time
from time import sleep
import seaborn as sns
import matplotlib.pyplot as plt

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
#Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  # print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df = pd.json_normalize(data['data'])
df["timestamp"] = pd.to_datetime("now")
df
#print(df)

def api_run():
  global df
  url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest' 
  #Original Sandbox Environment: 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
  parameters = {
    'start':'1',
    'limit':'15',
    'convert':'USD'
  }
  headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '0ad53085-1cb2-4eb8-ad9e-3ffbd7e56509',
  }

  session = Session()
  session.headers.update(headers)

  try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # print(data)
  except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)

  pd.set_option("display.max_columns", None)
  pd.set_option("display.max_rows", None)

  df2 = pd.json_normalize(data['data'])
  df2["timestamp"] = pd.to_datetime("now")
  df = pd.concat([df, df2], ignore_index=True)
   
  # If you want it to craete and read into a csv file instead
  #df12 = pd.json_normalize(data['data'])
  #df12["timestamp"] = pd.to_datetime("now")
  #if not os.path.isfile(r"C:\Users\John\projects\API.csv"):
    #df.to_csv(r"C:\Users\John\projects\API.csv", header="column_names")
  #else:
    #df.to_csv(r"C:\Users\John\projects\API.csv", mode="a", header=False)

#for i in range(333):
#  api_run()
#  print("API Successful")
#  sleep(60)
#exit()

pd.set_option("display.float_format", lambda x: "%.5f" % x)
#print(df)

df4 = df.groupby("name", sort=False)[['quote.USD.percent_change_1h','quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d']].mean()

df5 = df4.stack()
#print(df5)

df6 = df5.to_frame(name="values")

df7 = df6.reset_index()

df7['level_1'] = df7['level_1'].replace(['quote.USD.percent_change_24h','quote.USD.percent_change_7d','quote.USD.percent_change_30d','quote.USD.percent_change_60d','quote.USD.percent_change_90d'],['24h','7d','30d','60d','90d'])

df8 = df7.rename(columns={"level_1": "percent_change"})


sns.catplot(x="percent_change", y="values", hue="name", data=df8, kind="point")
#plt.show()

df9 = df[['name','quote.USD.price','timestamp']]
df9 = df9.query("name == 'Bitcoin'")
print(df9)

sns.set_theme(style="darkgrid")
sns.lineplot(x="timestamp", y="quote.USD.price", data=df9)
plt.show()