# ClickUp Login Program

A simple Python program that demonstrates how to authenticate with the ClickUp API and perform basic operations.

## Features

- 🔐 Secure authentication with ClickUp API using API tokens
- 👤 User information retrieval
- 🏢 Workspace/team listing
- 🛡️ Error handling and validation
- 📝 Clean, documented code with type hints

## Files

- `clickup_login.py` - Main program with ClickUpLogin class
- `example_usage.py` - Usage examples
- `requirements.txt` - Python dependencies

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Get your ClickUp API token:**
   - Go to [ClickUp Settings > Apps](https://app.clickup.com/settings/apps)
   - Generate a new API token
   - Copy the token for use in the program

3. **Set up authentication (choose one method):**

   **Method 1: Environment Variable (Recommended)**
   ```bash
   export CLICKUP_API_TOKEN="your_token_here"
   ```

   **Method 2: Direct token input**
   - The program will prompt you for the token if not found in environment

## Usage

### Basic Usage
```bash
python clickup_login.py
```

### Programmatic Usage
```python
from clickup_login import ClickUpLogin

# Using environment variable
clickup = ClickUpLogin()

# Or passing token directly
clickup = ClickUpLogin("your_api_token_here")

# Login and get user info
if clickup.login():
    print("Login successful!")
    
    # Get workspaces
    workspaces = clickup.get_workspaces()
    
    # Logout
    clickup.logout()
```

### Run Examples
```bash
python example_usage.py
```

## API Token Permissions

Make sure your ClickUp API token has the following permissions:
- Read user information
- Read workspace/team information

## Security Notes

- Never commit your API token to version control
- Use environment variables for production deployments
- Rotate your API tokens regularly
- Keep your tokens secure and don't share them

## Error Handling

The program includes comprehensive error handling for:
- Missing or invalid API tokens
- Network connectivity issues
- API rate limiting
- Invalid responses

## Sample Output

```
🚀 ClickUp Login Program
==============================
🔐 Attempting to login to ClickUp...
✅ Login successful! Welcome, john_doe!
📧 Email: john@example.com
🆔 User ID: 12345678

==============================
📋 Fetching workspaces...
✅ Found 2 workspace(s):
  • My Workspace (ID: 987654321)
  • Team Project (ID: 123456789)

🎉 Successfully connected to ClickUp!
You have access to 2 workspace(s).

==============================
👋 Logging out...
✅ Logged out successfully!
```

## Requirements

- Python 3.6+
- requests library
- Valid ClickUp API token

## License

This project is open source and available under the MIT License.
