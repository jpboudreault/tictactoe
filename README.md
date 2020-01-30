![](https://github.com/jpboudreault/tictactoe/workflows/syntax-and-unit-tests/badge.svg)

# Tic Tac Toe X
Python project for my kid's tic tac toe game. Feel free to reuse for 
your own fun or for educational purposes! It is available in French and English.

## setup
Adjust the following based on your environment

1. Get Python
1. Get PIP
1. `pip install -r requirements.txt`
1. `python3 manage.py migrate`
1. `python3 manage.py runserver`
1. Set the language using an environment property of by tweaking settings.py

## adding another language
The following is a French example (fr)
`python3 manage.py makemessages -l fr -i venv`
`python3 manage.py compilemessages -i venv`

## notes & todos
todo bla bla around the env variable
todo clean up the simulation page
todo use fontawesome's icons for the game
todo use react instead of python views + jquery
