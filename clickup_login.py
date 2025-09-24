#!/usr/bin/env python3
"""
Simple ClickUp Login Program
This program demonstrates how to authenticate with ClickUp API using an API token.
"""

import requests
import json
import os
from typing import Optional, Dict, Any


class ClickUpLogin:
    """Simple ClickUp authentication and basic API interaction class."""
    
    def __init__(self, api_token: Optional[str] = None):
        """
        Initialize ClickUp client with API token.
        
        Args:
            api_token: ClickUp API token. If not provided, will try to get from environment.
        """
        self.api_token = api_token or os.getenv('CLICKUP_API_TOKEN')
        self.base_url = 'https://api.clickup.com/api/v2'
        self.headers = {
            'Authorization': f'{self.api_token}',
            'Content-Type': 'application/json'
        }
        self.user_info = None
    
    def login(self) -> bool:
        """
        Authenticate with ClickUp API and retrieve user information.
        
        Returns:
            bool: True if login successful, False otherwise
        """
        if not self.api_token:
            print("❌ Error: No API token provided. Please set CLICKUP_API_TOKEN environment variable or pass token directly.")
            return False
        
        try:
            print("🔐 Attempting to login to ClickUp...")
            
            # Test authentication by getting user info
            response = requests.get(
                f'{self.base_url}/user',
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                self.user_info = response.json()['user']
                print(f"✅ Login successful! Welcome, {self.user_info['username']}!")
                print(f"📧 Email: {self.user_info['email']}")
                print(f"🆔 User ID: {self.user_info['id']}")
                return True
            else:
                print(f"❌ Login failed: {response.status_code} - {response.text}")
                return False
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Network error during login: {e}")
            return False
        except Exception as e:
            print(f"❌ Unexpected error during login: {e}")
            return False
    
    def get_workspaces(self) -> Optional[list]:
        """
        Get list of workspaces (teams) the user has access to.
        
        Returns:
            list: List of workspaces or None if error
        """
        if not self.user_info:
            print("❌ Please login first!")
            return None
        
        try:
            print("📋 Fetching workspaces...")
            response = requests.get(
                f'{self.base_url}/team',
                headers=self.headers,
                timeout=10
            )
            
            if response.status_code == 200:
                workspaces = response.json()['teams']
                print(f"✅ Found {len(workspaces)} workspace(s):")
                for workspace in workspaces:
                    print(f"  • {workspace['name']} (ID: {workspace['id']})")
                return workspaces
            else:
                print(f"❌ Failed to fetch workspaces: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error fetching workspaces: {e}")
            return None
    
    def logout(self):
        """Clean up session data."""
        print("👋 Logging out...")
        self.user_info = None
        print("✅ Logged out successfully!")


def main():
    """Main function to demonstrate ClickUp login."""
    print("🚀 ClickUp Login Program")
    print("=" * 30)
    
    # Option 1: Use environment variable
    clickup = ClickUpLogin()
    
    # Option 2: Prompt for API token if not in environment
    if not clickup.api_token:
        print("\n📝 ClickUp API Token not found in environment.")
        print("You can get your API token from: https://app.clickup.com/settings/apps")
        api_token = input("Please enter your ClickUp API token: ").strip()
        clickup = ClickUpLogin(api_token)
    
    # Attempt login
    if clickup.login():
        print("\n" + "=" * 30)
        
        # Get workspaces
        workspaces = clickup.get_workspaces()
        
        if workspaces:
            print(f"\n🎉 Successfully connected to ClickUp!")
            print(f"You have access to {len(workspaces)} workspace(s).")
        
        # Logout
        print("\n" + "=" * 30)
        clickup.logout()
    else:
        print("\n❌ Login failed. Please check your API token and try again.")
        print("💡 Make sure your token has the necessary permissions.")


if __name__ == "__main__":
    main()
