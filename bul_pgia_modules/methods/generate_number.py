#!/usr/bin/env python3
import random


class Generate:
    @staticmethod
    def generate_number(number_of_digits: int, can_repeat_digits: bool) -> str:
        i: int = 0
        number: str = ''
        if can_repeat_digits:
            while i < number_of_digits:
                if i == 0:
                    digit = random.randint(1, 9)
                    number += str(digit)
                else:
                    digit = random.randint(0, 9)
                    number += str(digit)
                i += 1
        else:
            while i < number_of_digits:
                if i == 0:
                    digit = random.randint(1, 9)
                    number += str(digit)
                else:
                    digit = random.randint(0, 9)
                    if str(digit) in number:
                        continue
                    else:
                        number += str(digit)

                i += 1
        return number
