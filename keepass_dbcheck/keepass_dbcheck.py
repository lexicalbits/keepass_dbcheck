# -*- coding: utf-8 -*-
import argparse
import getpass
import dbparser, pwparser, reporter

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
        kp = getattr(dbparser, keepass_parser)
        self.keepass_parser = kp(keepass_file, keyfile=keyfile)
        pp = getattr(pwparser, password_parser)
        self.password_parser = pp(password_file)
        o = getattr(reporter, output)
        self.output = o()

    def needs_password(self):
        return self.keepass_parser.needs_password()

    def set_password(self, password):
        self.keepass_parser.set_password(password)

    def run(self):
        self.output.set_scope(entry_count=self.keepass_parser.get_count(),
                password_count=self.password_parser.get_count())
        for path, pw in self.keepass_parser.get_all():
            self.output.next_entry(path, pw)
            lcpw = pw.lower();
            ctr = 0
            for testpw in self.password_parser.get_all():
                result = testpw.lower() == lcpw 
                self.output.report(path, pw, testpw, result, ctr)
                if result:
                    # No need to keep going, let's check the next password!
                    break
                ctr = ctr + 1



if __name__ == '__main__':
    run()
