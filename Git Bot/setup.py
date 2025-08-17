#!/usr/bin/env python3
"""
Setup script for Git Bot Agent
"""

import subprocess
import sys
import os
from pathlib import Path

def install_requirements():
    """Install required Python packages."""
    print("Installing required packages...")
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def make_executable():
    """Make scripts executable."""
    scripts = ["git_bot.py", "scheduler.py"]
    for script in scripts:
        script_path = Path(script)
        if script_path.exists():
            try:
                script_path.chmod(0o755)
                print(f"✅ Made {script} executable")
            except Exception as e:
                print(f"⚠️  Could not make {script} executable: {e}")

def check_git_repo():
    """Check if we're in a git repository."""
    try:
        subprocess.run(["git", "rev-parse", "--git-dir"], 
                      capture_output=True, check=True)
        print("✅ Git repository found")
        return True
    except subprocess.CalledProcessError:
        print("❌ Not in a git repository. Please run this from a git repository.")
        return False

def check_git_config():
    """Check if git user is configured."""
    try:
        name = subprocess.run(["git", "config", "user.name"], 
                            capture_output=True, text=True, check=True)
        email = subprocess.run(["git", "config", "user.email"], 
                             capture_output=True, text=True, check=True)
        
        if name.stdout.strip() and email.stdout.strip():
            print(f"✅ Git configured: {name.stdout.strip()} <{email.stdout.strip()}>")
            return True
        else:
            print("⚠️  Git user not configured. Please run:")
            print("   git config --global user.name 'Your Name'")
            print("   git config --global user.email 'your.email@example.com'")
            return False
    except subprocess.CalledProcessError:
        print("⚠️  Could not check git configuration")
        return False

def create_launch_script():
    """Create a launch script for easy execution."""
    launch_script = """#!/bin/bash
# Git Bot Launcher
cd "$(dirname "$0")"
python3 scheduler.py
"""
    
    with open("launch_git_bot.sh", "w") as f:
        f.write(launch_script)
    
    try:
        os.chmod("launch_git_bot.sh", 0o755)
        print("✅ Created launch script: launch_git_bot.sh")
    except Exception as e:
        print(f"⚠️  Could not make launch script executable: {e}")

def main():
    """Main setup function."""
    print("🚀 Setting up Git Bot Agent...")
    print("=" * 50)
    
    # Check if we're in a git repository
    if not check_git_repo():
        return
    
    # Check git configuration
    check_git_config()
    
    # Install requirements
    if not install_requirements():
        return
    
    # Make scripts executable
    make_executable()
    
    # Create launch script
    create_launch_script()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\nTo start the Git Bot:")
    print("1. Run: ./launch_git_bot.sh")
    print("2. Or run: python3 scheduler.py")
    print("\nThe bot will:")
    print("- Make daily commits at 14:30")
    print("- Make weekday commits at 10:00")
    print("- Create meaningful changes and commit messages")
    print("- Push changes automatically")
    print("\nTo stop the bot, press Ctrl+C")
    print("\nLogs will be saved to git_bot.log")

if __name__ == "__main__":
    main() 