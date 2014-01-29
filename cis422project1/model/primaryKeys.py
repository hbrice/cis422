__author__ = 'lucasr'
import random

class primaryKeys(object):
    rands = range(1,500)
    random.shuffle(rands)

    @staticmethod
    def retrievePrimaryKey(self):
        return self.rands.pop()
