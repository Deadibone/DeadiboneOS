import os
import colorama
from colorama import Fore
import shutil

colorama.init(autoreset=True)

def get_file_color(filename):
    if os.path.isdir(filename):
        return Fore.YELLOW  # Directories
    elif filename.endswith(('.c', '.cpp', '.h', '.py', '.java', '.js')):
        return Fore.GREEN   # Source code files
    elif filename.endswith('.txt'):
        return Fore.BLUE    # Text files
    elif filename.endswith(('.doc', '.docx', '.ppt', '.pptx', '.xls', '.xlsx')):
        return Fore.RED     # Office files
    elif filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
        return Fore.MAGENTA  # Image files
    elif filename.endswith(('.zip', '.tar', '.gz', '.rar')):
        return Fore.YELLOW   # Archive files
    elif filename.endswith(('.mp3', '.wav', '.ogg')):
        return Fore.CYAN     # Audio files
    elif filename.endswith(('.mp4', '.avi', '.mov', '.mkv')):
        return Fore.WHITE    # Video files
    else:
        return Fore.WHITE    # Default color for other files

def ls():
    files = os.listdir()
    if files:
        print("+" + "-" * 80 + "+")
        print("| {:<39} | {:<39} |".format("Deadibone", "DeadiboneOS"))
        print("+" + "-" * 80 + "+")
        
        for i in range(0, len(files), 2):
            row = ""
            for j in range(2):
                if i + j < len(files):
                    filename = files[i + j]
                    color = get_file_color(os.path.join(os.getcwd(), filename))
                    row += "{}{: <37} | ".format(color, filename)
                else:
                    row += "{:<39} | ".format("")  # Empty space for odd number of files
            print("| " + row.rstrip() + " |")
        
        print("+" + "-" * 80 + "+")
    else:
        print("No files found.")

def mkdir(directory):
    """Create a new directory."""
    try:
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    except FileExistsError:
        print(f"mkdir: cannot create directory '{directory}': File exists")
    except Exception as e:
        print(f"mkdir: {e}")

def rm(filename):
    """Remove a file."""
    try:
        os.remove(filename)
        print(f"File '{filename}' removed.")
    except FileNotFoundError:
        print(f"rm: cannot remove '{filename}': No such file or directory")
    except IsADirectoryError:
        print(f"rm: cannot remove '{filename}': Is a directory")
    except Exception as e:
        print(f"rm: {e}")

def rmdir(directory):
    """Remove an empty directory."""
    try:
        os.rmdir(directory)
        print(f"Directory '{directory}' removed.")
    except FileNotFoundError:
        print(f"rmdir: cannot remove '{directory}': No such file or directory")
    except OSError:
        print(f"rmdir: cannot remove '{directory}': Directory not empty")
    except Exception as e:
        print(f"rmdir: {e}")
        
def cp(original, copy):
    """Copy a file from original to copy."""
    try:
        shutil.copy(original, copy)
        print(f"Copied '{original}' to '{copy}'.")
    except FileNotFoundError:
        print(f"cp: {original}: No such file or directory")
    except Exception as e:
        print(f"cp: error: {e}")

def ren(original, new_name):
    """Rename a file from original to new_name."""
    try:
        os.rename(original, new_name)
        print(f"Renamed '{original}' to '{new_name}'.")
    except FileNotFoundError:
        print(f"ren: {original}: No such file or directory")
    except Exception as e:
        print(f"ren: error: {e}")