import requests
from bs4 import BeautifulSoup
import json


def getRepositories():
	reponse = requests.get("https://api.github.com/repositories")
	#parser = BeautifulSoup(results.text)
	if reponse:
		print('Success')
	else:
		print('Error')
		

getRepositories()	
	
