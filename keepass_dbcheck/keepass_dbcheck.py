# -*- coding: utf-8 -*-
import os
import argparse
import getpass
import dbparser, pwparser, reporter

def fixpath(path):
    return os.path.abspath(os.path.expanduser(path)) if isinstance(path, basestring) else None

def run():
    """
    Process command-line arguments and execute our actions
    :rtype : None
    """
    cli = argparse.ArgumentParser(description="Check your keepass passwords against a list of known passwords")
    cli.add_argument('--keepass_parser', default='kppy', choices=['kppy'],
                           help='Which keepass library to use (default kppy is best for Keepass v1)')
    cli.add_argument('--password_parser', default='plaintext', choices=['plaintext'],
                           help='How the given password file should be read')
    cli.add_argument('-p', '--password_file', required=True,
                           help='Path to the file containing the passwords we want to check against')
    cli.add_argument('-f', '--keepass_file', required=True,
                           help='Path to your keepass db')
    cli.add_argument('-k', '--keyfile', required=False,
                           help='Keyfile for the db (will prompt for password if not provided)')
    cli.add_argument('-o', '--output', default='console', choices=['console'],
                           help='How to view the results - defaults to echoing the names of all hits to the console')
    args = cli.parse_args()
    checker = KeepassChecker(**vars(args))
    if checker.needs_password():
        checker.set_password(getpass.getpass(prompt='Keepass password: '))
    checker.run()

class KeepassChecker(object):
    def __init__(self, keepass_file, password_file, keyfile=None, keepass_parser='kppy', password_parser='plaintext',
                 output='console'):
        """
        Create a checker that matches a password file against a keepass database and outputs the results
        :param keepass_file: The path to the keepass file (required)
        :param password_file: The path to the password list (requried)
        :param keyfile: The optional keyfile for use in the
        :param keepass_parser: Which keepass library to use to interact with the database (currently only kppy)
        :param password_parser: What format the password file is in (currently only plaintext)
        :param output: Where the output should go (currently only console)
        """
        kp = getattr(dbparser, keepass_parser)
        self.keepass_parser = kp(fixpath(keepass_file), keyfile=fixpath(keyfile))
        pp = getattr(pwparser, password_parser)
        self.password_parser = pp(fixpath(password_file))
        o = getattr(reporter, output)
        self.output = o()

    def needs_password(self):
        """
        Check to see if the database might need a password.  Always true if you didn't provide a keyfile.
        :return: True if you should add a password to this checker
        """
        return self.keepass_parser.needs_password()

    def set_password(self, password):
        """
        Assign an optional password to the keypass parser.  This is only necessary if the file doesn't use a keyfile.
        :param password: Password for the keepass database
        """
        self.keepass_parser.set_password(password)

    def run(self):
        """
        Initialize the matching process.
        """
        self.output.set_scope(entry_count=self.keepass_parser.get_count(),
                password_count=self.password_parser.get_count())
        bad = []
        for path, pw in self.keepass_parser.get_all():
            self.output.next_entry(path, pw)
            lcpw = pw.lower();
            ctr = 0
            match = False
            for testpw in self.password_parser.get_all():
                self.output.on_test(path, pw, testpw, ctr)
                match = testpw.lower() == lcpw 
                if match:
                    bad.append([path, pw])
                    break
                ctr = ctr + 1
            self.output.result(path, pw, match)
        self.output.summary(bad)



if __name__ == '__main__':
    run()
