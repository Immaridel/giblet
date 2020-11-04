#!/bin/bash

#--------------------------------------------------------------------------------------------------------------
# Because Python3 is not native to Centos6, you need to do the below to enter the correct environment to use it.
# Once you run this, you can install modules with pip/pip3 (same thing).  This will NOT disrupt Python2's env.
#
# > scl enable rh-python35 bash
#
#--------------------------------------------------------------------------------------------------------------

scl enable rh-python35 "PYTHONPATH=/opt/rh/rh-python35/root/usr/lib/python3.5/site-packages python /root/gibletPython/bot.py"
