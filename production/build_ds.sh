### Run in the terminal by entering this file path (must be given execute permissions with chmod)
### requires a python 3 environment

#!/bin/sh
#source ../venv/bin/activate
set -e


############################################
###### generate ufo's and designspace ######


echo "Generating Designspace and UFOs"
fontmake -g fontmake_test.glyphs -o ufo
python3 designspace.py --helper helpers/*.designspace --output master_ufo/*.designspace 



###### generate ufo's and designspace ######
############################################




