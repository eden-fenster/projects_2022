#!/usr/bin/env python3
from typing import List
import random


class Choose:
    @staticmethod
    def choose_random_snack(snacks: List[str]) -> str:
        return random.choice(snacks)
