#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-06-20
Purpose: encryption_decryption
"""

# --------------------------------------------------
import argparse
import os
from string import ascii_lowercase
import ast


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
                        dest='encrypt',
                        default=True,
                        action='store_true')

    parser.add_argument('-d',
                        '--decrypt',
                        help='decrypt text',
                        dest='encrypt',
                        default=True,
                        action='store_false')

    parser.add_argument('-f',
                        '--file-dict',
                        help='Get Dict from file',
                        default='')

    parser.add_argument('-o',
                        '--outfile',
                        help='Write Dict to file',
                        default='')

    args = parser.parse_args()

    if os.path.isfile(args.transformation):
        args.transformation = open(args.transformation).read().rstrip()

    return args


def main() -> None:
    args = get_args()
    text: str = args.text
    transformation_pattern: str = args.transformation
    encrypt: bool = args.encrypt
    outfile = args.outfile

    dictionary: dict = create_dictionary(transformation_pattern=transformation_pattern, encrypt=encrypt)

    if outfile:
        out_fh = open(outfile, 'wt')
        out_fh.write(str(dictionary))
        out_fh.close()

    translated_text: str = translate_text(text_to_translate=text, dictionary=dictionary)
    print(translated_text)


def create_dictionary(transformation_pattern: str, encrypt: bool) -> dict:
    dictionary: dict = {}
    if encrypt:
        for i in range(0, len(transformation_pattern)):
            dictionary.update({ascii_lowercase[i]: transformation_pattern[i]})
    else:
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
