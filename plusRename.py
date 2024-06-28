import re
from pathlib import Path

filelist = sorted(Path.cwd().glob("*.*"))
episodecount = 1

for file in filelist:
    # getting episode string
    match = re.search(r"(E)(\d+)", str(file))
    # splitting E and number
    epi_let = match.group(1)
    epi_num = match.group(2)
    # adding one
    epi_num = str(int(epi_num) + 1)
    # renaming
    renamed = re.sub(r"E\d+", epi_let + epi_num, str(file))
    file.rename(renamed)
