===============
DetectMe Server
===============

DetectMe Server on Django 1.5.

The main responsabilities of this server are:

#. Share detectors between LabelMe Mobile (LMeMob) users
#. Get the real time detection of the LMeMob.
#. Output the video of the real time detection

*note: still under development*

1. Detector Sharing
===================

TBD.

2. Real Time Visualization
==========================

TBD.

3. Instruction to execute
=========================

Depending on the enviroment (development, staging, testing or production)
a different settings have to be loaded. To avoid having to add `--settings`
after each `django-admin.py` instruction, an alternative is to set the 
enviroment variable:

    $ export DJANGO_SETTINGS_MODULE=detectme.settings.local


