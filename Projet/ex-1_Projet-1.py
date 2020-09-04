import os
import requests
from bs4 import BeautifulSoup
import json
		
#def emptyfile(fichier.text)
	#if fichier.text is not none
		

def getRepositories():
	res = requests.get("https://api.github.com/repositories")
	json.loads(res.text)
	
	json_item = json.loads(res.text)
	for item in json_item:
		title = "Title : " + item["name"] + "\n" + "Description : "
		des = item["description"]
		if des is None :
			des = "no description "
		open("/home/thomas/Thomas_F_Repository/Projet/results.text","a").write(title+des+"\n")
		

getRepositories()	
	
