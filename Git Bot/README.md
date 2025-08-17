# Git Bot Agent 🤖

An intelligent Git bot that creates meaningful commits to maintain an active GitHub profile with a green contribution graph.

## Features ✨

- **Smart Commit Generation**: Creates realistic commit messages following conventional commit standards
- **Meaningful Changes**: Generates actual code changes, documentation updates, and configuration improvements
- **Automated Scheduling**: Runs automatically at scheduled times to maintain daily activity
- **Configurable**: Easy to customize commit types, timing, and content
- **Safe Operation**: Checks for existing commits to avoid duplicates
- **Comprehensive Logging**: Detailed logs for monitoring and debugging

## What It Does 🎯

The Git Bot creates realistic commits by:

1. **Updating Documentation**: README files, API docs, contributing guidelines
2. **Improving Code**: Adding utility functions, components, and tests
3. **Enhancing Configuration**: Package.json scripts, TypeScript config, ESLint rules
4. **Adding Styles**: CSS files with modern styling and animations
5. **Creating Tests**: Unit tests and integration tests
6. **Refactoring**: Code improvements and optimizations

## Installation 🚀

### Prerequisites

- Python 3.7+
- Git repository
- Git user configured

### Quick Setup

1. **Navigate to the Git Bot directory:**
   ```bash
   cd "Git Bot"
   ```

2. **Run the setup script:**
   ```bash
   python3 setup.py
   ```

3. **Start the bot:**
   ```bash
   ./launch_git_bot.sh
   ```

### Manual Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Make scripts executable:**
   ```bash
   chmod +x git_bot.py scheduler.py
   ```

3. **Configure Git (if not already done):**
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

## Usage 📖

### Starting the Bot

```bash
# Option 1: Use the launch script
./launch_git_bot.sh

# Option 2: Run directly
python3 scheduler.py

# Option 3: Run once manually
python3 git_bot.py
```

### Configuration

Edit `config.json` to customize the bot behavior:

```json
{
  "schedule": {
    "daily_time": "14:30",
    "weekday_time": "10:00"
  },
  "commit_settings": {
    "max_commits_per_day": 1,
    "preferred_commit_types": ["feat", "fix", "docs", "refactor"]
  }
}
```

### Schedule

The bot runs:
- **Daily at 14:30** (main commit)
- **Weekdays at 10:00** (backup commit)
- **Immediately** when started (test run)

## Commit Types 📝

The bot generates commits using these types:

- **feat**: New features and functionality
- **fix**: Bug fixes and issue resolutions
- **docs**: Documentation updates
- **style**: Code formatting and style changes
- **refactor**: Code improvements and restructuring
- **test**: Test additions and improvements
- **chore**: Maintenance tasks and updates
- **perf**: Performance improvements
- **ci**: CI/CD configuration changes
- **build**: Build system changes

## Example Commits 🎨

```
feat(ui): add user authentication system
fix(api): resolve memory leak in data processing
docs(components): update API documentation
refactor(utils): improve error handling
test(auth): add integration tests for authentication
chore(deps): update dependencies for security patches
```

## File Changes 📁

The bot creates and updates various file types:

### Documentation
- `README.md` - Project overview and updates
- `docs/API.md` - API documentation
- `docs/DEPLOYMENT.md` - Deployment guide
- `docs/CONTRIBUTING.md` - Contributing guidelines

### Code Files
- `lib/helpers.ts` - Utility functions
- `lib/validation.ts` - Validation utilities
- `components/Button.tsx` - React components
- `__tests__/utils.test.ts` - Test files

### Configuration
- `package.json` - New scripts and dependencies
- `tsconfig.json` - TypeScript configuration
- `.eslintrc.json` - ESLint rules
- `next.config.ts` - Next.js configuration

### Styles
- `styles/components.css` - Component styles
- `styles/animations.css` - Animation keyframes
- `styles/themes.css` - Theme definitions

## Safety Features 🛡️

- **Duplicate Prevention**: Checks if a commit was already made today
- **Error Handling**: Graceful handling of Git errors and network issues
- **Logging**: Comprehensive logging for monitoring and debugging
- **Safe Operations**: Only modifies files in the repository
- **Configurable Limits**: Prevents excessive commits

## Monitoring 📊

### Logs

The bot creates detailed logs in `git_bot.log`:

```
2024-01-15 14:30:01 - INFO - Starting Git Bot Scheduler...
2024-01-15 14:30:02 - INFO - Running initial test...
2024-01-15 14:30:03 - INFO - Successfully committed: feat(ui): add responsive design
2024-01-15 14:30:04 - INFO - Successfully pushed changes to remote
```

### GitHub Activity

Monitor your GitHub profile to see the green contribution graph:

- Daily commits will appear as green squares
- Commit messages will be realistic and meaningful
- Code changes will be actual improvements

## Customization ⚙️

### Adding Custom Content

Edit the GitBot class in `git_bot.py` to add:

- New commit message templates
- Additional file types to modify
- Custom project-specific content
- Different scheduling logic

### Project-Specific Configuration

Update `config.json` with your project details:

```json
{
  "content": {
    "project_name": "Your Project",
    "project_description": "Your project description",
    "tech_stack": ["React", "Node.js", "MongoDB"],
    "features": ["Feature 1", "Feature 2", "Feature 3"]
  }
}
```

## Troubleshooting 🔧

### Common Issues

1. **"Not in a git repository"**
   - Ensure you're running from a Git repository
   - Run `git init` if needed

2. **"Git user not configured"**
   - Set your Git user: `git config --global user.name "Your Name"`
   - Set your email: `git config --global user.email "your.email@example.com"`

3. **"Permission denied"**
   - Make scripts executable: `chmod +x *.py *.sh`

4. **"Module not found"**
   - Install requirements: `pip install -r requirements.txt`

### Debug Mode

Run with verbose logging:

```bash
python3 -u git_bot.py 2>&1 | tee debug.log
```

## Best Practices 💡

1. **Review Commits**: Occasionally review the commits to ensure they're appropriate
2. **Customize Content**: Update the bot to match your project's actual needs
3. **Monitor Logs**: Check logs regularly for any issues
4. **Backup**: Keep a backup of your repository before running the bot
5. **Test First**: Run the bot manually first to see what it does

## Ethical Considerations 🤔

- **Transparency**: Be honest about using automated commits
- **Quality**: Ensure the bot creates meaningful, useful changes
- **Learning**: Use this as a tool to learn Git and development practices
- **Contribution**: Consider contributing to open source projects instead

## License 📄

This project is for educational purposes. Use responsibly and ethically.

## Support 💬

If you encounter issues:

1. Check the logs in `git_bot.log`
2. Review the troubleshooting section
3. Ensure your Git configuration is correct
4. Verify you're in a Git repository

---

**Remember**: This bot is designed to help maintain an active GitHub profile while creating meaningful contributions. Use it responsibly and consider it a learning tool for Git and development practices. 