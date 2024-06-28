#
#
# THIS SCRIPT RENAMES FILES IN SXXEXX ORDER
# TO BE USED FOR SHOWS WHERE ALL EPISODES ARE S01EXX
# PUT EPISODES INTO SEASON FOLDERS AND THEN RUN FROM SHOW FOLDER
# EG
# TV_SHOW/   < RUN HERE
#   |____S1/
#   |  |____SHOW_S01E01.MP4
#   |  |____SHOW_S01E02.MP4
#   |____S2/
#      |____SHOW_S01E03.MP4
#      |____SHOW_S01E04.MP4
#
#
# WILL BECOME
# TV_SHOW/
#   |____S1/
#   |  |____SHOW_S01E01.MP4
#   |  |____SHOW_S01E02.MP4
#   |____S2/
#      |____SHOW_S02E01.MP4
#      |____SHOW_S02E02.MP4
#
#
import re
from pathlib import Path

filelist = sorted(Path.cwd().rglob("*.*"))
seriesCount = "1"
episodeCount = 1

for file in filelist:
    seriesDir = file.parent.name[1]

    if not seriesDir.isnumeric():
        continue
    elif seriesCount < seriesDir:
        seriesCount = seriesDir
        episodeCount = 1

    series = "S0" + seriesCount
    episode = "E0" + str(episodeCount)
    renamed = re.sub(r"S0\dE\d+", series + episode, str(file))
    file.rename(renamed)
    print(renamed)
    episodeCount += 1

# WORKS IF RAN FROM VIDEO FILE DIR
# TODO
# ADD TYPER OPTIONS
# TEST MODE THAT DUMPS FILEAMES INSTEAD OF RENAMING
# MAYBE NOT RGLOB
# RUN CHECKS FOR DIFFERENT S##E## STRNGS
# IF 3 DIGIT EPISODE COUNT, MAKE ALL 3 DIGIT