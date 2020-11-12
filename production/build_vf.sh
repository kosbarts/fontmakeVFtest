### Run in the terminal by entering this file path (must be given execute permissions with chmod)
### requires a python 3 environment

#!/bin/sh
#source ../venv/bin/activate
set -e


############################################
#### generate variable fonts ####



echo "Generating VFs"
mkdir -p ../fonts/variable

# fontmake -m master_ufo/AllenteSans.designspace -o variable --output-path ../fonts/variable/AllenteSansVF.ttf
fontmake -m master_ufo/FontmakeTest.designspace -o variable --output-path ../fonts/variable/FontmakeTestVF.ttf
rm -rf instance_ufo/ #master_ufo/  #deletes only the instances which we don't need


#### generate variable fonts ####
############################################






