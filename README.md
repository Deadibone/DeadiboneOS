# [Deadibone](https://deadibone.github.io)
This is a dumb *os*

Written in python.

Just download all of the python scripts and run deadiboneos.py

This is NOT proffessional

## Commands:

cd: Usage: cd <directory> Change the current directory to <directory>.,

mkdir: Usage: mkdir <directory> Create a new directory with the name <directory>.,

rm: Usage: rm <file> Remove the file <file>.,

rmdir: Usage: rmdir <directory> Remove the directory <directory>.,

symf: Usage: symf <filename> Open <filename> in the text editor.,

fetch: Usage: fetch <URL> Download the file from the specified <URL>.,

reboot: Usage: reboot Restart the DeadiboneOS environment.,

python: usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...   Options (and corresponding environment variables):  -b : issue warnings about str(bytes_instance), str(bytearray_instance)   and comparing bytes/bytearray with str. (-bb: issue errors)  -B : don't write .pyc files on import; also PYTHONDONTWRITEBYTECODE=x  -c cmd : program passed in as string (terminates option list)  -d : turn on parser debugging output (for experts only, only works on   debug builds); also PYTHONDEBUG=x  -E : ignore PYTHON* environment variables (such as PYTHONPATH)  -h : print this help message and exit (also -? or --help)  -i : inspect interactively after running script; forces a prompt even   if stdin does not appear to be a terminal; also PYTHONINSPECT=x  -I : isolate Python from the user's environment (implies -E and -s)  -m mod : run library module as a script (terminates option list)  -O : remove assert and __debug__-dependent statements; add .opt-1 before   .pyc extension; also PYTHONOPTIMIZE=x  -OO: do -O changes and also discard docstrings; add .opt-2 before   .pyc extension  -P : don't prepend a potentially unsafe path to sys.path  -q : don't print version and copyright messages on interactive startup  -s : don't add user site directory to sys.path; also PYTHONNOUSERSITE  -S : don't imply 'import site' on initialization  -u : force the stdout and stderr streams to be unbuffered;   this option has no effect on stdin; also PYTHONUNBUFFERED=x  -v : verbose (trace import statements); also PYTHONVERBOSE=x   can be supplied multiple times to increase verbosity  -V : print the Python version number and exit (also --version)   when given twice, print more information about the build  -W arg : warning control; arg is action:message:category:module:lineno   also PYTHONWARNINGS=arg  -x : skip first line of source, allowing use of non-Unix forms of #!cmd  -X opt : set implementation-specific option  --check-hash-based-pycs always|default|never:   control how Python invalidates hash-based .pyc files  --help-env  : print help about Python environment variables and exit  --help-xoptions : print help about implementation-specific -X options and exit  --help-all  : print complete help information and exit   Arguments:  file   : program read from script file  -  : program read from stdin (default; interactive mode if a tty)  arg ...: arguments passed to program in sys.argv[1:],

pip: Usage:pip <command> [options]   Commands:install Install packages.downloadDownload packages.uninstall   Uninstall packages.freeze  Output installed packages in requirements format.inspect Inspect the python environment.listList installed packages.showShow information about installed packages.check   Verify installed packages have compatible dependencies.config  Manage local and global configuration.search  Search PyPI for packages.cache   Inspect and manage pip's wheel cache.index   Inspect information available from package indexes.wheel   Build wheels from your requirements.hashCompute hashes of package archives.completion  A helper command used for command completion.debug   Show information useful for debugging.helpShow help for commands.   General Options:-h, --help  Show help.--debug Let unhandled exceptions propagate outside the main subroutine,instead of logging them to stderr.--isolated  Run pip in an isolated mode, ignoring environment variables and user configuration.--require-virtualenvAllow pip to only run in a virtual environment; exit with an error otherwise.--python <python>   Run pip with the specified Python interpreter.-v, --verbose   Give more output. Option is additive, and can be used up to 3 times.-V, --version   Show version and exit.-q, --quiet Give less output. Option is additive, and can be used up to 3 times (corresponding to WARNING, ERROR,and CRITICAL logging levels).--log <path>Path to a verbose appending log.--no-input  Disable prompting for input.--keyring-provider <keyring_provider>Enable the credential lookup via the keyring library if user input is allowed. Specify whichmechanism to use [disabled, import, subprocess]. (default: disabled)--proxy <proxy> Specify a proxy in the form scheme://[user:passwd@]proxy.server:port.--retries <retries> Maximum number of retries each connection should attempt (default 5 times).--timeout <sec> Set the socket timeout (default 15 seconds).--exists-action <action>Default action when a path already exists: (s)witch, (i)gnore, (w)ipe, (b)ackup, (a)bort.--trusted-host <hostname>   Mark this host or host:port pair as trusted, even though it does not have valid or any HTTPS.--cert <path>   Path to PEM-encoded CA certificate bundle. If provided, overrides the default. See 'SSL CertificateVerification' in pip documentation for more information.--client-cert <path>Path to SSL client certificate, a single file containing the private key and the certificate in PEMformat.--cache-dir <dir>   Store the cache data in <dir>.--no-cache-dir  Disable the cache.--disable-pip-version-checkDon't periodically check PyPI to determine whether a new version of pip is available for download.Implied with --no-index.--no-color  Suppress colored output.--no-python-version-warningSilence deprecation warnings for upcoming unsupported Pythons.--use-feature <feature> Enable new functionality, that may be backward incompatible.--use-deprecated <feature>  Enable deprecated functionality, that will be removed in the future.,

google: Usage: google <search query> Search Google for <search query>.,

man: Usage: man <command> Display the manual for <command>.,

ls: Usage: ls List files and directories in the current directory.,

clear: Usage: clear Clear the terminal screen.,

exit: Usage: exit Exit the DeadiboneOS environment.,

man: Usage: man <command search> Search commands,

cp: Usage: cp <original filename> <copied filename> Copy a file.,

ren: Usage: ren <original filename> <name after renamed> Rename a file.,

wikipedia: Usage: wikipedia <article title>  Fetch and display the Wikipedia article.,

dox: Usage: dox  A simple word processor.,

flask: Usage: flask [OPTIONS] COMMAND [ARGS]... A general utility script for Flask applications. An application to load must be given with the '--app' option, 'FLASK_APP'environment variable, or with a 'wsgi.py' or 'app.py' file in the currentdirectory.   Options:-e, --env-file FILE   Load environment variables from this file. python-  dotenv must be installed.-A, --app IMPORT  The Flask application or factory function to load, in  the form 'module:name'. Module can be a dotted import  or file path. Name is not required if it is 'app',  'application', 'create_app', or 'make_app', and can be  'name(args)' to pass arguments.--debug / --no-debug  Set debug mode.--version Show the Flask version.--helpShow this message and exit.   Commands:routes  Show the routes for the app.run Run a development server.shell   Run a shell in the app context.,

install: Usage: install <github-username/github-repo> Install a GitHub repository.
