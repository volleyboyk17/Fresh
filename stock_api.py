#!/usr/bin/env python3
"""
Indian Stock Market API
Flask-based REST API for Indian stock market data
"""

from flask import Flask, jsonify, request
from indian_stock_market import IndianStockMarket
import json

app = Flask(__name__)
market = IndianStockMarket()

@app.route('/')
def home():
    """Home endpoint with API documentation"""
    return jsonify({
        "message": "Indian Stock Market API",
        "endpoints": {
            "/api/indices": "Get all major Indian stock market indices",
            "/api/stocks": "Get popular Indian stocks",
            "/api/stock/<symbol>": "Get specific stock data",
            "/api/search?q=<query>": "Search for a stock",
            "/api/summary": "Get market summary"
        },
        "example_symbols": [
            "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS"
        ]
    })

@app.route('/api/indices')
def get_indices():
    """Get all major Indian stock market indices"""
    try:
        indices_data = {}
        for name, symbol in market.indices.items():
            data = market.fetch_stock_data(symbol)
            if data:
                indices_data[name] = data
        
        return jsonify({
            "status": "success",
            "market_status": market.get_market_status(),
            "data": indices_data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/stocks')
def get_popular_stocks():
    """Get popular Indian stocks"""
    try:
        stocks_data = {}
        for name, symbol in market.popular_stocks.items():
            data = market.fetch_stock_data(symbol)
            if data:
                stocks_data[name] = data
        
        return jsonify({
            "status": "success",
            "data": stocks_data
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/stock/<symbol>')
def get_stock(symbol):
    """Get specific stock data"""
    try:
        data = market.fetch_stock_data(symbol)
        if data:
            return jsonify({
                "status": "success",
                "data": data
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Stock not found or data unavailable"
            }), 404
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/search')
def search_stock():
    """Search for a stock"""
    try:
        query = request.args.get('q', '')
        if not query:
            return jsonify({
                "status": "error",
                "message": "Query parameter 'q' is required"
            }), 400
        
        data = market.search_stock(query)
        if data:
            return jsonify({
                "status": "success",
                "query": query,
                "data": data
            })
        else:
            return jsonify({
                "status": "error",
                "message": "Stock not found or data unavailable"
            }), 404
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/api/summary')
def get_market_summary():
    """Get market summary"""
    try:
        summary = market.get_market_summary()
        return jsonify({
            "status": "success",
            "data": summary
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "status": "error",
        "message": "Endpoint not found"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "status": "error",
        "message": "Internal server error"
    }), 500

if __name__ == '__main__':
    print("🚀 Starting Indian Stock Market API...")
    print("📊 Available endpoints:")
    print("  - GET /api/indices - Major market indices")
    print("  - GET /api/stocks - Popular stocks")
    print("  - GET /api/stock/<symbol> - Specific stock data")
    print("  - GET /api/search?q=<query> - Search stocks")
    print("  - GET /api/summary - Market summary")
    print("\n🌐 Server running on http://localhost:5000")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
