# 🇮🇳 Indian Stock Market Status

A comprehensive Python application to fetch and display real-time Indian stock market data including major indices (NIFTY 50, SENSEX) and popular stocks.

## Features

- 📊 **Real-time Market Data**: Fetch live prices for Indian stock market indices and individual stocks
- 🏦 **Major Indices**: NIFTY 50, SENSEX, NIFTY BANK, NIFTY IT, and more
- 📈 **Popular Stocks**: Reliance, TCS, HDFC Bank, Infosys, and other top Indian companies
- 🔍 **Stock Search**: Search for specific stocks by name or symbol
- 🌐 **REST API**: Flask-based API for programmatic access
- 💹 **Market Status**: Real-time market status (OPEN/CLOSED/PRE_MARKET)
- 📱 **Interactive CLI**: User-friendly command-line interface

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Fresh
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

Run the interactive CLI application:

```bash
python indian_stock_market.py
```

The CLI provides the following options:
1. **View Market Indices** - Display major Indian stock market indices
2. **View Popular Stocks** - Show popular Indian stocks with current prices
3. **Search Specific Stock** - Search for any stock by name or symbol
4. **Market Summary (JSON)** - Get structured market data in JSON format
5. **Exit** - Close the application

### REST API

Start the Flask API server:

```bash
python stock_api.py
```

The API will be available at `http://localhost:5000` with the following endpoints:

#### API Endpoints

- **GET /** - API documentation and available endpoints
- **GET /api/indices** - Get all major Indian stock market indices
- **GET /api/stocks** - Get popular Indian stocks
- **GET /api/stock/\<symbol\>** - Get specific stock data (e.g., `/api/stock/RELIANCE.NS`)
- **GET /api/search?q=\<query\>** - Search for stocks (e.g., `/api/search?q=reliance`)
- **GET /api/summary** - Get market summary with NIFTY and SENSEX data

#### Example API Responses

**Market Indices:**
```json
{
  "status": "success",
  "market_status": "REGULAR",
  "data": {
    "NIFTY 50": {
      "symbol": "^NSEI",
      "current_price": 19674.25,
      "previous_close": 19653.75,
      "change": 20.5,
      "change_percent": 0.10,
      "currency": "INR",
      "market_state": "REGULAR"
    }
  }
}
```

**Individual Stock:**
```json
{
  "status": "success",
  "data": {
    "symbol": "RELIANCE.NS",
    "current_price": 2456.80,
    "previous_close": 2445.30,
    "change": 11.50,
    "change_percent": 0.47,
    "currency": "INR",
    "market_state": "REGULAR"
  }
}
```

## Supported Indices

- **NIFTY 50** (^NSEI) - NSE's flagship index
- **SENSEX** (^BSESN) - BSE's benchmark index
- **NIFTY BANK** (^NSEBANK) - Banking sector index
- **NIFTY IT** (^CNXIT) - Information Technology sector
- **NIFTY AUTO** (^CNXAUTO) - Automobile sector
- **NIFTY PHARMA** (^CNXPHARMA) - Pharmaceutical sector
- **NIFTY FMCG** (^CNXFMCG) - Fast Moving Consumer Goods

## Popular Stocks Included

- Reliance Industries (RELIANCE.NS)
- Tata Consultancy Services (TCS.NS)
- HDFC Bank (HDFCBANK.NS)
- Infosys (INFY.NS)
- ICICI Bank (ICICIBANK.NS)
- State Bank of India (SBIN.NS)
- ITC (ITC.NS)
- Bharti Airtel (BHARTIARTL.NS)
- Kotak Mahindra Bank (KOTAKBANK.NS)
- Hindustan Unilever (HINDUNILVR.NS)

## Data Source

The application uses Yahoo Finance API to fetch real-time stock market data. The data includes:
- Current market price
- Previous day's closing price
- Price change (absolute and percentage)
- Market status (OPEN/CLOSED/PRE_MARKET/POST_MARKET)
- Currency information

## Market Hours

Indian stock markets (NSE/BSE) operate:
- **Regular Trading**: 9:15 AM to 3:30 PM IST (Monday to Friday)
- **Pre-market**: 9:00 AM to 9:15 AM IST
- **Post-market**: 3:40 PM to 4:00 PM IST

## Error Handling

The application includes comprehensive error handling for:
- Network connectivity issues
- Invalid stock symbols
- API rate limiting
- Market data unavailability

## Contributing

Feel free to contribute by:
1. Adding more Indian stocks or indices
2. Implementing additional features
3. Improving error handling
4. Adding tests
5. Enhancing documentation

## License

This project is open source and available under the MIT License.

## Disclaimer

This application is for educational and informational purposes only. It should not be used as the sole basis for investment decisions. Always consult with a qualified financial advisor before making investment decisions.
