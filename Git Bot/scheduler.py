#!/usr/bin/env python3
"""
Git Bot Scheduler - Automatically runs the Git bot at scheduled intervals
"""

import schedule
import time
import subprocess
import logging
import os
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('git_bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def run_git_bot():
    """Run the Git bot script."""
    try:
        # Get the directory where this script is located
        script_dir = Path(__file__).parent
        git_bot_script = script_dir / "git_bot.py"
        
        # Change to the repository directory (parent of Git Bot folder)
        repo_dir = script_dir.parent
        
        # Run the Git bot
        result = subprocess.run(
            [sys.executable, str(git_bot_script)],
            cwd=repo_dir,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            logger.info("Git bot executed successfully")
            if result.stdout:
                logger.info(f"Output: {result.stdout}")
        else:
            logger.error(f"Git bot failed with return code {result.returncode}")
            if result.stderr:
                logger.error(f"Error: {result.stderr}")
                
    except Exception as e:
        logger.error(f"Failed to run Git bot: {e}")

def setup_schedule():
    """Set up the schedule for running the Git bot."""
    # Run once per day at a random time between 9 AM and 6 PM
    schedule.every().day.at("14:30").do(run_git_bot)
    
    # Also run on weekdays at 10:00 AM as a backup
    schedule.every().monday.at("10:00").do(run_git_bot)
    schedule.every().tuesday.at("10:00").do(run_git_bot)
    schedule.every().wednesday.at("10:00").do(run_git_bot)
    schedule.every().thursday.at("10:00").do(run_git_bot)
    schedule.every().friday.at("10:00").do(run_git_bot)
    
    logger.info("Schedule set up successfully")
    logger.info("Git bot will run daily at 14:30 and weekdays at 10:00")

def main():
    """Main function to run the scheduler."""
    logger.info("Starting Git Bot Scheduler...")
    
    # Set up the schedule
    setup_schedule()
    
    # Run once immediately to test
    logger.info("Running initial test...")
    run_git_bot()
    
    logger.info("Scheduler is running. Press Ctrl+C to stop.")
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
    except KeyboardInterrupt:
        logger.info("Scheduler stopped by user")
    except Exception as e:
        logger.error(f"Scheduler error: {e}")

if __name__ == "__main__":
    main() 