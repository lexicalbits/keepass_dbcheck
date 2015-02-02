# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
class PWParser(object):
    __metaclass__ = ABCMeta

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def get_count(self):
        pass
