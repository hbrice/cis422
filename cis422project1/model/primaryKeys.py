__author__ = 'lucasr'
import random

class primaryKeys(object):

    def __init__(self):
        self.rands = range(1,500)
        random.shuffle(self)

    def retrievePrimaryKey(self):
        return self.rands.pop()
