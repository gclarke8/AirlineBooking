""" Seating for Aircraft"""
from flight import *


class Layout:
    def __init__(self, registration, row, seat):
        self._row = row
        self._seat = seat
        self._registration = registration

    def registration(self):
        return self._registration

    def seatingPlan(self):
        return (range(1, self._row + 1)), "ABCDEFGHJKLMNOPQRSTU"[:self._seat]




