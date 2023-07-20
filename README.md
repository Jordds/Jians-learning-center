# Setup

Start of with installing an IDE, this is your coding environment. Most have built in features to help you code by doing a range of things like formatting code, show code thats wrong and more. There is a big list of IDE's available to use. 

- Vscode
- PyCharm

 This site gives you a bit more insight into IDE's and what they offer you. 
https://www.simplilearn.com/tutorials/python-tutorial/python-ide

# Install Linux (optional)

Install WSL in the command line. This allows you to run linux from within Windows. https://learn.microsoft.com/en-us/windows/wsl/install

Go to the windows store and download Ubuntu 22.04 LTS

The advantages of using Linux are pre-installed Python and it is pretty common for development teams to use Linux. It is optional since you can do everything on Windows as well

From what I know, to run Docker it would require Linux. For now Docker isn't a priority to run yet, in about a month or two when you want to learn to work with databases, this will be beneficial. The other solution is installing a database locally in Windows to work with it, which is a little bit of a pain to do.

# Install Python

Option 1: If chosen for Windows, Install Python through the Microsoft Store. This will allow the system to work with Python. 

Option 2: Install PyEnv on the system. This is a Python version manager which allows to easily swap between different version of Python. This may not be a big deal for now, but once you get more into programming, needing to switch versions can become an occurance. Using PyEnv allows for easily switchin to te needed version. https://github.com/pyenv-win/pyenv-win Note: I dont have this installed myself on windows. I do on Linux. 

# install Packages

The first thing you need to install is pip. This will allow to install Python packages with ease. Follow this guide https://phoenixnap.com/kb/install-pip-windows 

The next step is to install pipenv. This allows to create virtual environment for your project with the Python version and needed packages. This is a great tool when collaborating on code. By running a couple commands, you can activate the environment and make use of the needed packages and their versions. This will save you a great deal of time not having to manage your local versions of packages and more. Follow this installation guide: https://www.pythontutorial.net/python-basics/install-pipenv-windows/

