# -*- coding: utf-8 -*-
from .base import DBParser
from kppy.database import KPDBv1

class KPPYParser(DBParser):

    @classmethod
    def get_kppy_entry_path(cls, entry):
        path = []
        g = entry.group
        while(g):
            path.append(g.title)
            g = g.parent
        return "/".join(path.reverse())

    def get_all(self):
        if not self.reader:
            self.reader = KPDBv1(filepath=self.path, read_only=True, keyfile=self.keyfile,
                    password=self.password)
        for entry in self.reader.entries:
            path = self.get_kppy_entry_path(entry)
            yield path, entry.password
