
import pandas as pd
import ccxt

# python src/data_loader.py

class DataLoader:
    """
    
    """
    def __init__(self):
        """
        
        """
        self.exchange = ccxt.binance()
    
    def create_coin_df(self, coin, fiat, timeframe):
        """
        coin = BTC
        fiat = USDT
        timeframe = 1d
        """
        coin, fiat = coin.upper(), fiat.upper()
        try:
            bars = self.exchange.fetch_ohlcv(f"{coin}/{fiat}", timeframe=f"{timeframe}", limit=1000)
        except Exception as error:
            print(f"Error fetching data for {coin}/{fiat}: {error}")
            bars = []
        
        df = pd.DataFrame(bars, columns=["timestamp", "open", "high", "low", "close", "volume"])
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
        return df
    
    def create_csv_by_df(self, df, coin, fiat, timeframe, raw=False, processed=False):
        """
        
        """
        if raw:
            df.to_csv(f"data/raw/{coin}_{fiat}_{timeframe}.csv")
            print(f"CSV created: data/raw/{coin}_{fiat}_{timeframe}.csv")
        elif processed:
            df.to_csv(f"data/processed/{coin}_{fiat}_{timeframe}.csv")
            print(f"CSV created: data/processed/{coin}_{fiat}_{timeframe}.csv")
        else:
            print("Please choose between raw and processed folder.")

    
    def automate_create_csv_by_df(self, coins, fiats, timeframes, raw=False, processed=False):
        """
        
        """
        for coin, fiat, timeframe in zip(coins, fiats, timeframes):
            df = self.create_coin_df(coin, fiat, timeframe)
            self.create_csv_by_df(df, coin, fiat, timeframe, raw, processed)

dl = DataLoader().automate_create_csv_by_df(coins=["BTC", "ETH"], fiats=["USDT", "USDT"], timeframes=["1d", "1h"], raw=True)
