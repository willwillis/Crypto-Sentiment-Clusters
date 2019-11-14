import requests
import pandas as pd
from pprint import pprint

def get_crypto_daily_hist(ticker):
    """
    makes request to cryptocompare to grab 2000 HOURLY Crypto
    prices compared to USD. Valid tickers are: BTC, ETH, BCH
    
    Arguments:
        get_crypto_daily_hist(string) -  BTC or ETH or BCH
    """
    valid_tick = ["BTC", "ETH", "BCH"]
    api_key = "320d3649d072d10f295c182cd1f3b068e4726ba8a78289d1e1881718b8d30d0d"
    # Sorry Cam...
    # Left this out in the open, I couldn't help myself 
    # https://rice.bootcampcontent.com/Rice-Coding-Bootcamp/RU-HOU-FIN-PT-07-2019-U-C/blob/master/class/14-Deep-Learning/1/review/regression.ipynb
    
    if ticker in valid_tick: 
        url= f"https://min-api.cryptocompare.com/data/v2/histohour?fsym={ticker}&tsym=USD&api_key={api_key}&limit=2000"

        res = requests.get(url)
        res = res.json()
        
        if res["Response"] == "Success":
            return res["Data"]["Data"]
        
        else:
            
            raise Error("Response not successful! Error from request: " + res["Response"])
    
    else:
        raise ValueError("You lack a valid ticker symbol (Use BTC, ETH, BCH)")
        
def preprocess(historical_list, ticker, date_start=None, date_end=None):
    ticker = ticker.upper()
    df = pd.DataFrame(historical_list)
    df["conversionSymbol"] = ticker
    df["date_time"] = pd.to_datetime(df['time'], infer_datetime_format=True, unit="s")
    
    filtered_df = df[["date_time","time", "close","conversionSymbol", "volumeto", "volumefrom"]]
    
    if date_start:
        filtered_df = filtered_df[filtered_df['date_time']> date_start]
    if date_end:
        filtered_df = filtered_df[filtered_df['date_time']< date_end]
        
    return filtered_df

def get_crypto_daily_hist_as_pd(ticker):
    ticker = ticker.upper()
    return preprocess(get_crypto_daily_hist(ticker), ticker, '2019-10-15', '2019-11-01')