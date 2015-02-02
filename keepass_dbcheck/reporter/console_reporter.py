# -*- coding: utf-8 -*-
import sys
from .base import Reporter

class ConsoleReporter(Reporter):

    def reset(self):
        self.counter = 0

    def next_entry(self, entry_path, entry_password):
        print("\nTesting {0}".format(entry_path))

    def report(self, entry_path, entry_password, test_password, is_match, pw_counter=None):
        if pw_counter is not None:
            strmax = len(str(self.password_count))
            strctr = str(pw_counter + 1).zfill(strmax)
            sys.stdout.write("\r{0}/{1}".format(strctr, self.password_count))
            sys.stdout.flush()

        if is_match:
            print("{0} has a matching password".format(entry_path))
            self.reset()
