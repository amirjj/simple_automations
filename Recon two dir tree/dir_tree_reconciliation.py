from pathlib import Path
from collections import defaultdict


source_suffixes = ['.RPT']
dest_suffixes = ['.txt']

p = Path("..\searchfrom")
files = [x for x in p.iterdir() if x.is_file() and x.suffix in source_suffixes]

searchfrom = []
for file in files:
    with file.open() as f:
        lines = f.readlines()
        for line in lines[1:-1]:        
            searchfrom.append("IR"+line.split(",")[2])
            
searchin_db = defaultdict(list)
def append_dict(lines, filename):
    for line in lines:
        key = line.strip()
        searchin_db[key].append(filename)

p = Path("..\searchin")
files = [x for x in p.iterdir() if x.is_file() and x.suffix in dest_suffixes]
  
for file in files:
    with file.open() as f:
        lines = f.readlines()
        append_dict(lines, file)

        
if __name__ == "__main__":
    print("Source data count: " + str(len(searchfrom)))
    print("Search dataset count: " + str(len(searchin_db)))
    for serial in searchfrom:
        if serial in searchin_db:
            fn_str = " ".join([fn.name for fn in searchin_db[serial]])
            print(serial + ":" + fn_str)
