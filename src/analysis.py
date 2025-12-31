import pandas as pd

def calculate_daily_returns(price_series):
    return price_series.pct_change().dropna()

def calculate_volatility(returns):
    return returns.std()

def calculate_correlation(returns_df):
    return returns_df.corr()
