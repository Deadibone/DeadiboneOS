import os
import subprocess
import threading
import signal
import sys
import time
from pathlib import Path
import git  # Ensure you have GitPython installed
import keyboard  # Ensure you have the keyboard library installed

def install_repo(repo):
    """Install a GitHub repository to the DeadiboneOS apps directory."""
    base_dir = os.path.join(os.path.expanduser("~"), "DeadiboneOS", "apps")
    repo_name = repo.split('/')[-1]
    install_dir = os.path.join(base_dir, repo_name)

    # Create the apps directory if it doesn't exist
    Path(base_dir).mkdir(parents=True, exist_ok=True)

    # Clone the repository
    try:
        print(f"Installing {repo}...")
        git.Repo.clone_from(f"https://github.com/{repo}.git", install_dir)
        print(f"Installed {repo} to {install_dir}")
    except Exception as e:
        print(f"Error installing repository: {e}")

    return install_dir

def listen_for_quit(process):
    """Listen for Ctrl + Q to terminate the process."""
    while True:
        if keyboard.is_pressed('ctrl+q'):
            confirmation = input("\nAre you sure you want to quit? (y/n): ").strip().lower()
            if confirmation == 'y':
                print("Quitting application...")
                process.terminate()  # Terminate the subprocess
                break
        time.sleep(0.1)  # Polling delay

def run_installed_app(repo_name):
    """Run a Python script from the installed application."""
    app_dir = os.path.join(os.path.expanduser("~"), "DeadiboneOS", "apps", repo_name)

    if not os.path.exists(app_dir):
        print(f"No application found for '{repo_name}'")
        return

    # List all .py files in the application directory
    scripts = [f for f in os.listdir(app_dir) if f.endswith('.py')]
    
    if not scripts:
        print(f"No Python scripts found in '{repo_name}'")
        return

    print("Available scripts:")
    for i, script in enumerate(scripts):
        print(f"{i + 1}: {script}")

    choice = input("Select a script to run (number): ")
    try:
        script_to_run = scripts[int(choice) - 1]
        script_path = os.path.join(app_dir, script_to_run)

        # Run the selected script in a subprocess
        process = subprocess.Popen(["python", script_path])

        # Start a thread to listen for Ctrl + Q
        listener_thread = threading.Thread(target=listen_for_quit, args=(process,))
        listener_thread.daemon = True  # Allow thread to exit when main program does
        listener_thread.start()

        while True:
            if process.poll() is not None:  # Check if the process has finished
                print("Application has finished running.")
                break
            time.sleep(0.1)  # Polling delay

    except (ValueError, IndexError):
        print("Invalid selection. Please choose a valid number.")
    except Exception as e:
        print(f"An error occurred: {e}")