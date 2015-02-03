# -*- coding: utf-8 -*-
from clint.textui import progress, colored, puts
from .base import Reporter

class ConsoleReporter(Reporter):

    def reset(self):
        if hasattr(self, 'bar'):
            self.bar.done()
        self.bar = progress.Bar(expected_size=self.password_count)

    def next_entry(self, entry_path, entry_password):
        #print("Testing {0}".format(entry_path))
        puts(colored.blue("Testing{}".format(entry_path)))
        self.reset()

    def report(self, entry_path, entry_password, test_password, is_match, pw_counter=None):
        if pw_counter is not None:
            self.bar.show(pw_counter)

        if is_match:
            #print("\n{0} has a matching password".format(entry_path))
            puts(colored.red("{} has a matching password!".format(entry_path)))
            self.reset()
