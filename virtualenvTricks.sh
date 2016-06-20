#!/bin/sh
#
# These commands will create a set of links for using "Virtually Python"
# Copyright: 2016 Brig Young, Sonophoto Studios
# License:   BSD 2-Clause, See LICENSE
#

# These paths should work on any ubuntu based system
virtualenv --system-site-packages --prompt="VIRTUAL-34g " --python=/usr/bin/python3.4 ~/.v34g/
virtualenv --system-site-packages --prompt="VIRTUAL-27g " --python=/usr/bin/python2.7 ~/.v27g/
virtualenv --prompt="VIRTUAL-34 " --python=/usr/bin/python3.4 ~/.v34/
virtualenv --prompt="VIRTUAL-27 " --python=/usr/bin/python2.7 ~/.v27/

# To use these links, type: 
# $> source ~/.P3g
# et cetera...
# remember to 
# $> deactivate
# when you are finished
ln ~/.v34g/bin/activate ~/.P3g
ln ~/.v27g/bin/activate ~/.P2g
ln ~/.v34/bin/activate ~/.P34
ln ~/.v27/bin/activate ~/.P27

# For more information see: 
# https://github.com/Sonophoto/PythonNotes/blob/master/virtualenvTricks.md
