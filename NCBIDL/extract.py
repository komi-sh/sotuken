from collections import defaultdict
import datetime
import json

def extract():
    f = open("./NCBIDLout/search.json","r")
    records = json.load(f)
    f.close()

    info = defaultdict(list) # (key,value) = (organism,[Accession,update-date,ID])

    for r in records:
        if r["GBSeq_organism"] in info:
            firsttime = datetime.datetime.strptime(str(r['GBSeq_update-date']),"%d-%b-%Y")
            secondtime = datetime.datetime.strptime(str(info[r["GBSeq_organism"]][1]),"%d-%b-%Y")
            if firsttime > secondtime:
                info[r["GBSeq_organism"]][0] = r["GBSeq_primary-accession"]
                info[r["GBSeq_organism"]][1] = r["GBSeq_update-date"]
                info[r["GBSeq_organism"]][2] = r["GBSeq_definition"]
        else:
            info[r["GBSeq_organism"]].append(r["GBSeq_primary-accession"])
            info[r["GBSeq_organism"]].append(r["GBSeq_update-date"])
            info[r["GBSeq_organism"]].append(r["GBSeq_definition"])

    a = sorted(info.items()) # sort後はtaple
    info_s = dict((x, y) for x, y in a) # 辞書に戻す

    f = open("./NCBIDLout/extract.json","w")
    json.dump(info_s,f,indent = 0,ensure_ascii=False)
    f.close()