### plusRename
takes every episode in directory and adds one to it's episode count

### seRename
globs directories in a directory, and renames episodes with correct SXXEXX if they're currently S01EXX

eg
```
TV_SHOW/
|____S1/
   |  |____SHOW_S01E01.MP4
   |  |____SHOW_S01E02.MP4
   |____S2/
      |____SHOW_S01E03.MP4
      |____SHOW_S01E04.MP4
```
will become
```
TV_SHOW/
   |____S1/
   |  |____SHOW_S01E01.MP4
   |  |____SHOW_S01E02.MP4
   |____S2/
      |____SHOW_S02E01.MP4
      |____SHOW_S02E02.MP4
```
