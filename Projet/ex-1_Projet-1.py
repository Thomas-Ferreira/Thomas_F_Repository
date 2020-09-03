import requests
from bs4 import BeautifulSoup
import json


def getRepositories():
	res = requests.get("https://api.github.com/repositories")
	#parser = BeautifulSoup(reponse.text)
	json.loads(res.text)
	
	json_item = json.loads(res.text)
	for item in json_item:
		title = "Title : " + item["name"]
		open("/home/thomas/Thomas_F_Repository/Projet/results.text","a").write(title+"\n")
		

getRepositories()	
	
