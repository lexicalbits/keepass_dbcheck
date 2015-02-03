# -*- coding: utf-8 -*-
import os.path
from kppy.database import KPDBv1
from .base import DBParser

class KPPYParser(DBParser):

    @classmethod
    def get_kppy_entry_path(cls, entry):
        """
        Generate a full "path" for a keepass entry that includes titles for it and its parent group(s)
        :param entry: Which entry to process
        :return: String like {group}/{subgroup}/{entry}
        """
        path = [entry.title]
        g = entry.group
        while(g):
            if g.title:
                path.append(g.title)
            g = g.parent
        path.reverse()
        return "/".join(path)

    def load(self):
        """
        Load the keepass database into memory for processing
        :raise IOError: Fails if the file doesn't exist
        """
        if not hasattr(self, 'reader'):
            if not os.path.isfile(self.path):
                raise IOError('No such keepass file {}'.format(self.path))
            self.reader = KPDBv1(filepath=self.path, read_only=True, keyfile=self.keyfile,
                    password=self.password)
            self.reader.load()

    def get_all(self):
        """
        Loop through every entry in the database and yield it
        :return: Iterator tuple of path, password
        """
        self.load()
        for entry in self.reader.entries:
            if entry.title == 'Meta-Info':
                continue
            path = self.get_kppy_entry_path(entry)
            yield path, entry.password

    def get_count(self):
        """
        Gets a count of entries in the database
        :return: Integer count
        """
        self.load()
        return len(self.reader.entries)
