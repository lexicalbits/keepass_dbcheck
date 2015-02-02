# -*- coding: utf-8 -*-
from .base import Reporter

class ConsoleReporter(Reporter):

    def report(self, entry_path, entry_password, test_password, is_match):
        if is_match:
            print("{0} has a matching password".format(entry_path))
