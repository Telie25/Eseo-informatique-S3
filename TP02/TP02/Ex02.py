classDict = { 
    "class": { 
        "student": { 
            "name": "Mike", 
            "marks": { 
                "physics": 70, 
                "history": 80 
            } 
        } 
    } 
}

#1nom de l'étudiant
print(classDict["class"]["student"]["name"])

#2changement de la note
classDict["class"]["student"]["marks"]["physics"]=89

#3ajout de la clé 'average'
notes=[]
for value in classDict["class"]["student"]["marks"].values():
    notes+=[value]
sum=0
for i in range (len(notes)):
    sum+=notes[i]
classDict["class"]["student"]["average"]=sum/len(notes)

#4mise en liste
classDict["class"]["student"]=[classDict["class"]["student"]]

#5ajout de Ted
classDict["class"]["student"]+=[{"name":"Ted","marks":{"physics": 34,"history": 99}}]

#6ajout de la clé 'average' pour Ted
notes=[]
for value in classDict["class"]["student"][1]["marks"].values():
    notes+=[value]
sum=0
for i in range (len(notes)):
    sum+=notes[i]
classDict["class"]["student"][1]["average"]=sum/len(notes)

#7ajout de la clé 'average_grade'
sum=0
for i in range (len(classDict["class"]["student"])):
    sum+=classDict["class"]["student"][i]["average"]
classDict["class"]["student"]+=[{"average":sum/len(classDict["class"]["student"])}]

#8Afficher le dico complet
print(classDict)