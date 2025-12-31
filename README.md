# Market Data Analyzer

A powerful Python-based stock market analysis tool that fetches real-time stock data, calculates volatility metrics, analyzes correlations, and generates beautiful visualizations.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## Features

- **Real-time Data Fetching**: Automatically fetches stock data from Yahoo Finance
- **Volatility Analysis**: Calculate and visualize stock volatility metrics
- **Correlation Analysis**: Analyze relationships between multiple stocks
- **Risk Assessment**: Categorize stocks as Low, Medium, or High Risk based on volatility
- **Beautiful Visualizations**:
  - Stock Price Trends (time-series plots)
  - Returns Distribution (histogram analysis)
  - Correlation Heatmap (relationship visualization)
- **Robust Error Handling**: Smart fallback system for reliable data fetching
- **Sample Data Support**: Demonstration mode with realistic synthetic data

## 📊 Sample Output

### Volatility Summary
```
┏━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Stock ┃ Volatility ┃  Risk Profile  ┃
┡━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ AAPL  │   0.0205   │ Medium Risk    │
│ MSFT  │   0.0153   │ Medium Risk    │
│ TSLA  │   0.0401   │  High Risk     │
└───────┴────────────┴────────────────┘
```

### Correlation Matrix
```
          AAPL      MSFT      TSLA
AAPL  1.000000  0.372710  0.811214
MSFT  0.372710  1.000000  0.582145
TSLA  0.811214  0.582145  1.000000
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/market-data-analyzer.git
cd market-data-analyzer
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

3. **Install dependencies**
```bash
pip install -r src/requirements.txt
```

### Usage

**Basic Usage:**
```bash
python src/main.py --stocks AAPL MSFT TSLA
```

**With Multiple Stocks:**
```bash
python src/main.py --stocks AAPL MSFT TSLA GOOGL AMZN NVDA
```

**Help:**
```bash
python src/main.py --help
```

##  Project Structure

```
market-data-analyzer/
├── src/
│   ├── main.py              # Main entry point
│   ├── fetch_data.py        # Data fetching logic with multiple sources
│   ├── analysis.py          # Financial analysis functions
│   ├── visualize.py         # Visualization functions
│   └── requirements.txt     # Project dependencies
├── plots/                   # Generated visualization plots
├── venv/                    # Virtual environment (if created locally)
├── .env                     # Environment variables (optional)
├── README.md               # This file
└── .gitignore              # Git ignore rules
```

##  Dependencies

- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computations
- **matplotlib**: Plotting library
- **seaborn**: Statistical data visualization
- **yfinance**: Yahoo Finance data fetching
- **pandas_datareader**: Alternative data source
- **requests**: HTTP requests library
- **python-dotenv**: Environment variable management
- **rich**: Beautiful terminal output
- **pytest**: Testing framework

## 🔄 Data Fetching Strategy

The application uses a robust 4-tier fallback system for data reliability:

1. **Direct Yahoo Finance API** (via requests) - Most reliable
2. **yfinance Library** - Secondary option
3. **pandas_datareader** - Tertiary option
4. **Sample Data** - Demonstration fallback

This ensures the application continues to work even if one data source fails.

##  Analysis Features

### Volatility Analysis
- Calculates daily returns standard deviation
- Risk classification:
  - 🟢 Low Risk: volatility < 0.015
  - 🟡 Medium Risk: 0.015 ≤ volatility < 0.03
  - 🔴 High Risk: volatility ≥ 0.03

### Correlation Analysis
- Pearson correlation coefficient
- Identifies relationships between stocks
- Visualized via heatmap

### Visualizations Generated
1. **Price Trends**: Historical stock prices over 1 year
2. **Returns Distribution**: Distribution of daily returns for each stock
3. **Correlation Heatmap**: Color-coded correlation matrix

All plots are saved to the `plots/` directory with timestamps.

## 🔐 Optional Configuration

Create a `.env` file for Alpha Vantage API (optional):
```
ALPHA_VANTAGE_API_KEY=your_api_key_here
```

Get a free API key at: https://www.alphavantage.co/

## 📝 Example Output

```
📈 Stock Volatility & Correlation Analyzer

Fetching real data for AAPL...
✓ Got real data for AAPL from Yahoo Finance API
Fetching real data for MSFT...
✓ Got real data for MSFT from Yahoo Finance API
Fetching real data for TSLA...
✓ Got real data for TSLA from Yahoo Finance API

      📊 Stock Volatility Summary      
┏━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Stock ┃ Volatility ┃ Risk Profile ┃
┡━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ AAPL  │   0.0205   │ Medium Risk 🟡│
│ MSFT  │   0.0153   │ Medium Risk 🟡│
│ TSLA  │   0.0401   │  High Risk 🔴│
└───────┴────────────┴──────────────┘

📊 Correlation Matrix

          AAPL      MSFT      TSLA
AAPL  1.000000  0.372710  0.811214
MSFT  0.372710  1.000000  0.582145
TSLA  0.811214  0.582145  1.000000

📈 Generating visualizations...

Plotting stock price trends...
   💾 Price trends plot saved to: plots\price_trends_20251231_143408.png
Plotting returns distribution...
   💾 Returns distribution plot saved to: plots\returns_distribution_20251231_143428.png
Plotting correlation heatmap...
   💾 Correlation heatmap saved to: plots\correlation_heatmap_20251231_143428.png

✓ Visualizations completed!
```

## 🧪 Testing

Run the data fetching test:
```bash
python test_df.py
```

This will display the dataframe structure and statistics.

## 🐛 Troubleshooting

### Issue: "No valid stock data fetched"
- Check your internet connection
- Verify ticker symbols are valid
- Try again later (Yahoo Finance might be temporarily unavailable)

### Issue: Missing dependencies
```bash
pip install --upgrade -r src/requirements.txt
```

### Issue: Plots not displaying
- Plots are automatically saved to the `plots/` folder
- Check the directory for PNG files with timestamps

## 💡 Use Cases

- **Portfolio Analysis**: Analyze volatility and correlation of your stock holdings
- **Risk Assessment**: Identify high-risk stocks in your portfolio
- **Market Research**: Compare performance metrics across multiple stocks
- **Educational**: Learn about financial analysis and data visualization

## 🔮 Future Enhancements

- [ ] Support for more data sources (crypto, commodities)
- [ ] Advanced metrics (Sharpe ratio, Sortino ratio, Beta)
- [ ] Portfolio optimization recommendations
- [ ] Interactive dashboard (Streamlit/Dash)
- [ ] Historical analysis and trend predictions
- [ ] Email report generation
- [ ] Database integration for data persistence

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📧 Support

For issues, questions, or suggestions, please open an issue on GitHub.

## 🙏 Acknowledgments

- Yahoo Finance for stock data
- pandas, matplotlib, and seaborn for data processing and visualization
- The open-source community for amazing libraries

## 📚 Resources

- [Yahoo Finance API](https://finance.yahoo.com/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [matplotlib Tutorials](https://matplotlib.org/stable/tutorials/index.html)
- [Financial Analysis Guide](https://www.investopedia.com/)

---

**Made with ❤️ by the Market Data Analyzer Team**

**Last Updated:** December 31, 2025
