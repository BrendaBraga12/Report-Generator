from typing import Protocol

class Report(Protocol):


    def meth(self)->str:
        return Report