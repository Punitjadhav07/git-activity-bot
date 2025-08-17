#!/usr/bin/env python3
import os
import random
import subprocess
import datetime
from pathlib import Path

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except:
        return None

def generate_commit_message():
    commit_types = ["feat", "fix", "docs", "refactor", "test", "chore"]
    scopes = ["ui", "api", "auth", "database", "config", "utils"]
    features = ["user authentication", "data validation", "error handling", "performance optimization"]
    
    commit_type = random.choice(commit_types)
    scope = random.choice(scopes)
    
    if commit_type == "feat":
        feature = random.choice(features)
        return f"feat({scope}): add {feature}"
    elif commit_type == "fix":
        return f"fix({scope}): resolve performance issue"
    else:
        return f"{commit_type}({scope}): update component"

def create_changes():
    # Update README
    readme_path = Path("README.md")
    if readme_path.exists():
        content = readme_path.read_text()
        new_section = "\n## Recent Updates\n\n- Enhanced performance\n- Improved error handling\n- Better code organization\n"
        if new_section not in content:
            readme_path.write_text(content + new_section)
            return True
    
    # Create utility file
    utils_dir = Path("utils")
    utils_dir.mkdir(exist_ok=True)
    
    helper_file = utils_dir / "helpers.py"
    if not helper_file.exists():
        helper_file.write_text("""# Helper functions

def format_date(date):
    return date.strftime('%Y-%m-%d')

def validate_email(email):
    import re
    return re.match(r'^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$', email) is not None
""")
        return True
    
    return False

def main():
    # Check if already committed today
    today = datetime.date.today()
    last_commit = run_command(["git", "log", "-1", "--format=%cd", "--date=short"])
    
    if last_commit:
        try:
            last_commit_date = datetime.datetime.strptime(last_commit, "%Y-%m-%d").date()
            if last_commit_date == today:
                print("Already made a commit today")
                return
        except:
            pass
    
    # Create changes
    if create_changes():
        # Stage and commit
        run_command(["git", "add", "."])
        commit_message = generate_commit_message()
        run_command(["git", "commit", "-m", commit_message])
        print(f"Committed: {commit_message}")
    else:
        print("No changes to commit")

if __name__ == "__main__":
    main()
