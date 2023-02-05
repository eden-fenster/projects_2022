#!/usr/bin/env python3
class Range:

    def __init__(self, center: int, radius: int):
        self._center = center
        self._radius = radius

    def get_center(self) -> int:
        return self._center

    def get_radius(self) -> int:
        return self._radius
