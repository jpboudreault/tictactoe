![](https://github.com/jpboudreault/tictactoe/workflows/syntax-and-unit-tests/badge.svg)

# Tic Tac Toe X
Python project for my kid's tic tac toe game. Feel free to reuse for 
your own fun or for educational purposes! It is available in French and English.

## Setup
Adjust the following based on your environment

1. Get Python
1. Get PIP
1. `pip install -r requirements.txt`
1. `python3 manage.py migrate`
1. `python3 manage.py runserver`
1. Set the language using an environment property of by tweaking settings.py

## Environment Variables
1. `LANGUAGE_CODE` Language for the website. Currently supported: 'fr', 'en' 
1. `ALLOWED_HOSTS` collection of domain names where the project is hosted
1. `DEBUG` set to false when deploying on production
1. `SECRET_KEY` for administration

## How tos
### Add another language
The following is a French example (fr)
`python3 manage.py makemessages -l fr -i venv`
`python3 manage.py compilemessages -i venv`

## Todos
todo finish experimental defense play style (Xavier)
todo finish English support in JavaScript
todo use fontawesome's icons for the game
todo use react instead of python views + jquery
todo clean up the simulation page
