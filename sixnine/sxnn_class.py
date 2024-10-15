# -*- coding: utf-8 -*-

class SixNine():
    sixnine: int = 69

    def __str__(self):
        return str(self.sixnine)

    @classmethod
    def int(self) -> int:
        return self.sixnine

    @classmethod
    def text(self) -> str:
        return "six nine"

    @classmethod
    def bin(self) -> str:
        return bin(self.sixnine)

    @classmethod
    def oct(self) -> str:
        return oct(self.sixnine)

    @classmethod
    def hex(self) -> str:
        return hex(self.sixnine)
