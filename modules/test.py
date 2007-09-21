#!/usr/bin/python

from codes import *
from modules import func_module

class Test(func_module.FuncModule):
    def __init__(self):
        self.methods = {
            "test_add": self.add
        }
        func_module.FuncModule.__init__(self)

    def add(self, numb1, numb2):
        return numb1 + numb2

methods = Test()
register_rpc = methods.register_rpc