"""
Student Name: Boyang Yan
Student Number: 200495053
"""

from typing import Any

class THE:
    def __init__(self) -> None:
        self._slot = None
        pass
    def set(self, slot):
        self._slot = slot
    
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == "_slot":
            super().__setattr__(__name, __value)
        else:
            self._slot.__setattr__(__name, __value)
    
    def __getattr__(self, __name: str) -> Any:
        if __name != "_slot":
            return self._slot.__getattr__(__name)
        else:
            return None

the = THE()
