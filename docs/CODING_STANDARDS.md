# 🎨 Coding Standards

This document outlines the coding standards and best practices for the Fresh project. Following these guidelines ensures consistency, maintainability, and quality across our codebase.

## 📋 General Principles

### Code Quality
- **Readability**: Write code that tells a story
- **Simplicity**: Prefer simple solutions over complex ones
- **Consistency**: Follow established patterns in the codebase
- **Maintainability**: Write code that's easy to modify and extend

### SOLID Principles
- **S**ingle Responsibility Principle
- **O**pen/Closed Principle
- **L**iskov Substitution Principle
- **I**nterface Segregation Principle
- **D**ependency Inversion Principle

## 🔧 Code Formatting

We use automated tools to maintain consistent formatting:

### ESLint Configuration
```json
{
  "extends": [
    "eslint:recommended",
    "@typescript-eslint/recommended",
    "prettier"
  ],
  "rules": {
    "no-console": "warn",
    "no-unused-vars": "error",
    "prefer-const": "error",
    "no-var": "error"
  }
}
```

### Prettier Configuration
```json
{
  "semi": true,
  "trailingComma": "es5",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false
}
```

## 📝 Naming Conventions

### Variables and Functions
```javascript
// ✅ Good - camelCase
const userName = 'john_doe';
const calculateTotalPrice = (items) => { /* ... */ };

// ❌ Bad
const user_name = 'john_doe';
const calculate_total_price = (items) => { /* ... */ };
```

### Constants
```javascript
// ✅ Good - SCREAMING_SNAKE_CASE
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = 'https://api.example.com';

// ❌ Bad
const maxRetryAttempts = 3;
const apiBaseUrl = 'https://api.example.com';
```

### Classes
```javascript
// ✅ Good - PascalCase
class UserService {
  constructor() { /* ... */ }
}

class DatabaseConnection {
  connect() { /* ... */ }
}

// ❌ Bad
class userService { /* ... */ }
class database_connection { /* ... */ }
```

### Files and Directories
```
// ✅ Good - kebab-case for files
user-service.js
database-connection.js
api-routes.js

// ✅ Good - camelCase for directories
src/
  userManagement/
  apiRoutes/
  utils/

// ❌ Bad
UserService.js
database_connection.js
```

## 🏗️ Code Structure

### Function Guidelines
```javascript
// ✅ Good - Small, focused functions
const validateEmail = (email) => {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
};

const createUser = async (userData) => {
  if (!validateEmail(userData.email)) {
    throw new Error('Invalid email format');
  }
  
  return await userRepository.create(userData);
};

// ❌ Bad - Large, multi-purpose function
const processUser = async (userData) => {
  // Email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(userData.email)) {
    throw new Error('Invalid email format');
  }
  
  // Password hashing
  const hashedPassword = await bcrypt.hash(userData.password, 10);
  
  // Database operations
  const user = await userRepository.create({
    ...userData,
    password: hashedPassword
  });
  
  // Send welcome email
  await emailService.sendWelcomeEmail(user.email);
  
  // Log user creation
  logger.info(`User created: ${user.id}`);
  
  return user;
};
```

### Error Handling
```javascript
// ✅ Good - Explicit error handling
const fetchUserData = async (userId) => {
  try {
    const user = await userRepository.findById(userId);
    
    if (!user) {
      throw new NotFoundError(`User with ID ${userId} not found`);
    }
    
    return user;
  } catch (error) {
    logger.error('Failed to fetch user data', { userId, error });
    throw error;
  }
};

// ❌ Bad - Silent failures
const fetchUserData = async (userId) => {
  const user = await userRepository.findById(userId);
  return user || {};
};
```

### Async/Await vs Promises
```javascript
// ✅ Good - Use async/await
const processData = async () => {
  try {
    const data = await fetchData();
    const processed = await transformData(data);
    return await saveData(processed);
  } catch (error) {
    logger.error('Data processing failed', error);
    throw error;
  }
};

// ❌ Bad - Promise chains (when async/await is clearer)
const processData = () => {
  return fetchData()
    .then(data => transformData(data))
    .then(processed => saveData(processed))
    .catch(error => {
      logger.error('Data processing failed', error);
      throw error;
    });
};
```

## 📚 Documentation

### JSDoc Comments
```javascript
/**
 * Calculates the total price including tax
 * @param {number} basePrice - The base price before tax
 * @param {number} taxRate - The tax rate as a decimal (e.g., 0.08 for 8%)
 * @returns {number} The total price including tax
 * @throws {Error} When basePrice or taxRate is negative
 */
const calculateTotalPrice = (basePrice, taxRate) => {
  if (basePrice < 0 || taxRate < 0) {
    throw new Error('Price and tax rate must be non-negative');
  }
  
  return basePrice * (1 + taxRate);
};
```

### Inline Comments
```javascript
// ✅ Good - Explain why, not what
const retryAttempts = 3; // API can be flaky, retry up to 3 times

// Complex business logic explanation
if (user.subscriptionType === 'premium' && user.accountAge > 365) {
  // Premium users with accounts older than 1 year get additional features
  enableAdvancedFeatures(user);
}

// ❌ Bad - Obvious comments
const userName = 'john'; // Set userName to 'john'
i++; // Increment i
```

## 🧪 Testing Standards

### Test Structure
```javascript
// ✅ Good - Clear test structure
describe('UserService', () => {
  describe('createUser', () => {
    it('should create a user with valid data', async () => {
      // Arrange
      const userData = {
        email: 'test@example.com',
        name: 'Test User'
      };
      
      // Act
      const result = await userService.createUser(userData);
      
      // Assert
      expect(result).toHaveProperty('id');
      expect(result.email).toBe(userData.email);
    });
    
    it('should throw error for invalid email', async () => {
      // Arrange
      const userData = {
        email: 'invalid-email',
        name: 'Test User'
      };
      
      // Act & Assert
      await expect(userService.createUser(userData))
        .rejects
        .toThrow('Invalid email format');
    });
  });
});
```

### Test Naming
```javascript
// ✅ Good - Descriptive test names
it('should return 404 when user does not exist')
it('should hash password before saving to database')
it('should send welcome email after successful registration')

// ❌ Bad - Vague test names
it('should work')
it('should test user creation')
it('should handle errors')
```

## 🔒 Security Best Practices

### Input Validation
```javascript
// ✅ Good - Validate and sanitize input
const createUser = async (userData) => {
  const schema = Joi.object({
    email: Joi.string().email().required(),
    name: Joi.string().min(2).max(50).required(),
    age: Joi.number().integer().min(13).max(120)
  });
  
  const { error, value } = schema.validate(userData);
  if (error) {
    throw new ValidationError(error.details[0].message);
  }
  
  return await userRepository.create(value);
};

// ❌ Bad - No validation
const createUser = async (userData) => {
  return await userRepository.create(userData);
};
```

### Environment Variables
```javascript
// ✅ Good - Use environment variables for sensitive data
const dbConfig = {
  host: process.env.DB_HOST,
  password: process.env.DB_PASSWORD,
  ssl: process.env.NODE_ENV === 'production'
};

// ❌ Bad - Hardcoded sensitive data
const dbConfig = {
  host: 'localhost',
  password: 'mypassword123',
  ssl: false
};
```

## 📊 Performance Guidelines

### Database Queries
```javascript
// ✅ Good - Efficient queries
const getUsersWithPosts = async (limit = 10) => {
  return await User.findAll({
    include: [{ model: Post, limit: 5 }],
    limit,
    order: [['createdAt', 'DESC']]
  });
};

// ❌ Bad - N+1 query problem
const getUsersWithPosts = async () => {
  const users = await User.findAll();
  
  for (const user of users) {
    user.posts = await Post.findAll({ where: { userId: user.id } });
  }
  
  return users;
};
```

### Memory Management
```javascript
// ✅ Good - Process large datasets in chunks
const processLargeDataset = async (data) => {
  const chunkSize = 1000;
  
  for (let i = 0; i < data.length; i += chunkSize) {
    const chunk = data.slice(i, i + chunkSize);
    await processChunk(chunk);
  }
};

// ❌ Bad - Process everything at once
const processLargeDataset = async (data) => {
  return await Promise.all(data.map(item => processItem(item)));
};
```

## 🔍 Code Review Checklist

Before submitting code for review:

- [ ] Code follows naming conventions
- [ ] Functions are small and focused
- [ ] Error handling is implemented
- [ ] Tests are written and passing
- [ ] Documentation is updated
- [ ] No hardcoded values or secrets
- [ ] Performance considerations addressed
- [ ] Security best practices followed

## 🚫 Common Anti-Patterns to Avoid

### Magic Numbers
```javascript
// ✅ Good
const MAX_LOGIN_ATTEMPTS = 5;
const CACHE_EXPIRY_HOURS = 24;

if (loginAttempts > MAX_LOGIN_ATTEMPTS) {
  lockAccount();
}

// ❌ Bad
if (loginAttempts > 5) {
  lockAccount();
}
```

### Deep Nesting
```javascript
// ✅ Good - Early returns
const processUser = (user) => {
  if (!user) {
    return null;
  }
  
  if (!user.isActive) {
    return { error: 'User is inactive' };
  }
  
  if (!user.hasPermission) {
    return { error: 'Insufficient permissions' };
  }
  
  return processActiveUser(user);
};

// ❌ Bad - Deep nesting
const processUser = (user) => {
  if (user) {
    if (user.isActive) {
      if (user.hasPermission) {
        return processActiveUser(user);
      } else {
        return { error: 'Insufficient permissions' };
      }
    } else {
      return { error: 'User is inactive' };
    }
  } else {
    return null;
  }
};
```

## 🛠️ Tools and Automation

### Pre-commit Hooks
```json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "pre-push": "npm test"
    }
  },
  "lint-staged": {
    "*.{js,ts}": [
      "eslint --fix",
      "prettier --write",
      "git add"
    ]
  }
}
```

### VS Code Settings
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": true
  },
  "javascript.preferences.quoteStyle": "single",
  "typescript.preferences.quoteStyle": "single"
}
```

## 📈 Continuous Improvement

- Regularly review and update coding standards
- Learn from code reviews and team feedback
- Stay updated with industry best practices
- Contribute to improving team processes

---

*Remember: These standards are guidelines to help us write better code together. When in doubt, prioritize readability and maintainability over strict adherence to rules.*
