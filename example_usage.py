#!/usr/bin/env python3
"""
Example usage of the ClickUp Login Program
"""

from clickup_login import ClickUpLogin
import os

def example_with_environment_variable():
    """Example using environment variable for API token."""
    print("Example 1: Using environment variable")
    print("-" * 40)
    
    # Set your API token as environment variable:
    # export CLICKUP_API_TOKEN="your_token_here"
    
    clickup = ClickUpLogin()
    
    if clickup.login():
        workspaces = clickup.get_workspaces()
        clickup.logout()
    else:
        print("Login failed - check your CLICKUP_API_TOKEN environment variable")

def example_with_direct_token():
    """Example passing API token directly."""
    print("\nExample 2: Passing token directly")
    print("-" * 40)
    
    # Replace with your actual API token
    api_token = "your_clickup_api_token_here"
    
    clickup = ClickUpLogin(api_token)
    
    if clickup.login():
        workspaces = clickup.get_workspaces()
        clickup.logout()
    else:
        print("Login failed - check your API token")

if __name__ == "__main__":
    print("🔧 ClickUp Login Examples")
    print("=" * 50)
    
    # Check if environment variable is set
    if os.getenv('CLICKUP_API_TOKEN'):
        example_with_environment_variable()
    else:
        print("💡 To run the environment variable example, set:")
        print("   export CLICKUP_API_TOKEN='your_token_here'")
        print("\n📝 For now, you can modify example_usage.py with your token")
        
    # Uncomment the line below and add your token to test
    # example_with_direct_token()
