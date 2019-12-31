#!/bin/sh
#
# These commands will create a set of links for using "Virtually Python"
# https://github.com/Sonophoto/PythonNotes/blob/master/virtuallyPython.md
#
# USAGE: ./virtuallyPython.sh [alias | help]
#    [alias] appends a set of aliases to your ~/.bashrc
#    [help]  prints a detailed usage screen
#
# Copyright: 2016,2017 Brig Young, Sonophoto Studios
# License:   BSD 2-Clause: If you use it, cite it! --thanks.
# See LICENSE file: https://github.com/Sonophoto/PythonNotes/LICENSE
#


# Where can we find python2.7 and python3.x?
#TODO Add tests for Python2 and Python3 in our check_dependencies()
python27_path="/usr/bin/python2.7"
python3_path="/usr/bin/python3.5"

# prompt and install directory for python2.7 with no modules installed
prompt_v27s="VIRTUAL-27s "
dir_py27slick="$HOME/.v27s"
alias_py27slick="py2s"

# prompt and install directory for python3.x with no modules installed
prompt_v3s="VIRTUAL-35s "
dir_py3slick="$HOME/.v3s"
alias_py3slick="py3s"

# prompt and install directory for python2.7 with all OS installed python2.7 modules
prompt_v27g="VIRTUAL-27g "
dir_py27global="$HOME/.v27g"
alias_py27global="py2g"

# prompt and install directory for python3.x with all OS installed python3.x modules
prompt_v3g="VIRTUAL-35g "
dir_py3global="$HOME/.v3g"
alias_py3global="py3g"


check_dependencies () {
   #TODO Add tests for Python2 and Python3
   echo "Checking for virtualenv and version number"
   virtualenv --version
   if [ $? != 0 ]
   then
      User_Response=""
      echo "virtualenv is NOT installed. Shall we install it? (yes or no)"
      read User_Response
      echo "Got a User_Response of $User_Response"
      case "$User_Response" in
         [Yy]*)
            sudo apt install virtualenv
         ;;
         *)
            echo "virtuallyPython.sh requires virtualenv"
            echo "Get more info at: https://pypi.python.org/pypi/virtualenv"
            echo ""
            echo "Download virtualenv and install to continue..."
            exit 1
         ;;
       esac
   fi
}


print_usage () {
cat << EOF
Warning: Paths in this script must be ported on non-ubuntu based systems

Usage: ./virtuallyPython.sh [--alias | --help]

No Options: creates and initializes all four virtual environments for manual usage.

alias: Append the aliases $alias_py27slick, $alias_py3slick, $alias_py27global,
       $alias_py3global and dvirt to your .bashrc.
       These allow fast, single command access to swithching Python versions
       Inside the virtual environment python is ALWAYS named "python"

       $alias_py27slick: This is python2.7 with a BARE library installation
       $alias_py3slick: This is python3.5 with a BARE library installation
       $alias_py27global: This is python2.7 with all OS installed Python 2.7 libraries
       $alias_py3global: This is python3.5 with all OS installed Python 3.5 libraries
       dvirt: Exits the virtual environment. Make sure you exit each environment
              before you change to the next or you will next environments inside
              each other which works, unfortunately for your sanity.

 help: Displays this message and exits cleanly

Author: Brig Young; Official Source: http://https://github.com/Sonophoto/PythonNotes/
There should also be a file named README.md with more detailed info

EOF
}


create_virtual_envs () {
   virtualenv --prompt=$prompt_v27s --python=$python27_path $dir_py27slick
   virtualenv --prompt=$prompt_v3s --python=$python3_path $dir_py3slick
   virtualenv --system-site-packages --prompt=$prompt_v27g --python=$python27_path $dir_py27global
   virtualenv --system-site-packages --prompt=$prompt_v3g --python=$python3_path $dir_py3global
}


create_aliases () {
   # NOTE you cannot put these in a shell script, it must be sourced in process!
   echo "alias $alias_py27slick='source $dir_py27slick/bin/activate'" >> ~/.bashrc
   echo "alias $alias_py3slick='source $dir_py3slick/bin/activate'" >> ~/.bashrc
   echo "alias $alias_py27global='source $dir_py27global/bin/activate'" >> ~/.bashrc
   echo "alias $alias_py3global='source $dir_py3global/bin/activate'" >> ~/.bashrc
   echo "alias dvirt='deactivate'" >> ~/.bashrc
   echo ""
   echo "***** You must run 'source $HOME/.bashrc' to load your aliases *****"
   echo "***** If you want to use them immediately.                     *****"

}


# "Main" function

# Lets see if we have any options requested, there should only be one or zero args
if [ $# -gt 1 ];
then # Too Many args
   echo "***** ERROR! *****"
   echo "Not Running: Too Many Arguments! = $#, $@"
   print_usage
   exit 1
fi

# We have zero or one argument, lets see what it is
if [ $# -eq 1 ];
then

   if [ "$1" = "--help" -o  "$1" = "-h" -o "$1" = "help" ];
   then
      echo "Running with print_usage argument => $1"
      print_usage
      exit 0

   elif [ "$1" = "--alias" -o "$1" = "-a" -o "$1" = "alias" ];
   then
      echo "Running with create_aliases => $1"
      check_dependencies
      create_virtual_envs
      create_aliases
      exit 0

   else # Bad Argument
      echo "***** ERROR! *****"
      echo "Not Running: Bad Argument = $1"
      print_usage
      exit 1
   fi

else # $? = 0, No Arguments
   echo "Running with zero arguments."
   check_dependencies
   create_virtual_envs
   exit 0
fi

