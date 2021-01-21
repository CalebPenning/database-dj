## Playlist-app

To get this application running, make sure you do the following in the Terminal:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `createdb playlist-app`
5. `flask run`

Windows users can do the following in Powershell:

1. `cd C:\PATH\TO\PROJECT\FOLDER`
2. `python -m virtualenv <name_of_environment>`
3. `.\<name_of_environment>\scripts\activate`
4. `pip install -r requirements.txt`
5. `createdb playlist-app`
6. `flask run`

OPTIONAL:
`(While in virtualenv) python -m seed.py`

### To run in development mode
#### Windows:
1. `(In powershell window, before running app) $env:FLASK_ENV = 'development'`
2. `flask run`

#### UNIX:
1. `export FLASK_ENV='development'`
2. `flask run`