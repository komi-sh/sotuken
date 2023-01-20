from Bio import Entrez
import json
import os

# 参照URL
# https://biotech-lab.org/articles/2275#PubMedAbstract
# https://qiita.com/joemphilips/items/767c67524e4b7e328834

def search(kensaku):
    handle = Entrez.esearch(db="protein", term=kensaku,retmax = 1000)
    record = Entrez.read(handle)
    handle = Entrez.efetch(db="protein", id=record["IdList"], retmode="xml")
    records = Entrez.read(handle)

    os.makedirs("./NCBIDLout", exist_ok = True)

    f = open("./NCBIDLout/search.json","w")
    json.dump(records, f,indent = 0, ensure_ascii=False)
    f.close()