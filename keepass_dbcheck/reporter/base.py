# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty

class Reporter(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.entry_count = None
        self.password_count = None

    def set_scope(self, entry_count, password_count):
        self.entry_count = entry_count
        self.password_count = password_count

    @abstractmethod
    def next_entry(self, entry_path, entry_password):
        pass
    @abstractmethod
    def report(self, entry_path, entry_password, test_password, is_match):
        pass
