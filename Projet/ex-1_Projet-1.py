import requests
from bs4 import Beautifulsoup
import json


def getRepositories():
    reponse = requests.get("https://api.github.com/repositories")
    print (reponse)




