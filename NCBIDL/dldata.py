from Bio import Entrez
import json

def dlxml():
    f = open("./NCBIDLout/extract.json","r")
    info = json.load(f)
    f.close()

    Accessionlist = []

    for v in info.values():
        Accessionlist.append(v[0])

    print(Accessionlist)

    handle = Entrez.efetch(db="protein", id=Accessionlist, rettype ="gb",retmode="xml")
    records = Entrez.read(handle)

    f = open("./NCBIDLout/dlxml.json","w")
    json.dump(records, f, indent = 0, ensure_ascii=False)
    f.close()

def dltxt():
    f = open("./NCBIDLout/extract.json","r")
    info = json.load(f)
    f.close()

    Accessionlist = []

    for v in info.values():
        Accessionlist.append(str(v[0]))

    handle = Entrez.efetch(db="protein", id=Accessionlist, rettype ="gb",retmode="txt")

    f = open("./NCBIDLout/dltxt.txt","w")
    f.write(handle.read())
    f.close

def makecsv():
    f = open("./NCBIDLout/extract.json","r")
    info = json.load(f)
    f.close()

    f = open("./NCBIDLout/info.csv","w")
    for k,v in info.items():
        f.write(v[0] + "," + k + "\n")
    f.close

