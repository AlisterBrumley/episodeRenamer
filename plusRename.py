import re
from pathlib import Path

filelist = sorted(Path.cwd().glob("*.*"), reverse=True)
episodecount = 1

for file in filelist:
    # getting episode string
    match = re.search(r"(E)(\d+)", str(file))
    if match is None:
        continue
    # splitting E(1) and number(2)
    epi_let = match.group(1)
    epi_num = match.group(2)
    # adding one
    epi_num = str(int(epi_num) + 1).zfill(2)
    # renaming
    renamed = re.sub(r"E\d+", epi_let + epi_num, str(file))
    # print(renamed)
    file.rename(renamed)
