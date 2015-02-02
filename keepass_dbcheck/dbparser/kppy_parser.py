# -*- coding: utf-8 -*-
import os.path
from kppy.database import KPDBv1
from .base import DBParser

class KPPYParser(DBParser):

    @classmethod
    def get_kppy_entry_path(cls, entry):
        path = [entry.title]
        g = entry.group
        while(g):
            if g.title:
                path.append(g.title)
            g = g.parent
        path.reverse()
        return "/".join(path)

    def load(self):
        if not hasattr(self, 'reader'):
            if not os.path.isfile(self.path):
                raise IOError('No such keepass file {}'.format(self.path))
            self.reader = KPDBv1(filepath=self.path, read_only=True, keyfile=self.keyfile,
                    password=self.password)
            self.reader.load()

    def get_all(self):
        self.load()
        for entry in self.reader.entries:
            if entry.title == 'Meta-Info':
                continue
            path = self.get_kppy_entry_path(entry)
            yield path, entry.password

    def get_count(self):
        self.load()
        return len(self.reader.entries)
