# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod, abstractproperty
class DBParser(object):
    __metaclass__ = ABCMeta

    def __init__(self, keepass_file, keyfile=None):
        """
        Initialize a DB parser
        :param keepass_file: Path to the keepass file
        :param keyfile: An optional keyfile to access the database
        """
        self.path = keepass_file
        self.keyfile = keyfile

    def needs_password(self):
        """
        Check if the DB requires a password for access
        :return:
        """
        return self.keyfile is None

    def set_password(self, password):
        """
        Assign a password for the DB
        :param password:
        """
        self.password = password

    @abstractmethod
    def get_all(self):
        pass
