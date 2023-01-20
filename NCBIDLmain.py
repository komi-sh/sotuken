from NCBIDL import search
from NCBIDL import extract
from NCBIDL import dldata
import sys

if __name__ == '__main__':
    search.search(sys.argv[1])
    extract.extract()
    dldata.dlxml()
    dldata.dltxt()
    dldata.makecsv()

# "生物名（属、科など）[All Fields] AND たんぱく質名[Protein Name] NOT partial[All Fields]" 