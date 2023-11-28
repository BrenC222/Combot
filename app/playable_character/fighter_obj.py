import os
import sys

class Fighter:

    def __init__(self, data=None):
        self.data = data
        self.name = None
        self.moveset = None
        if self.data:
            self.load_data()

    # CHORE get the name and moveset from python dict and set self.name and self.moveset
    def load_data(data=None):
        if data:
            self.data = data
        else:
            raise ValueError("Error python dict required")
