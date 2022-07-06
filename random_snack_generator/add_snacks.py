#!/usr/bin/env python3
from typing import List


def add_snacks(snacks: str) -> List[str]:
    number_of_snacks: int = len(snacks)
    snacks_in_house: List[str] = []
    if number_of_snacks == 1:
        snacks_in_house.append(snacks[0])
    if number_of_snacks > 1:
        for snack in snacks:
            snacks_in_house.append(snack)
    return snacks_in_house
