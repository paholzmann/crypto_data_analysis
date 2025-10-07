
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
        Creates a DataFrame for a pair (cryptocurrency/ fiat currency) on a custom timeframe.

        The DataFrame contains the timestamp including OHLCV (open, high, low, close, volume) data for a coin pair.
        This DataFrame is the basic DataFrame that can be extended with additional analytical columns and values.

        Args:
            coin (str): Chosen cryptocurrency.
            fiat (str): Chosen fiat currency.
            timeframe (str): Chosen timeframe.

        Returns:
            df (pd.DataFrame):
                DataFrame that contains OHLCV data for a coin pair.
                Columns:
                    * timestamp: Timestamp of the OHLCV data.
                    * open: Opening price of coin pair on given timestamp.
                    * high: Highest price of coin pair on given timestamp.
                    * low: Lowest price of coin pair on given timestamp.
                    * close: Closing price of coin pair on given timestamp.
                    * volume: Volume of coin pair on given timestamp.

        Example:
            btc_df = obj.create_coin_df(coin="BTC", fiat="USDT", timeframe="1d")
            >>>     timestamp   open        high        low         close       volume
                0   2025-10-06  124500.000  126000.000  123000.000  124800.000  150000000.000
                1   2025-10-05  124800.000  125000.000  124000.000  124900.000  120000000.000
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
        Creates a csv file with DataFrame.

        CSV-File will be created and added in its suitable folder.

        Args:
            df (pd.DataFrame): Coin pair DataFrame.
            coin (str): Chosen cryptocurrency.
            fiat (str): Chosen fiat currency.
            timeframe (str): Chosen timeframe.
            raw (bool | optional): If True then the csv file will be saved in data/raw, meaning the data in the csv file is incomplete.
            processed (bool | optional): If True then the csv file will be saved in data/processed, meaning the data in the csv file is complete.

        Output:
            data
                raw
                    btc.csv
                processed
                    btc.csv
            
        Example:
            obj.create_csv_by_df(df=btc_df, coin="BTC", fiat="USDT", timeframe="1d", raw=True, processed=False)
            >>> data/raw/btc.csv
                timestamp, open, high, low, close, volume
                2025-10-06, 124500.000, 126000.000, 123000.000, 124800.000, 150000000.000
                2025-10-5, 124800.000, 125000.000, 124000.000, 124900.000, 120000000.000
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
        Automate CSV-File creation.

        Create many CSV-Files thanks to automation.

        Args:
            coins (list of str): All chosen cryptocurrencies.
            fiats (list of str): All chosen fiat currencies.
            timeframes (list of str): All chosen timeframes.
            raw (bool | optional): If the data is unprocessed.
            processed (bool | optional): If the data is processed.

        Output:
            data
                raw
                    btc.csv
                    eth.csv
                processed
                    btc.csv
                    eth.csv

        Example:
            obj.automate_create_csv_by_df(coins=["BTC", "ETH"], fiats=["USDT", "USDT"], timeframes=["1d", "1h"], raw=True)
            >>> data/raw/btc.csv
                timestamp, open, high, low, close, volume
                2025-10-06, 124500.000, 126000.000, 123000.000, 124800.000, 150000000.000
                2025-10-5, 124800.000, 125000.000, 124000.000, 124900.000, 120000000.000
                
                data/raw/eth.csv
                timestamp, open, high, low, close, volume
                2025-10-06, 1200.000, 1300.000, 1100.000, 12000000.000
                2025-10-05, 1100.000, 1200.000, 1000.000, 1200.000, 1300000.000
        """
        for coin, fiat, timeframe in zip(coins, fiats, timeframes):
            df = self.create_coin_df(coin, fiat, timeframe)
            self.create_csv_by_df(df, coin, fiat, timeframe, raw, processed)

dl = DataLoader().automate_create_csv_by_df(coins=["BTC", "ETH"], fiats=["USDT", "USDT"], timeframes=["1d", "1h"], raw=True)
