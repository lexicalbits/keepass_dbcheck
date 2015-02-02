# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
class DBParser(object):
    __metaclass__ = ABCMeta

    def __init__(self, keepass_file, keyfile=None):
        self.path = keepass_file
        self.keyfile = keyfile

    def needs_password(self):
        return self.keyfile is None

    def set_password(self, password):
        self.password = password

    @abstractmethod
    def get_all(self):
        pass
