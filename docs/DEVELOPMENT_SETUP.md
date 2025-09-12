# 🛠️ Development Environment Setup

This guide will help you set up your development environment for the Fresh project.

## 📋 Prerequisites

### Required Software

#### Node.js
- **Version**: 18.x or higher (LTS recommended)
- **Download**: [nodejs.org](https://nodejs.org/)
- **Verify installation**: `node --version && npm --version`

#### Git
- **Version**: 2.x or higher
- **Download**: [git-scm.com](https://git-scm.com/)
- **Verify installation**: `git --version`

#### Code Editor (Recommended: VS Code)
- **Download**: [Visual Studio Code](https://code.visualstudio.com/)
- **Alternative editors**: WebStorm, Sublime Text, Vim, etc.

## 🚀 Quick Setup

### 1. Clone the Repository
```bash
git clone https://github.com/volleyboyk17/Fresh.git
cd Fresh
```

### 2. Install Dependencies
```bash
# Using npm
npm install

# Or using yarn (if preferred)
yarn install
```

### 3. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit the .env file with your local settings
# (Add your editor command here, e.g., code .env)
```

### 4. Verify Setup
```bash
# Run the development server
npm run dev

# Run tests
npm test

# Run linting
npm run lint
```

## 🔧 Detailed Setup Instructions

### Node.js Version Management

We recommend using a Node.js version manager for consistency:

#### Using nvm (macOS/Linux)
```bash
# Install nvm
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash

# Restart terminal or source your profile
source ~/.bashrc

# Install and use the project's Node.js version
nvm install 18
nvm use 18
nvm alias default 18
```

#### Using nvm-windows (Windows)
```bash
# Download and install from: https://github.com/coreybutler/nvm-windows
# Then run:
nvm install 18.17.0
nvm use 18.17.0
```

### VS Code Setup

#### Recommended Extensions
Install these extensions for the best development experience:

```json
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "dbaeumer.vscode-eslint",
    "bradlc.vscode-tailwindcss",
    "ms-vscode.vscode-json",
    "christian-kohler.path-intellisense",
    "formulahendry.auto-rename-tag",
    "ms-vscode.vscode-typescript-next"
  ]
}
```

#### VS Code Settings
Create `.vscode/settings.json` in your project root:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "files.associations": {
    "*.env*": "dotenv"
  }
}
```

### Package Manager Configuration

#### npm Configuration
```bash
# Set npm registry (if using private registry)
npm config set registry https://registry.npmjs.org/

# Configure npm for faster installs
npm config set prefer-offline true
npm config set cache-max 86400000
```

#### Yarn Configuration (Optional)
```bash
# Install yarn globally
npm install -g yarn

# Verify installation
yarn --version
```

## 🌍 Environment Variables

### Required Environment Variables

Create a `.env` file in the project root:

```bash
# Application
NODE_ENV=development
PORT=3000

# Database (when implemented)
# DATABASE_URL=postgresql://username:password@localhost:5432/fresh_dev

# API Keys (when needed)
# API_KEY=your_api_key_here

# Other configuration
LOG_LEVEL=debug
```

### Environment Files Structure
```
.env                # Default environment variables
.env.local          # Local overrides (git-ignored)
.env.development    # Development-specific variables
.env.test           # Test environment variables
.env.production     # Production variables (never commit sensitive data)
```

## 🧪 Development Tools

### Available Scripts

```bash
# Development
npm run dev          # Start development server with hot reload
npm run build        # Build for production
npm run start        # Start production server

# Testing
npm test             # Run all tests
npm run test:watch   # Run tests in watch mode
npm run test:coverage # Run tests with coverage report

# Code Quality
npm run lint         # Run ESLint
npm run lint:fix     # Fix ESLint issues automatically
npm run format       # Format code with Prettier
npm run type-check   # Run TypeScript type checking (if applicable)

# Database (when implemented)
npm run db:migrate   # Run database migrations
npm run db:seed      # Seed database with test data
npm run db:reset     # Reset database
```

### Git Hooks Setup

Pre-commit hooks are automatically installed with Husky:

```bash
# Hooks will run automatically on:
git commit    # Runs linting and formatting
git push      # Runs tests
```

## 🐛 Troubleshooting

### Common Issues

#### Node.js Version Mismatch
```bash
# Error: "The engine 'node' is incompatible with this module"
# Solution: Use the correct Node.js version
nvm use 18
```

#### Permission Issues (macOS/Linux)
```bash
# Error: EACCES permission denied
# Solution: Fix npm permissions
sudo chown -R $(whoami) ~/.npm
```

#### Port Already in Use
```bash
# Error: "Port 3000 is already in use"
# Solution: Kill the process or use a different port
lsof -ti:3000 | xargs kill -9
# Or set a different port in .env
PORT=3001
```

#### Module Not Found
```bash
# Error: "Cannot find module"
# Solution: Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Getting Help

If you encounter issues:

1. **Check the troubleshooting section** above
2. **Search existing issues** on GitHub
3. **Ask in team chat** or reach out to your mentor
4. **Create a new issue** with detailed information:
   - Operating system and version
   - Node.js and npm versions
   - Error messages and stack traces
   - Steps to reproduce

## 🔍 Verification Checklist

After setup, verify everything works:

- [ ] Node.js and npm are installed and correct versions
- [ ] Repository is cloned and dependencies installed
- [ ] Environment variables are configured
- [ ] Development server starts without errors
- [ ] Tests run successfully
- [ ] Linting passes without errors
- [ ] VS Code extensions are installed and working
- [ ] Git hooks are functioning

## 🚀 Next Steps

Once your environment is set up:

1. **Read the [Onboarding Guide](../ONBOARDING.md)** for your first tasks
2. **Review [Coding Standards](CODING_STANDARDS.md)** before making changes
3. **Check the [Contributing Guide](../CONTRIBUTING.md)** for workflow information
4. **Join team communication channels** and introduce yourself

Welcome to the Fresh development team! 🎉

---

*Last updated: [Current Date]*
*If you find any issues with this setup guide, please update it or create an issue.*
