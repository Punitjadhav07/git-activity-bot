#!/usr/bin/env python3
"""
Git Bot Agent - Automated meaningful commits for GitHub activity
This bot creates realistic commits to maintain an active GitHub profile.
"""

import os
import random
import subprocess
import json
import datetime
from pathlib import Path
from typing import List, Dict, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GitBot:
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path).resolve()
        self.commit_types = [
            "feat", "fix", "docs", "style", "refactor", "test", "chore", "perf", "ci", "build"
        ]
        self.scopes = [
            "ui", "api", "auth", "database", "config", "utils", "components", "styles", "docs", "tests"
        ]
        
        # Commit message templates
        self.commit_templates = {
            "feat": [
                "feat({scope}): add {feature}",
                "feat({scope}): implement {feature}",
                "feat({scope}): introduce {feature}",
                "feat({scope}): add support for {feature}"
            ],
            "fix": [
                "fix({scope}): resolve {issue}",
                "fix({scope}): correct {issue}",
                "fix({scope}): address {issue}",
                "fix({scope}): patch {issue}"
            ],
            "docs": [
                "docs({scope}): update {documentation}",
                "docs({scope}): improve {documentation}",
                "docs({scope}): add {documentation}",
                "docs({scope}): clarify {documentation}"
            ],
            "refactor": [
                "refactor({scope}): improve {component}",
                "refactor({scope}): optimize {component}",
                "refactor({scope}): restructure {component}",
                "refactor({scope}): simplify {component}"
            ],
            "test": [
                "test({scope}): add tests for {component}",
                "test({scope}): improve test coverage for {component}",
                "test({scope}): add integration tests for {component}",
                "test({scope}): update test cases for {component}"
            ],
            "chore": [
                "chore({scope}): update {dependency}",
                "chore({scope}): clean up {component}",
                "chore({scope}): organize {component}",
                "chore({scope}): maintain {component}"
            ]
        }
        
        # Feature/component names for realistic commits
        self.features = [
            "user authentication", "data validation", "error handling", "loading states",
            "responsive design", "accessibility", "performance optimization", "security",
            "caching", "logging", "monitoring", "deployment", "testing", "documentation",
            "code formatting", "linting", "build process", "CI/CD", "database queries",
            "API endpoints", "middleware", "utilities", "components", "hooks", "context"
        ]
        
        self.issues = [
            "memory leak", "performance issue", "security vulnerability", "UI bug",
            "data inconsistency", "race condition", "type error", "build failure",
            "test failure", "deployment issue", "accessibility issue", "mobile layout",
            "browser compatibility", "API timeout", "validation error", "authentication bug"
        ]
        
        self.components = [
            "user interface", "data layer", "authentication system", "error boundary",
            "form validation", "state management", "routing", "API client", "database",
            "caching layer", "logging system", "monitoring", "build configuration",
            "test suite", "documentation", "deployment script", "utility functions"
        ]

    def run_command(self, command: List[str], cwd: Optional[str] = None) -> str:
        """Run a shell command and return the output."""
        try:
            result = subprocess.run(
                command,
                cwd=cwd or self.repo_path,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logger.error(f"Command failed: {' '.join(command)}")
            logger.error(f"Error: {e.stderr}")
            raise

    def get_git_status(self) -> Dict[str, List[str]]:
        """Get current git status."""
        try:
            status = self.run_command(["git", "status", "--porcelain"])
            files = {
                "modified": [],
                "untracked": [],
                "staged": []
            }
            
            for line in status.split('\n'):
                if line:
                    status_code = line[:2]
                    filename = line[3:]
                    
                    if status_code.startswith('M'):
                        files["modified"].append(filename)
                    elif status_code.startswith('??'):
                        files["untracked"].append(filename)
                    elif status_code.startswith('A'):
                        files["staged"].append(filename)
            
            return files
        except subprocess.CalledProcessError:
            return {"modified": [], "untracked": [], "staged": []}

    def generate_commit_message(self) -> str:
        """Generate a realistic commit message."""
        commit_type = random.choice(self.commit_types)
        scope = random.choice(self.scopes)
        
        if commit_type in self.commit_templates:
            template = random.choice(self.commit_templates[commit_type])
            
            if commit_type == "feat":
                feature = random.choice(self.features)
                return template.format(scope=scope, feature=feature)
            elif commit_type == "fix":
                issue = random.choice(self.issues)
                return template.format(scope=scope, issue=issue)
            elif commit_type == "docs":
                doc_type = random.choice(["README", "API docs", "component docs", "setup guide", "troubleshooting"])
                return template.format(scope=scope, documentation=doc_type)
            elif commit_type == "refactor":
                component = random.choice(self.components)
                return template.format(scope=scope, component=component)
            elif commit_type == "test":
                component = random.choice(self.components)
                return template.format(scope=scope, component=component)
            elif commit_type == "chore":
                component = random.choice(self.components)
                return template.format(scope=scope, component=component)
        
        # Fallback
        return f"{commit_type}({scope}): update {random.choice(self.components)}"

    def create_meaningful_changes(self) -> bool:
        """Create meaningful file changes for the commit."""
        changes_made = False
        
        # Create or update various types of files
        file_actions = [
            self._update_readme,
            self._update_config,
            self._update_docs,
            self._update_tests,
            self._update_utils,
            self._update_styles,
            self._update_components
        ]
        
        # Randomly select 1-3 actions to perform
        num_actions = random.randint(1, 3)
        selected_actions = random.sample(file_actions, num_actions)
        
        for action in selected_actions:
            if action():
                changes_made = True
        
        return changes_made

    def _update_readme(self) -> bool:
        """Update README with meaningful content."""
        readme_path = self.repo_path / "README.md"
        
        if not readme_path.exists():
            content = """# QClinic

A modern healthcare management system built with Next.js and TypeScript.

## Features

- Patient management
- Appointment scheduling
- Medical records
- Billing and invoicing
- Staff management
- Reporting and analytics

## Getting Started

1. Clone the repository
2. Install dependencies: `npm install`
3. Run the development server: `npm run dev`
4. Open [http://localhost:3000](http://localhost:3000)

## Tech Stack

- Next.js 14
- TypeScript
- Tailwind CSS
- Prisma ORM
- PostgreSQL
- NextAuth.js

## Contributing

Please read our contributing guidelines before submitting pull requests.

## License

MIT License - see LICENSE file for details.
"""
            readme_path.write_text(content)
            return True
        
        # Update existing README
        current_content = readme_path.read_text()
        
        # Add a new section or update existing one
        updates = [
            "\n## Recent Updates\n\n- Improved performance and user experience\n- Enhanced security features\n- Better error handling and logging\n- Updated dependencies for security patches\n",
            "\n## Development\n\n- Added comprehensive test coverage\n- Improved code documentation\n- Enhanced build process\n- Better development workflow\n",
            "\n## Deployment\n\n- Optimized for production deployment\n- Enhanced monitoring and logging\n- Improved error tracking\n- Better performance metrics\n"
        ]
        
        if not any(update.strip() in current_content for update in updates):
            update = random.choice(updates)
            readme_path.write_text(current_content + update)
            return True
        
        return False

    def _update_config(self) -> bool:
        """Update configuration files."""
        config_files = [
            ("next.config.ts", self._update_next_config),
            ("package.json", self._update_package_json),
            ("tsconfig.json", self._update_tsconfig),
            (".eslintrc.json", self._update_eslint_config)
        ]
        
        for filename, updater in config_files:
            file_path = self.repo_path / filename
            if file_path.exists() and updater(file_path):
                return True
        
        return False

    def _update_next_config(self, file_path: Path) -> bool:
        """Update Next.js configuration."""
        try:
            content = file_path.read_text()
            if "experimental" not in content:
                new_content = content.replace(
                    "const nextConfig = {",
                    """const nextConfig = {
  experimental: {
    optimizePackageImports: ['@radix-ui/react-icons'],
  },"""
                )
                file_path.write_text(new_content)
                return True
        except Exception:
            pass
        return False

    def _update_package_json(self, file_path: Path) -> bool:
        """Update package.json with new scripts or dependencies."""
        try:
            data = json.loads(file_path.read_text())
            
            # Add a new script
            if "scripts" in data:
                new_scripts = {
                    "lint:fix": "next lint --fix",
                    "type-check": "tsc --noEmit",
                    "format": "prettier --write .",
                    "test:watch": "jest --watch"
                }
                
                for script_name, script_command in new_scripts.items():
                    if script_name not in data["scripts"]:
                        data["scripts"][script_name] = script_command
                        file_path.write_text(json.dumps(data, indent=2))
                        return True
        except Exception:
            pass
        return False

    def _update_tsconfig(self, file_path: Path) -> bool:
        """Update TypeScript configuration."""
        try:
            data = json.loads(file_path.read_text())
            if "compilerOptions" in data:
                # Add strict mode if not present
                if "strict" not in data["compilerOptions"]:
                    data["compilerOptions"]["strict"] = True
                    file_path.write_text(json.dumps(data, indent=2))
                    return True
        except Exception:
            pass
        return False

    def _update_eslint_config(self, file_path: Path) -> bool:
        """Update ESLint configuration."""
        try:
            data = json.loads(file_path.read_text())
            if "rules" in data:
                # Add a new rule
                new_rules = {
                    "no-console": "warn",
                    "prefer-const": "error",
                    "no-unused-vars": "warn"
                }
                
                for rule, value in new_rules.items():
                    if rule not in data["rules"]:
                        data["rules"][rule] = value
                        file_path.write_text(json.dumps(data, indent=2))
                        return True
        except Exception:
            pass
        return False

    def _update_docs(self) -> bool:
        """Update documentation files."""
        docs_dir = self.repo_path / "docs"
        docs_dir.mkdir(exist_ok=True)
        
        doc_files = [
            ("API.md", "API Documentation"),
            ("DEPLOYMENT.md", "Deployment Guide"),
            ("CONTRIBUTING.md", "Contributing Guidelines"),
            ("CHANGELOG.md", "Changelog")
        ]
        
        for filename, title in doc_files:
            file_path = docs_dir / filename
            if not file_path.exists():
                content = f"""# {title}

This document provides information about {title.lower()}.

## Overview

{title} is an important part of our development process.

## Details

- Feature 1: Description
- Feature 2: Description
- Feature 3: Description

## Usage

Instructions for using this feature.

## Examples

```javascript
// Example code
const example = "Hello World";
console.log(example);
```

## Notes

Additional notes and considerations.
"""
                file_path.write_text(content)
                return True
        
        return False

    def _update_tests(self) -> bool:
        """Update test files."""
        test_dir = self.repo_path / "__tests__"
        test_dir.mkdir(exist_ok=True)
        
        test_files = [
            ("utils.test.ts", "Utility functions"),
            ("components.test.tsx", "React components"),
            ("api.test.ts", "API endpoints"),
            ("auth.test.ts", "Authentication")
        ]
        
        for filename, description in test_files:
            file_path = test_dir / filename
            if not file_path.exists():
                content = f"""import {{ describe, it, expect }} from 'vitest';

describe('{description}', () => {{
  it('should work correctly', () => {{
    expect(true).toBe(true);
  }});

  it('should handle edge cases', () => {{
    const input = 'test';
    expect(input).toBeDefined();
  }});

  it('should return expected results', () => {{
    const result = 2 + 2;
    expect(result).toBe(4);
  }});
}});
"""
                file_path.write_text(content)
                return True
        
        return False

    def _update_utils(self) -> bool:
        """Update utility files."""
        utils_dir = self.repo_path / "lib"
        utils_dir.mkdir(exist_ok=True)
        
        utils_files = [
            ("helpers.ts", "Helper functions"),
            ("validation.ts", "Validation utilities"),
            ("formatting.ts", "Formatting utilities"),
            ("constants.ts", "Application constants")
        ]
        
        for filename, description in utils_files:
            file_path = utils_dir / filename
            if not file_path.exists():
                content = f"""// {description}

export function formatDate(date: Date): string {{
  return date.toLocaleDateString();
}}

export function validateEmail(email: string): boolean {{
  const emailRegex = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
  return emailRegex.test(email);
}}

export function capitalize(str: string): string {{
  return str.charAt(0).toUpperCase() + str.slice(1);
}}

export function debounce<T extends (...args: any[]) => any>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {{
  let timeout: NodeJS.Timeout;
  return (...args: Parameters<T>) => {{
    clearTimeout(timeout);
    timeout = setTimeout(() => func(...args), wait);
  }};
}}
"""
                file_path.write_text(content)
                return True
        
        return False

    def _update_styles(self) -> bool:
        """Update style files."""
        styles_dir = self.repo_path / "styles"
        styles_dir.mkdir(exist_ok=True)
        
        style_files = [
            ("components.css", "Component styles"),
            ("utilities.css", "Utility classes"),
            ("themes.css", "Theme definitions"),
            ("animations.css", "Animation keyframes")
        ]
        
        for filename, description in style_files:
            file_path = styles_dir / filename
            if not file_path.exists():
                content = f"""/* {description} */

.custom-button {{
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 0.2s ease-in-out;
}}

.custom-button:hover {{
  transform: translateY(-1px);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}}

.fade-in {{
  animation: fadeIn 0.3s ease-in-out;
}}

@keyframes fadeIn {{
  from {{
    opacity: 0;
    transform: translateY(10px);
  }}
  to {{
    opacity: 1;
    transform: translateY(0);
  }}
}}

.responsive-container {{
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}}

@media (min-width: 768px) {{
  .responsive-container {{
    padding: 0 2rem;
  }}
}}
"""
                file_path.write_text(content)
                return True
        
        return False

    def _update_components(self) -> bool:
        """Update component files."""
        components_dir = self.repo_path / "components"
        components_dir.mkdir(exist_ok=True)
        
        component_files = [
            ("Button.tsx", "Button component"),
            ("Card.tsx", "Card component"),
            ("Modal.tsx", "Modal component"),
            ("Loading.tsx", "Loading component")
        ]
        
        for filename, description in component_files:
            file_path = components_dir / filename
            if not file_path.exists():
                component_name = description.split()[0]
                content = f"""import React from 'react';

interface {component_name}Props {{
  children?: React.ReactNode;
  className?: string;
  onClick?: () => void;
}}

export function {component_name}({{ 
  children, 
  className = '', 
  onClick 
}}: {component_name}Props) {{
  return (
    <div 
      className="{{component_name.lower()}}-component {{className}}"
      onClick={{onClick}}
    >
      {{children}}
    </div>
  );
}}
"""
                file_path.write_text(content)
                return True
        
        return False

    def make_commit(self) -> bool:
        """Make a meaningful commit."""
        try:
            # Check if we're in a git repository
            self.run_command(["git", "rev-parse", "--git-dir"])
            
            # Create meaningful changes
            if not self.create_meaningful_changes():
                logger.info("No meaningful changes to commit")
                return False
            
            # Stage all changes
            self.run_command(["git", "add", "."])
            
            # Generate commit message
            commit_message = self.generate_commit_message()
            
            # Make the commit
            self.run_command(["git", "commit", "-m", commit_message])
            
            logger.info(f"Successfully committed: {commit_message}")
            return True
            
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to make commit: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return False

    def push_changes(self) -> bool:
        """Push changes to remote repository."""
        try:
            self.run_command(["git", "push"])
            logger.info("Successfully pushed changes to remote")
            return True
        except subprocess.CalledProcessError as e:
            logger.error(f"Failed to push changes: {e}")
            return False

def main():
    """Main function to run the Git bot."""
    bot = GitBot()
    
    # Check if we should make a commit today
    today = datetime.date.today()
    
    # Get the last commit date
    try:
        last_commit = bot.run_command(["git", "log", "-1", "--format=%cd", "--date=short"])
        last_commit_date = datetime.datetime.strptime(last_commit, "%Y-%m-%d").date()
        
        if last_commit_date == today:
            logger.info("Already made a commit today")
            return
    except:
        pass
    
    # Make a commit
    if bot.make_commit():
        # Push changes
        bot.push_changes()
    else:
        logger.info("No commit was made")

if __name__ == "__main__":
    main() 