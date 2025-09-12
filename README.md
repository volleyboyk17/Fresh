# Gold Rate Today 🏆

A comprehensive gold rate application that provides real-time gold prices in multiple formats and currencies.

## Features

- 📊 **Live Gold Prices**: Real-time gold rates from multiple reliable APIs
- 💎 **Multiple Formats**: Troy ounce, gram, and various karat purities (24K, 22K, 18K, etc.)
- 🌐 **Web Interface**: Beautiful, responsive web application
- 🔄 **Auto-refresh**: Prices update automatically every 5 minutes
- 🛡️ **Fallback System**: Reliable fallback prices when APIs are unavailable
- 🚀 **REST API**: Complete Python Flask API for integration

## Quick Start

### Web Application
Simply open `index.html` in your browser to view current gold rates with a beautiful interface.

### Python API Server
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python gold_api.py
   ```

3. Access the API at `http://localhost:5000`

## API Endpoints

- `GET /` - API documentation
- `GET /api/gold/current` - Current gold price per troy ounce
- `GET /api/gold/gram` - Current gold price per gram
- `GET /api/gold/karat/<karat>` - Gold price for specific karat (10, 14, 16, 18, 20, 21, 22, 24)
- `GET /api/gold/formats` - All gold price formats in one response
- `GET /api/health` - Health check endpoint

## Example API Response

```json
{
  "success": true,
  "data": {
    "price_per_oz": 2650.50,
    "timestamp": "2025-09-12T12:51:00",
    "source": "metals-api.com"
  },
  "unit": "USD per Troy Ounce"
}
```

## Gold Price Formats

- **Troy Ounce**: International standard for precious metals trading
- **Gram**: Common unit in jewelry markets
- **24K Gold**: Pure gold (100% purity)
- **22K Gold**: 91.67% purity (common in jewelry)
- **18K Gold**: 75% purity (popular for fine jewelry)

## Data Sources

The application fetches data from multiple reliable sources:
- metals-api.com
- goldpricez.com
- Fallback pricing when APIs are unavailable

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: Python Flask
- **APIs**: Multiple gold price data providers
- **Styling**: Modern CSS with gradients and animations

## License

Open source - feel free to use and modify as needed!
