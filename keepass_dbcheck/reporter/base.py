# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty

class Reporter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def report(self, entry_path, entry_password, test_password, is_match):
        pass
