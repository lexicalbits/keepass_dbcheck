# -*- coding: utf-8 -*-
import sys
import time
from clint.textui import progress, colored, puts, puts_err
from .base import Reporter

LINE_CLEAR = ' ' * 80

class ConsoleReporter(Reporter):

    rate = .01

    def reset(self):
        #if hasattr(self, 'bar') and self.bar is not None:
            #self.bar.done()
        self.bar = progress.Bar(expected_size=self.password_count)
        self.tick = time.time()

    def needs_refresh(self):
        tick = time.time()
        d = tick - self.tick
        if d > self.rate:
            self.tick = tick
            return True
        return False

    def next_entry(self, entry_path, entry_password):
        puts(colored.blue("Testing {}".format(entry_path)))
        self.reset()

    def on_test(self, entry_path, entry_password, test_password, pw_counter):
        if pw_counter is not None and self.needs_refresh():
            self.bar.show(pw_counter)
            
    def result(self, entry_path, entry_password, is_match):
        puts_err("\r{}".format(LINE_CLEAR), newline=False)
        if is_match:
            puts(colored.red("\r{} has a guessable password!".format(entry_path)), newline=False)
        else:
            puts(colored.green("\r{} looks OK".format(entry_path)), newline=False)
        puts("")

    def summary(self, results):
        puts_err("\r{}".format(LINE_CLEAR), newline=False)
        if len(results) == 0:
            puts(colored.green("\r0/{} of your passwords are trivially guessable!".format(self.entry_count)))
        else:
            puts(colored.red(
                "\r{}/{} of your passwords are trivially guessable:".format(len(results), self.entry_count)))
            for result in results:
                puts(result[0])
