# -*- coding: utf-8 -*-
from .base import PWParser
class PlainTextParser(PWParser):
    def get_all(self):
        with open(self.path, 'r') as f:
            for line in f:
                yield line.strip()
    def get_count(self):
        return sum(1 for line in open(self.path, 'r'))
