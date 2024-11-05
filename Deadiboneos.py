import os
import curses
import subprocess
from file_manager import ls, mkdir, rm, rmdir, cp, ren
from symf import symf 
from fetch import fetch
from google import google_search
from wikipedia import fetch_wikipedia_article
from install import install_repo, run_installed_app
from colorama import Fore, Back, Style


# Manual entries for commands
manual = {
    "cd": "Usage: cd <directory>\nChange the current directory to <directory>.",
    "mkdir": "Usage: mkdir <directory>\nCreate a new directory with the name <directory>.",
    "rm": "Usage: rm <file>\nRemove the file <file>.",
    "rmdir": "Usage: rmdir <directory>\nRemove the directory <directory>.",
    "symf": "Usage: symf <filename>\nOpen <filename> in the text editor.",
    "fetch": "Usage: fetch <URL>\nDownload the file from the specified <URL>.",
    "reboot": "Usage: reboot\nRestart the DeadiboneOS environment.",
    "python": "usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ... \n\nOptions (and corresponding environment variables): \n-b     : issue warnings about str(bytes_instance), str(bytearray_instance) \n         and comparing bytes/bytearray with str. (-bb: issue errors) \n-B     : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x \n-c cmd : program passed in as string (terminates option list) \n-d     : turn on parser debugging output (for experts only, only works on \n         debug builds); also PYTHONDEBUG=x \n-E     : ignore PYTHON* environment variables (such as PYTHONPATH) \n-h     : print this help message and exit (also -? or --help) \n-i     : inspect interactively after running script; forces a prompt even \n         if stdin does not appear to be a terminal; also PYTHONINSPECT=x \n-I     : isolate Python from the user's environment (implies -E and -s) \n-m mod : run library module as a script (terminates option list) \n-O     : remove assert and __debug__-dependent statements; add .opt-1 before \n         .pyc extension; also PYTHONOPTIMIZE=x \n-OO    : do -O changes and also discard docstrings; add .opt-2 before \n         .pyc extension \n-P     : don't prepend a potentially unsafe path to sys.path \n-q     : don't print version and copyright messages on interactive startup \n-s     : don't add user site directory to sys.path; also PYTHONNOUSERSITE \n-S     : don't imply 'import site' on initialization \n-u     : force the stdout and stderr streams to be unbuffered; \n         this option has no effect on stdin; also PYTHONUNBUFFERED=x \n-v     : verbose (trace import statements); also PYTHONVERBOSE=x \n         can be supplied multiple times to increase verbosity \n-V     : print the Python version number and exit (also --version) \n         when given twice, print more information about the build \n-W arg : warning control; arg is action:message:category:module:lineno \n         also PYTHONWARNINGS=arg \n-x     : skip first line of source, allowing use of non-Unix forms of #!cmd \n-X opt : set implementation-specific option \n--check-hash-based-pycs always|default|never: \n         control how Python invalidates hash-based .pyc files \n--help-env      : print help about Python environment variables and exit \n--help-xoptions : print help about implementation-specific -X options and exit \n--help-all      : print complete help information and exit \n\nArguments: \nfile   : program read from script file \n-      : program read from stdin (default; interactive mode if a tty) \narg ...: arguments passed to program in sys.argv[1:]",
    "pip": "Usage: \n  pip <command> [options] \n\nCommands: \n  install                     Install packages. \n  download                    Download packages. \n  uninstall                   Uninstall packages. \n  freeze                      Output installed packages in requirements format. \n  inspect                     Inspect the python environment. \n  list                        List installed packages. \n  show                        Show information about installed packages. \n  check                       Verify installed packages have compatible dependencies. \n  config                      Manage local and global configuration. \n  search                      Search PyPI for packages. \n  cache                       Inspect and manage pip's wheel cache. \n  index                       Inspect information available from package indexes. \n  wheel                       Build wheels from your requirements. \n  hash                        Compute hashes of package archives. \n  completion                  A helper command used for command completion. \n  debug                       Show information useful for debugging. \n  help                        Show help for commands. \n\nGeneral Options: \n  -h, --help                  Show help. \n  --debug                     Let unhandled exceptions propagate outside the main subroutine,instead of logging them to stderr. \n  --isolated                  Run pip in an isolated mode, ignoring environment variables and user configuration. \n  --require-virtualenv        Allow pip to only run in a virtual environment; exit with an error otherwise. \n  --python <python>           Run pip with the specified Python interpreter. \n  -v, --verbose               Give more output. Option is additive, and can be used up to 3 times. \n  -V, --version               Show version and exit. \n  -q, --quiet                 Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR, \n                              and CRITICAL logging levels). \n  --log <path>                Path to a verbose appending log. \n  --no-input                  Disable prompting for input. \n  --keyring-provider <keyring_provider> \n                              Enable the credential lookup via the keyring library if user input is allowed. Specify which \n                              mechanism to use [disabled, import, subprocess]. (default: disabled) \n  --proxy <proxy>             Specify a proxy in the form scheme://[user:passwd@]proxy.server:port. \n  --retries <retries>         Maximum number of retries each connection should attempt (default 5 times). \n  --timeout <sec>             Set the socket timeout (default 15 seconds). \n  --exists-action <action>    Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort. \n  --trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS. \n  --cert <path>               Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL Certificate \n                              Verification' in pip documentation for more information. \n  --client-cert <path>        Path to SSL client certificate, a single file containing the private key and the certificate in PEM \n                              format. \n  --cache-dir <dir>           Store the cache data in <dir>. \n  --no-cache-dir              Disable the cache. \n  --disable-pip-version-check \n                              Don't periodically check PyPI to determine whether a new version of pip is available for download. \n                              Implied with --no-index. \n  --no-color                  Suppress colored output. \n  --no-python-version-warning \n                              Silence deprecation warnings for upcoming unsupported Pythons. \n  --use-feature <feature>     Enable new functionality, that may be backward incompatible. \n  --use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.",
    "google": "Usage: google <search query>\nSearch Google for <search query>.",
    "man": "Usage: man <command>\nDisplay the manual for <command>.",
    "ls": "Usage: ls\nList files and directories in the current directory.",
    "clear": "Usage: clear\nClear the terminal screen.",
    "exit": "Usage: exit\nExit the DeadiboneOS environment.",
    "man": "Usage: you're using it right now",
    "cp": "Usage: cp <original filename> <copied filename>\nCopy a file.",
    "ren": "Usage: ren <original filename> <name after renamed>\nRename a file.",
    "wikipedia": "Usage: wikipedia <article title> \nFetch and display the Wikipedia article.",
    "dox": "Usage: dox \nA simple word processor.",
    "flask": "Usage: flask [OPTIONS] COMMAND [ARGS]... \n\n  A general utility script for Flask applications. \n\n  An application to load must be given with the '--app' option, 'FLASK_APP' \n  environment variable, or with a 'wsgi.py' or 'app.py' file in the current \n  directory. \n\nOptions: \n  -e, --env-file FILE   Load environment variables from this file. python- \n    dotenv must be installed. \n  -A, --app IMPORT      The Flask application or factory function to load, in \n    the form 'module:name'. Module can be a dotted import \n    or file path. Name is not required if it is 'app', \n    'application', 'create_app', or 'make_app', and can be \n    'name(args)' to pass arguments. \n  --debug / --no-debug  Set debug mode. \n  --version             Show the Flask version. \n  --help                Show this message and exit. \n\nCommands: \n  routes  Show the routes for the app. \n  run     Run a development server. \n  shell   Run a shell in the app context.",
    "install": "Usage: install <github-username/github-repo>\nInstall a GitHub repository."
}


def main_menu():
    app_dir = os.path.join(os.path.expanduser("~"), "DeadiboneOS", "apps")
    directory = os.path.join(os.path.expanduser("~"), "DeadiboneOS")
    os.makedirs(app_dir, exist_ok=True)
    os.chdir(directory)
    current_dir = os.getcwd()
    global filename
    
    while True:
        current_dir = os.getcwd()
        print(Fore.GREEN + f"┌──(", end="")
        print(Fore.BLUE + f"{os.getlogin()}𝓫DeadiboneOS", end="")
        print(Fore.GREEN + f")-[", end="")
        print(Fore.WHITE + f"{current_dir}", end="")
        print(Fore.GREEN + f"]")
        print(Fore.GREEN + "└─", end="")
        command = input(Fore.WHITE + f"$ ")
        parts = command.split()
        
        if command == '':
            print("Please type in a command. For help, please type 'man <query>'")
            
        elif parts[0] == "cd":
            directory = ' '.join(parts[1:]).strip('"').strip("'")
            if directory:
                try:
                    os.chdir(directory)
                    current_dir = os.getcwd()
                except FileNotFoundError:
                    print(f"cd: no such file or directory: {directory}")
            else:
                print("cd: missing argument")

        elif parts[0] == "mkdir":
            if len(parts) > 1:
                directory = ' '.join(parts[1:]).strip('"').strip("'")
                mkdir(directory)
            else:
                print("mkdir: missing argument")
                
        elif parts[0] == "dox":
            script_name = ''.join('wordprocessor.py').strip() #Get the script name
                
            try:
                subprocess.run(['python', script_name]) # Run the Python script
            except FileNotFoundError:
                print(f"dox: Launching error, please try again after restarting the system")
            except Exception as e:
                print(f"Error running dox: {e}")
                
        elif parts[0] == "wikipedia":  # New wikipedia command
            if len(parts) > 1:
                title = ' '.join(parts[1:]).strip()
                fetch_wikipedia_article(title)
            else:
                print("wikipedia: missing article title")

        elif parts[0] == "rm":
            if len(parts) > 1:
                filename = ' '.join(parts[1:]).strip('"').strip("'")
                choice = input("Are you sure to remove this file? (y/n) ")
                if choice == 'y':
                    rm(filename)
            else:
                print("rm: missing argument")

        elif parts[0] == "rmdir":
            if len(parts) > 1:
                directory = ' '.join(parts[1:]).strip('"').strip("'")
                choice = input("Are you sure to remove this file? (y/n) ")
                if choice == 'y':
                    rmdir(directory)
            else:
                print("rmdir: missing argument")

        elif parts[0] == "symf":  # Change from nano to symf
            if len(parts) > 1:
                filename = ' '.join(parts[1:]).strip('"').strip("'")  # Handle quoted names
                curses.wrapper(symf, filename)  # Call the symf function with the filename
            else:
                print("symf: missing filename")

        elif parts[0] == "ls":
            ls()
            
        elif parts[0] == "install":
            if len(parts) > 1:
                repo = parts[1]
                install_dir = install_repo(repo)            
            else:
                print("install: missing repository specification")
                            
        elif parts[0] == "cp":  # New cp command
            if len(parts) == 3:
                cp(parts[1], parts[2])
            else:
                print("cp: invalid number of arguments")

        elif parts[0] == "ren":  # New ren command
            if len(parts) == 3:
                ren(parts[1], parts[2])
            else:
                print("ren: invalid number of arguments")
                            
        elif parts[0] == "sysinfo":
            print("DeadiboneOS Alpha 0.01 Python Edition, minimal installation")
            print("This is a VERY EARLY version of DeadiboneOS, it may contain many bugs")
            print("DO NOT TAKE SCREENSHOTS")
            print("   *Website: https://deadibone.github.io")
            
        elif parts[0] == "man":  # New man command
            if len(parts) > 1:
                search_term = parts[1]
                # Search for the command
                if search_term in manual:
                    print(manual[search_term])
                else:
                    # Search for the term in all manual entries
                    print(f"Searching for '{search_term}' in manual entries:")
                    found = False
                    for cmd, description in manual.items():
                        if search_term.lower() in cmd.lower() or search_term.lower() in description.lower():
                            print(f"\n{cmd}:\n{description}")
                            found = True
                    if not found:
                        print(f"man: no manual entry found for '{search_term}'")
            else:
                print("man: missing command name")
        
        elif parts[0] == "google":
            if len(parts) > 1:
                query = ' '.join(parts[1:]).strip() # Join the parts of the query
                
                google_search(query) # Call the google search function
            else:
                print("google: missing search query")
            
        elif parts[0] == "python":
            if len(parts) > 1:
                script_name = ''.join(parts[1:]).strip() #Get the script name
                
                try:
                    subprocess.run(['python', script_name]) # Run the Python script
                except FileNotFoundError:
                    print(f"python: {script_name}: No such file or directory")
                except Exception as e:
                    print(f"Error running script: {e}")
            else:
                print("python: missing script name")
                
        elif parts[0] == "flask":
            if len(parts) > 1:
                script_name = ''.join(parts[1:]).strip() #Get the script name
                
                try:
                    subprocess.run(['flask', script_name]) # Run the Python script
                except FileNotFoundError:
                    print(f"flask: {script_name}: No such flask application")
                except Exception as e:
                    print(f"Error running flask: {e}")
            else:
                print("flask: missing flask application name")
        
        elif parts[0] == "pip":
            if len(parts) > 1:
                try:
                    subprocess.run(['pip'] + parts[1:]) # Pass the rest of the command to pip
                except Exception as e:
                    print(f"Error running pip: {e}")
            else:
                print("pip: missing command")
            
        elif parts[0] == "reboot":
            print("Rebooting DeadiboneOS...")
            return
        
        elif parts[0] == "fetch":
            if len(parts) > 1:
                url = ' '.join(parts[1:]).strip()  # Join the parts of the URL
                fetch(url)  # Call the fetch function
            else:
                print("fetch: missing URL")

        elif parts[0] == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen

        elif parts[0] == "exit":
            print("Exiting DeadiboneOS.")
            break
                          
        else:
            app_dir = os.path.join(os.path.expanduser("~"), "DeadiboneOS", "apps")
            
            command_found = False
            
            for app in os.listdir(app_dir):
                app_path = os.path.join(app_dir, app)
                if os.path.isdir(app_path) and app == parts[0]:
                    run_installed_app(app)
                    command_found = True
                    break
            
            if not command_found:    
                print(f"{parts[0]}: command/application not found")


if __name__ == "__main__":
    print("Welcome to DeadiboneOS Alpha 0.01 Python Edition, minimal installation")
    print("This is a VERY EARLY version of DeadiboneOS, it may contain many bugs")
    print("DO NOT TAKE SCREENSHOTS")
    print("   *Website: https://deadibone.github.io")
    
    while True:
        main_menu()