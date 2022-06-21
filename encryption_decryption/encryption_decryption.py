#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-06-20
Purpose: encryption_decryption
"""

# --------------------------------------------------
import argparse
from dataclasses import dataclass
import random
from string import ascii_lowercase
from typing import Dict


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='encryption_decryption',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input text',
                        metavar='Input text')

    parser.add_argument('transformation',
                        help='Transformation pattern',
                        metavar='Transformation pattern')

    parser.add_argument('-e',
                        '--encrypt',
                        help='encrypt text',
                        type=bool,
                        default=False)

    parser.add_argument('-d',
                        '--decrypt',
                        help='decrypt text',
                        type=bool,
                        default=False)

    return parser.parse_args()


def main() -> None:
    args = get_args()
    text: str = args.text
    transformation_pattern: str = args.transformation
    encrypt: bool = args.encrypt
    decrypt: bool = args.decrypt
    dictionary: Dict[str] = create_dictionary(transformation_pattern=transformation_pattern,
                                              encrypt=encrypt, decrypt=decrypt)
    translated_text: str = translate_text(text_to_translate=text, dictionary=dictionary)
    print(translated_text)
    pass


def create_dictionary(transformation_pattern: str, encrypt: bool, decrypt: bool) -> dict:
    dictionary: Dict[str] = {}
    if encrypt:
        for i in range(0, len(transformation_pattern)):
            dictionary.update({ascii_lowercase[i]: transformation_pattern[i]})
    if decrypt:
        for i in range(0, len(ascii_lowercase)):
            dictionary.update({transformation_pattern[i]: ascii_lowercase[i]})
    return dictionary


def translate_text(text_to_translate: str, dictionary: dict) -> str:
    new_text: str = ''
    for letter in text_to_translate:
        new_text += dictionary.get(letter, letter)
    return new_text


if __name__ == '__main__':
    main()
