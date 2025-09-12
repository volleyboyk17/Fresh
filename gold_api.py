#!/usr/bin/env python3
"""
Gold Rate API - A simple Flask API to fetch current gold prices
Provides endpoints for various gold rate formats and currencies
"""

import requests
import json
from datetime import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GoldRateAPI:
    def __init__(self):
        self.apis = [
            {
                'name': 'metals-api',
                'url': 'https://metals-api.com/api/latest',
                'parser': self._parse_metals_api
            },
            {
                'name': 'goldpricez',
                'url': 'https://goldpricez.com/api/rates/gold/usd/1',
                'parser': self._parse_goldpricez
            }
        ]
        self.cache = {}
        self.cache_duration = 300  # 5 minutes in seconds
    
    def _parse_metals_api(self, data):
        """Parse metals-api.com response"""
        try:
            if 'rates' in data and 'Gold(USDXAU)' in data['rates']:
                return {
                    'price_per_oz': data['rates']['Gold(USDXAU)'],
                    'timestamp': data.get('date', datetime.now().isoformat()),
                    'source': 'metals-api.com'
                }
        except Exception as e:
            logger.error(f"Error parsing metals-api data: {e}")
        return None
    
    def _parse_goldpricez(self, data):
        """Parse goldpricez.com response"""
        try:
            if isinstance(data, dict) and 'gold' in data:
                return {
                    'price_per_oz': data['gold'],
                    'timestamp': datetime.now().isoformat(),
                    'source': 'goldpricez.com'
                }
            elif isinstance(data, (int, float)):
                return {
                    'price_per_oz': data,
                    'timestamp': datetime.now().isoformat(),
                    'source': 'goldpricez.com'
                }
        except Exception as e:
            logger.error(f"Error parsing goldpricez data: {e}")
        return None
    
    def fetch_gold_price(self):
        """Fetch current gold price from available APIs"""
        # Check cache first
        now = datetime.now().timestamp()
        if 'gold_price' in self.cache:
            cache_time = self.cache['gold_price'].get('cached_at', 0)
            if now - cache_time < self.cache_duration:
                return self.cache['gold_price']['data']
        
        # Try each API
        for api in self.apis:
            try:
                logger.info(f"Trying API: {api['name']}")
                response = requests.get(api['url'], timeout=10)
                
                if response.status_code == 200:
                    data = response.json()
                    parsed_data = api['parser'](data)
                    
                    if parsed_data:
                        # Cache the result
                        self.cache['gold_price'] = {
                            'data': parsed_data,
                            'cached_at': now
                        }
                        logger.info(f"Successfully fetched from {api['name']}")
                        return parsed_data
                        
            except Exception as e:
                logger.error(f"Error with {api['name']}: {e}")
                continue
        
        # Fallback price if all APIs fail
        logger.warning("All APIs failed, using fallback price")
        fallback_data = {
            'price_per_oz': 2650.00,  # Approximate current gold price
            'timestamp': datetime.now().isoformat(),
            'source': 'fallback',
            'note': 'This is a fallback price as live APIs are unavailable'
        }
        
        # Cache fallback for shorter duration
        self.cache['gold_price'] = {
            'data': fallback_data,
            'cached_at': now - self.cache_duration + 60  # Cache for 1 minute only
        }
        
        return fallback_data

# Initialize the gold rate API
gold_api = GoldRateAPI()

@app.route('/')
def home():
    """API documentation endpoint"""
    return jsonify({
        'name': 'Gold Rate API',
        'version': '1.0.0',
        'description': 'Get current gold prices in various formats',
        'endpoints': {
            '/api/gold/current': 'Get current gold price per troy ounce',
            '/api/gold/gram': 'Get current gold price per gram',
            '/api/gold/formats': 'Get gold prices in multiple formats',
            '/api/gold/karat/<karat>': 'Get gold price for specific karat (e.g., 24, 22, 18)',
        },
        'example': '/api/gold/current'
    })

@app.route('/api/gold/current')
def get_current_gold_price():
    """Get current gold price per troy ounce"""
    try:
        data = gold_api.fetch_gold_price()
        return jsonify({
            'success': True,
            'data': data,
            'unit': 'USD per Troy Ounce'
        })
    except Exception as e:
        logger.error(f"Error in get_current_gold_price: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/gold/gram')
def get_gold_price_per_gram():
    """Get current gold price per gram"""
    try:
        data = gold_api.fetch_gold_price()
        price_per_gram = data['price_per_oz'] / 31.1035  # Convert troy ounce to gram
        
        return jsonify({
            'success': True,
            'data': {
                'price_per_gram': round(price_per_gram, 2),
                'price_per_oz': data['price_per_oz'],
                'timestamp': data['timestamp'],
                'source': data['source']
            },
            'unit': 'USD per Gram'
        })
    except Exception as e:
        logger.error(f"Error in get_gold_price_per_gram: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/gold/karat/<int:karat>')
def get_gold_price_by_karat(karat):
    """Get gold price for specific karat"""
    try:
        if karat not in [10, 14, 16, 18, 20, 21, 22, 24]:
            return jsonify({
                'success': False,
                'error': 'Invalid karat. Supported values: 10, 14, 16, 18, 20, 21, 22, 24'
            }), 400
        
        data = gold_api.fetch_gold_price()
        price_per_gram = data['price_per_oz'] / 31.1035
        
        # Calculate price based on karat purity
        purity = karat / 24
        karat_price = price_per_gram * purity
        
        return jsonify({
            'success': True,
            'data': {
                'karat': karat,
                'purity_percentage': round(purity * 100, 2),
                'price_per_gram': round(karat_price, 2),
                'base_price_per_oz': data['price_per_oz'],
                'timestamp': data['timestamp'],
                'source': data['source']
            },
            'unit': f'USD per Gram ({karat}K Gold)'
        })
    except Exception as e:
        logger.error(f"Error in get_gold_price_by_karat: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/gold/formats')
def get_gold_prices_all_formats():
    """Get gold prices in multiple formats"""
    try:
        data = gold_api.fetch_gold_price()
        price_per_oz = data['price_per_oz']
        price_per_gram = price_per_oz / 31.1035
        
        formats = {
            'troy_ounce': {
                'price': price_per_oz,
                'unit': 'USD per Troy Ounce',
                'description': 'Standard international trading unit'
            },
            'gram': {
                'price': round(price_per_gram, 2),
                'unit': 'USD per Gram',
                'description': 'Common jewelry market unit'
            },
            'karat_prices': {}
        }
        
        # Calculate prices for different karats
        for karat in [24, 22, 21, 20, 18, 16, 14, 10]:
            purity = karat / 24
            karat_price = price_per_gram * purity
            formats['karat_prices'][f'{karat}k'] = {
                'price': round(karat_price, 2),
                'unit': f'USD per Gram ({karat}K)',
                'purity': f'{round(purity * 100, 2)}%'
            }
        
        return jsonify({
            'success': True,
            'data': formats,
            'metadata': {
                'timestamp': data['timestamp'],
                'source': data['source'],
                'last_updated': datetime.now().isoformat()
            }
        })
    except Exception as e:
        logger.error(f"Error in get_gold_prices_all_formats: {e}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'version': '1.0.0'
    })

if __name__ == '__main__':
    print("🏆 Gold Rate API Server Starting...")
    print("📊 Available endpoints:")
    print("  - GET /                     - API documentation")
    print("  - GET /api/gold/current     - Current gold price per oz")
    print("  - GET /api/gold/gram        - Current gold price per gram")
    print("  - GET /api/gold/karat/<k>   - Gold price for specific karat")
    print("  - GET /api/gold/formats     - All gold price formats")
    print("  - GET /api/health           - Health check")
    print("\n🚀 Server running on http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
