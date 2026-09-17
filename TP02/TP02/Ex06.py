from colorama import Fore, Back, Style, init
init(autoreset=True)
import requests 
#py -m pip install requests 
#Fonction d'impression de liste de liste sous forme tableau
def print_table(table):
    col_widths = [max(len(str(row[i])) for row in table) for i in range(len(table[0]))]
    for row_index, row in enumerate(table):
        line = " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        if row_index == 0:
            print(Fore.RED + line)
        else:
            print(line)

def get_university_data(country = "France"):
    url = f"http://universities.hipolabs.com/search?country={country}"

    rawdata = requests.get(url)

    if not rawdata:
        raise Exception

    data = rawdata.json()
    return data


if __name__ == "__main__":
    uni_data = get_university_data("France")
    print(uni_data)

#Enlever les université sans region specifié
b=0
for i in range (len(uni_data)):
    a=i-b
    if uni_data[a]['state-province']==None:
        uni_data.pop(a)
        b+=1
#Creer une liste trier des régions
L=[]
for i in range (len(uni_data)):
    L+=[uni_data[i]['state-province']]
L.sort()
#Trie les université par leur région
uni_data_sorted=[]
for i in range (len(uni_data)):
    a=0
    b=0
    while a==0:
        if uni_data[b]['state-province']==L[i]:
            uni_data_sorted+=[uni_data.pop(b)]
            a=1
        else:
            b+=1
#Imprime un tableau des universités triées
table=[]
table+=[list(uni_data_sorted[0].keys())]
for i in range (len(uni_data_sorted)):
    table+=[list(uni_data_sorted[i].values())]
print_table(table)
    