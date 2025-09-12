# Contributing to Fresh

Thank you for your interest in contributing to Fresh! This document provides guidelines and information for contributors.

## 🤝 Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors. Please be respectful and professional in all interactions.

## 🚀 Getting Started

1. **Fork the repository** and clone it locally
2. **Set up your development environment** following the [Development Setup Guide](docs/DEVELOPMENT_SETUP.md)
3. **Create a new branch** for your feature or bug fix
4. **Make your changes** following our coding standards
5. **Test your changes** thoroughly
6. **Submit a pull request** with a clear description

## 🌿 Branching Strategy

We use a feature branch workflow:

- `master` - Main branch, always deployable
- `feature/your-feature-name` - Feature branches
- `bugfix/issue-description` - Bug fix branches
- `hotfix/critical-fix` - Critical production fixes

### Branch Naming Convention
- `feature/add-user-authentication`
- `bugfix/fix-login-validation`
- `hotfix/security-patch`
- `docs/update-readme`

## 📝 Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Types
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools

### Examples
```
feat: add user authentication system
fix: resolve login validation issue
docs: update API documentation
refactor: simplify user service logic
```

## 🔍 Code Review Process

1. **All changes** must go through a pull request
2. **At least one approval** is required from a team member
3. **All checks must pass** (linting, tests, etc.)
4. **Address feedback** promptly and professionally
5. **Squash commits** when merging (if requested)

## 🧪 Testing

- Write tests for new features and bug fixes
- Ensure all existing tests pass
- Aim for good test coverage
- Include both unit and integration tests where appropriate

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Code follows our style guidelines
- [ ] Self-review of the code
- [ ] Tests added/updated as needed
- [ ] Documentation updated if necessary
- [ ] No merge conflicts with master

### PR Description Template
```markdown
## Description
Brief description of the changes

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new functionality

## Screenshots (if applicable)
Add screenshots to help explain your changes

## Additional Notes
Any additional information or context
```

## 🎨 Code Style

We use automated tools to maintain consistent code style:

- **ESLint** for JavaScript linting
- **Prettier** for code formatting
- **Husky** for pre-commit hooks

### Key Guidelines
- Use meaningful variable and function names
- Write clear, concise comments
- Follow the existing code structure and patterns
- Keep functions small and focused
- Use async/await instead of callbacks

## 🐛 Reporting Issues

When reporting issues, please include:

1. **Clear description** of the problem
2. **Steps to reproduce** the issue
3. **Expected behavior** vs actual behavior
4. **Environment details** (OS, Node.js version, etc.)
5. **Screenshots or error messages** if applicable

Use our issue templates when available.

## 💡 Suggesting Features

We welcome feature suggestions! Please:

1. **Check existing issues** to avoid duplicates
2. **Provide clear use cases** for the feature
3. **Consider the impact** on existing functionality
4. **Be open to discussion** and feedback

## 📚 Documentation

- Update documentation for any new features
- Keep README.md current
- Add inline comments for complex logic
- Update API documentation if applicable

## 🏷️ Versioning

We use [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality
- **PATCH** version for backwards-compatible bug fixes

## 🎉 Recognition

Contributors will be recognized in:
- Release notes for significant contributions
- Contributors section (coming soon)
- Special thanks in project documentation

## ❓ Questions?

If you have questions about contributing:
- Check existing documentation
- Ask in team chat or discussions
- Reach out to project maintainers
- Create an issue for clarification

## 📄 License

By contributing to Fresh, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to Fresh! 🚀
