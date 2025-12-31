#!/usr/bin/env python
"""Test script to display the dataframe output"""

from src.fetch_data import fetch_stock_data
import pandas as pd

# Fetch data for sample stocks
tickers = ['AAPL', 'MSFT', 'TSLA']
print(f"Fetching data for: {', '.join(tickers)}\n")

try:
    df = fetch_stock_data(tickers)
    
    print("\n" + "="*80)
    print("DATAFRAME SHAPE")
    print("="*80)
    print(f"Shape: {df.shape}")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n" + "="*80)
    print("FIRST 10 ROWS")
    print("="*80)
    print(df.head(10))
    
    print("\n" + "="*80)
    print("LAST 10 ROWS")
    print("="*80)
    print(df.tail(10))
    
    print("\n" + "="*80)
    print("DATAFRAME INFO")
    print("="*80)
    print(df.info())
    
    print("\n" + "="*80)
    print("DESCRIPTIVE STATISTICS")
    print("="*80)
    print(df.describe())
    
    print("\n" + "="*80)
    print("MISSING VALUES")
    print("="*80)
    print(df.isnull().sum())
    
    print("\n" + "="*80)
    print("CORRELATION MATRIX")
    print("="*80)
    print(df.corr())
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
