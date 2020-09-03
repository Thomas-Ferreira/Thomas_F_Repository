###### Test_1 #####

import os

os.chdir('./books')

def getBooksTitleAndAuthor():

    titles=[]
    authors=[]
    dictionnary={}

    for file in os.listdir():
        current_file=open(file,encoding="utf-8")

        for line in current_file.readlines():

            if line.startswith("Title:"):
                titles.append(line.split(": ")[1].replace("\n", ""))

            elif line.startswith("Author:"):
                authors.append(line.split(": ")[1].replace("\n", ""))

                break  

            dictionnary["titles"] = titles     
            dictionnary["authors"] = authors
            return dictionnary


def renameAllBooks():

    dictionnary=getBooksTitleAndAuthor()
    i=0
    
    for file in os.listdir():
        os.rename(file, dictionnary["titles"][i] + "-" + dictionnary["authors"][i] + ".txt")
        i += 1
