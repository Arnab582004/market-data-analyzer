import pandas as pd
from src.analysis import calculate_volatility

def test_volatility_calculation():
    data = pd.Series([0.01, -0.02, 0.03, -0.01])
    vol = calculate_volatility(data)
    assert vol > 0
