''' Run different python versions i.e. 2.7 > python or python2.7 or 3.5 > python3.5 '''
''' Use pip the same way, pip for python 2.7 or pip3.5 for python3.5 '''
''' install desired python version in virtual env > virtual <env> --python=python<version> '''
''' Using virtual environments you can run python version & other package versions desired '''

#First Flask_Restful app
from flask import Flask
from Flask_Restful import resource, api

''' Resources are things the api is concerned with e.g, items, students etc '''

app = Flask(__name__)
