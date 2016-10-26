# handy-dandy


Small useful programs that you feel like you should already have.

-----------------------------------------------------------------

### Batch Rename Filename
USAGE `python batch-rename-filenames.py [-tuleRnzxrqwapiI] <FILE/DIRECTORY> [<FILE/DIRECTORY>]`

`-t` : Title Case filename

`-u` : UPPERCASE filename

`-l` : lowercase filename

`-e` : lowercase extension

`-E` : UPPERCASE extension

`-n` : remove all non-numerical characters

`--alpha` : remove all non-letter ascii characters

`-z <NEW EXTENSION>` : change extension

`-x <PATTERN TO DELETE>` : delete all instances of pattern

`-r <PATTERN TO REPLACE | NEW PATTERN>` : replace all instaces of pattern, separated by ' | '

`-q <NUMBER OF CHARACTERS TO REMOVE>` : truncate filename from the left

`-w <NUMBER OF CHARACTERS TO REMOVE>` : truncate filename from the right

`-a <STRING>` : append string to filename

`-p <STRING>` : prepend string to filename

`-i <PADDING>` : leftwardly enumerate all files and apply padding to numbers (padding 3 -> 001)

`-I <PADDING>` : rightwardly enumerate all files and apply padding to numbers (padding 3 -> 001)


### Batch Rename Extensions
USAGE `python batch-rename-extensions.py` <FILE>