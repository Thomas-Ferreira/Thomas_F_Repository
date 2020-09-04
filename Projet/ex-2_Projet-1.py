import os
import requests
import json
		

def getRepositories():
	res = requests.get("https://api.github.com/search/repositories?sort=star&q=created:2020-01-01&perpage=100")
	
	json_item = json.loads(res.text)["items"]
	#print (json_item)
	for item in json_item:
		title = "Title : " + item["name"] + "\n" + "Description : "
		des = item["description"]
		if des is None :
			des = "no description "
		star = str(item ["stargazers_count"])
		open("/home/thomas/Thomas_F_Repository/Projet/results_ex-2.text","a").write(title+"	"+des+"\n"+" stars : " + star + "\n")
		

getRepositories()	
