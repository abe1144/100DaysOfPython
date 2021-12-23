import requests
import os
import pandas as pd
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

params = {"function":"TIME_SERIES_DAILY","symbol":STOCK, "apikey":os.environ.get("alphavantage")}


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get("https://www.alphavantage.co/query", params=params)
response.raise_for_status()
data = response.json()

daily_prices = data['Time Series (Daily)']

dataframe = pd.DataFrame.from_dict(daily_prices, orient="index")
dataframe.columns = ["open", "high", "low", "close", "volume"]

dataframe['open'] = pd.to_numeric(dataframe['open'], downcast="float")

dataframe = dataframe.sort_index()

dataframe['diff'] = dataframe['open'].diff()
dataframe['last_day_price'] = dataframe['open'].shift(1)
dataframe['pct_change'] = dataframe['diff'] / dataframe['last_day_price']

for index,row in dataframe.tail(5).iterrows():
    if abs(row['pct_change']) > 0.05:
        print(index, row['pct_change'])
        

        ## STEP 2: Use https://newsapi.org
        # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

        news_params = {"q":COMPANY_NAME,"from":index,"to":index, "sortBy":"popularity","apiKey":os.environ.get("newapi")}

        r = requests.get("https://newsapi.org/v2/everything", params=news_params)
        r.raise_for_status()
        news = r.json()
        news_lst = news['articles'][:3]
        descriptions = []
        for article in news_lst:
            descriptions.append(article['description'])
        
        
        ## STEP 3: Use https://www.twilio.com
        # Send a seperate message with the percentage change and each article's title and description to your phone number. 
        account_sid = os.environ.get("twilio_account_sid")
        auth_token = os.environ.get("twilio_key")

        client = Client(account_sid, auth_token)
        message = client.messages \
                    .create(
                        body="Headline1: {} \n Headline2: {} \n Headline3: {}".format(descriptions[0], descriptions[1], descriptions[2]),
                        from_='+12695254318',
                        to=os.environ.get("cell_number")
                 )
        print(message.status)


