===============================
Keepass DB Checker
===============================

Check your keepass v1/keepassx - stored passwords against a list of common passwords.


Basic Usage
-----------
First, you'll need to get your hands on a list of passwords.  One easily available set is here:

http://sourceforge.net/projects/cracklib/files/cracklib-words/2008-05-07/cracklib-words-20080507.gz/download

Once you do, you simply use the following bash command::

    python keepass_dbcheck.py -f /path/to/passwords.kdb -p /path/to/passwordlist

The script will loop through your passwords and look for matches in the password list.  It'll warn you
of matches as it finds them and give you a summary at the end.

Advanced Usage
--------------
**Expanded database access**

My passwords are in keepass v1, so I built this using software that knew how to talk to those files.
If you need to access v2 files, it should be simple to integrate another python/keepass library into
this tool (see *customization* below)

Once you add your library, just tell the program you want to use it by adding your wrapper to 
dbparser/__init__.py and passing the scoped variable into the python command::

    # In dbparser/__init__.py
    from .your_parser import YourParser as yourp

    # In the console
    python keepass_dbcheck.py -f /path/to/passwords.kdb -p /path/to/passwordlist \
           --keepass-parser=yourp


**Alternate password formats**

If you come across another good list of sample passwords, first of all, let me know!  Second, if it happens
to use a more complicated format than one-password-per-line of plain text, you should be able to easily
add a parser that will handle the new format (see *customization* below)

Once you add your library, just tell the program you want to use it by adding your wrapper to 
pwparser/__init__.py and passing the scoped variable into the python command::

    # In pwparser/__init__.py
    from .your_parser import YourParser as yourp

    # In the console
    python keepass_dbcheck.py -f /path/to/passwords.kdb -p /path/to/passwordlist \
           --password-parser=yourp


**Alternate output**
The default output of the application is designed to be viewed during an interactive console session.
If you want to change how the output works - say, to make something more script-friendly - you can easily
add your own reporter (see *customization* below)

Once you add your library, just tell the program you want to use it by adding your wrapper to 
reporter/__init__.py and passing the scoped variable into the python command::

    # In reporter/__init__.py
    from .your_parser import YourParser as yourp

    # In the console
    python keepass_dbcheck.py -f /path/to/passwords.kdb -p /path/to/passwordlist \
           --output=yourp


Customization
-------------
I tried to make this app as flexible as possible.  Do do that, most of the major components are abstracted
and isolated into subpackages for easy expansion: password parsing in /pwparser, database processing in 
/dbparser, and output in /reporter.

Each subpackage has a class in .base that defines the interface between the main script and the component.
Simply subclass that base class, add a command-line-friendly reference in the subpackage's __init__.py file,
and pass that reference into the appropriate script parameter::

    python keepass_dbcheck.py -f /path/to/passwords.kdb -p /path/to/passwordlist \
        --keepass-parser=your_keepass_parser \
        --password-parser=your_password_parser \
        --output=your_reporter


Future wishlist
---------------
* Add extra checks to see if your password is made of easily recompiled word fragments in the keepass entry's
  username and URL fields
* Add a script-friendly reporter
* Capture and normalize exceptions in the dbparser subpackage so other libraries' errors can be standardized
* Modularize the actual password check project so other sanity checks (password length, basic personal
  information, etc.) can be added as time goes on


License
-------
BSD license, go nuts!
