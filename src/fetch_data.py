import os
import time
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import requests

try:
    import pandas_datareader as pdr
except ImportError:
    pdr = None


def create_sample_data(symbol, days=365):
    """Create realistic sample stock data for demonstration"""
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    
    # Base prices for each ticker
    base_prices = {
        'AAPL': 190,
        'MSFT': 410,
        'TSLA': 260,
        'GOOGL': 140,
        'AMZN': 190,
        'NVDA': 130
    }
    
    base_price = base_prices.get(symbol, 100)
    
    # Generate realistic-looking price data
    np.random.seed(hash(symbol) % 2**32)
    returns = np.random.normal(0.0005, 0.02, len(dates))
    prices = base_price * np.exp(np.cumsum(returns))
    
    return pd.Series(prices, index=dates, name="Close")


def fetch_from_pandas_datareader(symbol):
    """Try to fetch from pandas_datareader (Yahoo Finance)"""
    if pdr is None:
        return None
    
    try:
        end_date = datetime.today()
        start_date = end_date - timedelta(days=365)
        
        df = pdr.data.DataReader(
            name=symbol,
            data_source="yahoo",
            start=start_date,
            end=end_date
        )
        if df.empty or df is None:
            return None

        return df["Close"]
    except Exception as e:
        return None


def fetch_from_requests_yahoo(symbol):
    """Fetch from Yahoo Finance using requests with proper headers"""
    try:
        # Use proper user-agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        end_date = int(datetime.now().timestamp())
        start_date = int((datetime.now() - timedelta(days=365)).timestamp())
        
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        params = {
            'interval': '1d',
            'period1': start_date,
            'period2': end_date
        }
        
        response = requests.get(url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        if 'chart' not in data or 'result' not in data['chart'] or not data['chart']['result']:
            return None
        
        result = data['chart']['result'][0]
        timestamps = result['timestamp']
        closes = result['indicators']['quote'][0]['close']
        
        # Filter out None values
        prices = []
        dates = []
        for ts, close in zip(timestamps, closes):
            if close is not None:
                prices.append(close)
                dates.append(pd.to_datetime(ts, unit='s'))
        
        if not prices:
            return None
        
        return pd.Series(prices, index=dates, name="Close")
    
    except Exception as e:
        print(f"⚠️ Direct Yahoo requests error: {e}")
        return None


def fetch_from_yfinance(symbol):
    """Try to fetch from yfinance as fallback"""
    try:
        import yfinance as yf
        
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        
        # Try with improved parameters and retries
        for attempt in range(3):
            try:
                df = yf.download(
                    symbol,
                    start=start_date.strftime("%Y-%m-%d"),
                    end=end_date.strftime("%Y-%m-%d"),
                    progress=False,
                    threads=False,
                    timeout=30
                )

                if df.empty or df is None or len(df) == 0:
                    if attempt < 2:
                        time.sleep(2)
                        continue
                    return None

                return df["Close"]
            except Exception as e:
                if attempt < 2:
                    print(f"⚠️ Retry {attempt + 1}/3 for {symbol}...")
                    time.sleep(2)
                    continue
                raise e
                
    except Exception as e:
        print(f"⚠️ yfinance error: {e}")
        return None


def fetch_single_stock(symbol):
    """Fetch stock data with fallbacks: requests -> yfinance -> pandas_datareader -> sample data"""
    
    print(f"Fetching real data for {symbol}...")
    
    # Try direct requests to Yahoo Finance first (most reliable)
    close_prices = fetch_from_requests_yahoo(symbol)
    if close_prices is not None and len(close_prices) > 0:
        print(f"✓ Got real data for {symbol} from Yahoo Finance API")
        return close_prices
    
    # Try yfinance
    close_prices = fetch_from_yfinance(symbol)
    if close_prices is not None and len(close_prices) > 0:
        print(f"✓ Got real data for {symbol} from yfinance")
        return close_prices
    
    # Try pandas_datareader
    close_prices = fetch_from_pandas_datareader(symbol)
    if close_prices is not None and len(close_prices) > 0:
        print(f"✓ Got real data for {symbol} from pandas_datareader")
        return close_prices
    
    # Use sample data as last resort
    print(f"⚠️ Using sample data for {symbol}")
    return create_sample_data(symbol)


def fetch_stock_data(tickers):
    """Fetch stock data for multiple tickers with fallback logic"""
    all_prices = {}

    for ticker in tickers:
        try:
            close_prices = fetch_single_stock(ticker)
            if close_prices is not None and len(close_prices) > 0:
                all_prices[ticker] = close_prices
        except Exception as e:
            print(f"❌ Error fetching {ticker}: {e}")
            # Try sample data as last resort
            try:
                all_prices[ticker] = create_sample_data(ticker)
                print(f"   Using sample data for {ticker}")
            except:
                pass

        # Respect API rate limits
        time.sleep(1)

    if not all_prices:
        raise RuntimeError("No valid stock data fetched.")

    price_df = pd.DataFrame(all_prices).dropna()

    if price_df.empty:
        # If all data was dropped, use the original data without dropping NaN
        price_df = pd.DataFrame(all_prices)

    return price_df
