#!/usr/bin/env python3
"""
Indian Stock Market Status Application
Fetches real-time data for Indian stock market indices and individual stocks
"""

import requests
import json
from datetime import datetime
from typing import Dict, List, Optional
import time

class IndianStockMarket:
    """Class to fetch Indian stock market data"""
    
    def __init__(self):
        self.base_url = "https://query1.finance.yahoo.com/v8/finance/chart/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Major Indian indices
        self.indices = {
            'NIFTY 50': '^NSEI',
            'SENSEX': '^BSESN',
            'NIFTY BANK': '^NSEBANK',
            'NIFTY IT': '^CNXIT',
            'NIFTY AUTO': '^CNXAUTO',
            'NIFTY PHARMA': '^CNXPHARMA',
            'NIFTY FMCG': '^CNXFMCG'
        }
        
        # Popular Indian stocks
        self.popular_stocks = {
            'Reliance Industries': 'RELIANCE.NS',
            'TCS': 'TCS.NS',
            'HDFC Bank': 'HDFCBANK.NS',
            'Infosys': 'INFY.NS',
            'ICICI Bank': 'ICICIBANK.NS',
            'State Bank of India': 'SBIN.NS',
            'ITC': 'ITC.NS',
            'Bharti Airtel': 'BHARTIARTL.NS',
            'Kotak Mahindra Bank': 'KOTAKBANK.NS',
            'HUL': 'HINDUNILVR.NS'
        }

    def fetch_stock_data(self, symbol: str) -> Optional[Dict]:
        """Fetch stock data for a given symbol"""
        try:
            url = f"{self.base_url}{symbol}"
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            result = data['chart']['result'][0]
            
            # Extract current price and metadata
            meta = result['meta']
            current_price = meta.get('regularMarketPrice', 0)
            previous_close = meta.get('previousClose', 0)
            change = current_price - previous_close
            change_percent = (change / previous_close) * 100 if previous_close != 0 else 0
            
            return {
                'symbol': symbol,
                'current_price': round(current_price, 2),
                'previous_close': round(previous_close, 2),
                'change': round(change, 2),
                'change_percent': round(change_percent, 2),
                'currency': meta.get('currency', 'INR'),
                'market_state': meta.get('marketState', 'UNKNOWN'),
                'timezone': meta.get('timezone', 'IST')
            }
            
        except Exception as e:
            print(f"Error fetching data for {symbol}: {str(e)}")
            return None

    def get_market_status(self) -> str:
        """Get current market status"""
        # Check NIFTY to determine market status
        nifty_data = self.fetch_stock_data('^NSEI')
        if nifty_data:
            return nifty_data['market_state']
        return "UNKNOWN"

    def display_indices(self):
        """Display major Indian stock market indices"""
        print("🇮🇳 INDIAN STOCK MARKET INDICES")
        print("=" * 50)
        
        market_status = self.get_market_status()
        print(f"Market Status: {market_status}")
        print(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}")
        print("-" * 50)
        
        for name, symbol in self.indices.items():
            data = self.fetch_stock_data(symbol)
            if data:
                change_indicator = "📈" if data['change'] >= 0 else "📉"
                print(f"{change_indicator} {name:<15}: ₹{data['current_price']:>8} "
                      f"({data['change']:+.2f}, {data['change_percent']:+.2f}%)")
            else:
                print(f"❌ {name:<15}: Data unavailable")
            time.sleep(0.1)  # Rate limiting

    def display_popular_stocks(self):
        """Display popular Indian stocks"""
        print("\n📊 POPULAR INDIAN STOCKS")
        print("=" * 50)
        
        for name, symbol in self.popular_stocks.items():
            data = self.fetch_stock_data(symbol)
            if data:
                change_indicator = "📈" if data['change'] >= 0 else "📉"
                print(f"{change_indicator} {name:<20}: ₹{data['current_price']:>8} "
                      f"({data['change']:+.2f}, {data['change_percent']:+.2f}%)")
            else:
                print(f"❌ {name:<20}: Data unavailable")
            time.sleep(0.1)  # Rate limiting

    def search_stock(self, query: str) -> Optional[Dict]:
        """Search for a specific stock (basic implementation)"""
        # Try to find in popular stocks first
        for name, symbol in self.popular_stocks.items():
            if query.lower() in name.lower():
                return self.fetch_stock_data(symbol)
        
        # Try direct symbol lookup (assuming .NS suffix for NSE)
        if not query.endswith('.NS'):
            query += '.NS'
        
        return self.fetch_stock_data(query)

    def get_market_summary(self) -> Dict:
        """Get a summary of the market performance"""
        nifty_data = self.fetch_stock_data('^NSEI')
        sensex_data = self.fetch_stock_data('^BSESN')
        
        summary = {
            'market_status': self.get_market_status(),
            'timestamp': datetime.now().isoformat(),
            'nifty_50': nifty_data,
            'sensex': sensex_data
        }
        
        return summary

def main():
    """Main function to run the stock market application"""
    market = IndianStockMarket()
    
    print("🇮🇳 Welcome to Indian Stock Market Status App!")
    print("=" * 60)
    
    while True:
        print("\nOptions:")
        print("1. View Market Indices")
        print("2. View Popular Stocks")
        print("3. Search Specific Stock")
        print("4. Market Summary (JSON)")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            market.display_indices()
        elif choice == '2':
            market.display_popular_stocks()
        elif choice == '3':
            query = input("Enter stock name or symbol: ").strip()
            if query:
                data = market.search_stock(query)
                if data:
                    change_indicator = "📈" if data['change'] >= 0 else "📉"
                    print(f"\n{change_indicator} {query.upper()}")
                    print(f"Current Price: ₹{data['current_price']}")
                    print(f"Change: {data['change']:+.2f} ({data['change_percent']:+.2f}%)")
                    print(f"Previous Close: ₹{data['previous_close']}")
                    print(f"Market State: {data['market_state']}")
                else:
                    print("❌ Stock not found or data unavailable")
        elif choice == '4':
            summary = market.get_market_summary()
            print("\n📋 Market Summary (JSON):")
            print(json.dumps(summary, indent=2))
        elif choice == '5':
            print("👋 Thank you for using Indian Stock Market Status App!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
