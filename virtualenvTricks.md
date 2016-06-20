      __     ___      _               _ _           ____        _   _                 
      \ \   / (_)_ __| |_ _   _  __ _| | |_   _    |  _ \ _   _| |_| |__   ___  _ __  
       \ \ / /| | '__| __| | | |/ _` | | | | | |   | |_) | | | | __| '_ \ / _ \| '_ \ 
        \ V / | | |  | |_| |_| | (_| | | | |_| |   |  __/| |_| | |_| | | | (_) | | | |
         \_/  |_|_|   \__|\__,_|\__,_|_|_|\__, |   |_|    \__, |\__|_| |_|\___/|_| |_|
                                          |___/           |___/                       

###A Virtual Environment Trick using virtualenv 

***Full Disclosure (YMMV):***

_virtualenv_

      --version: 15.0.2
      
_Mint 17.1 MATE_

      uname: Linux [hostname] 3.13.0-37-generic #64-Ubuntu SMP [datetime] i686 athlon i686 GNU/Linux
      
_Python 2.7 Package Installed_ 

      --version: Python 2.7.6
      
_Python 3.4 Package Installed_

      --version: Python 3.4.3
      
_using /bin/bash -l_

      --version: GNU bash, version 4.3.11(1)-release
      

***USE CASE:*** 

(Yes, this may make _you_ yawn, but I think this is the coolest thing since Algol.)

Learning both Python 2.7 and Python 3.4 is a pain. Naturally we want to 
act as if the version we are using is the actual system version without all of 
the hassle of typing numbers after all of our commands and the hassle of system
and version conflicts with Python libraries.

Python 3.x is here to stay! It is definitely worth the effort with more consistency
in language syntax and enhanced functionality.

These "Macros" make it much easier to use whichever version you wish and change 
from minute to minute! This method INCLUDES your regular installed system 
libraries automagiacally! ***Or*** lets you use a bare environment and only 
add what you want at the moment...
                                        ...and change your mind later!

             ***_It Unixishy!_*** (hard to type, easy to forget, utterly cryptic...)

***In my home directory I created four virtualenv directories:***

_Note the_ ***'g'*** _on the end of these directory names and prompt strings!_

      virtualenv --system-site-packages --prompt="VIRTUAL-34g " --python=/usr/bin/python3.4 ~/.v34g/
      virtualenv --system-site-packages --prompt="VIRTUAL-27g " --python=/usr/bin/python2.7 ~/.v27g/

_Note there is_ ***NO*** 'g' _on the end of these directory names and prompt strings!_

      virtualenv --prompt="VIRTUAL-34 " --python=/usr/bin/python3.4 ~/.v34/
      virtualenv --prompt="VIRTUAL-27 " --python=/usr/bin/python2.7 ~/.v27/


***Next we create links***

      ln ~/.v34g/bin/activate ~/.P3g
      ln ~/.v27g/bin/activate ~/.P2g
      ln ~/.v34/bin/activate ~/.P34
      ln ~/.v27/bin/activate ~/.P27

***Now from anywhere we are we can use one of four python virtual environments by saying:

        $> source ~/.P3g  # Now we are in a virtual 3.4 environment
                            with ALL of our version 3.4 system libraries
        $> python --version
        Python 3.4.3
        $> pip --version
        pip 8.1.2 from [path_spec]python3.4/site-packages (python 3.4)
        $> pip freeze
        [system_libraries]
       
***Now lets switch to Python 2.7 with a bare system (no libraries installed)***

        $> deactivate     # Leave the Python 3.4 virtual environment, 
                            System's default Python is restored
        $> source ~/.P27  # Now we are in a virtual Python 2.7
                            with NO system libraries
        $> python --version
        Python 2.7.6
        $> pip --version
        pip 8.1.2 from [path_spec]python2.7/site-packages (python 2.7)
        $> pip freeze
        [None]
        $> deactivate
        
        ... and we are back at the system's version which can be whatever, we don't care ;-)
       
 
***NOTE!*** Your project DOES NOT have to be in the .vxxg or .vxx directories it can be anywhere...

***BUT:*** Remember, your "no library" versions will come back up with whatever libraries you do
install in them if you do not explicitly delete them with pip... 

To maintain a specific virtual environment you should create a specific setup of virtualenv just
for your project and keep all of your files in THAT directory with your requirements.txt etc.
Activate this specific environment to work on that specific project.
        
#It Works Great!
