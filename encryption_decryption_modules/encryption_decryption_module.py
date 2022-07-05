#!/usr/bin/env python3
"""
Author : eden <eden@localhost>
Date   : 2022-07-05
Purpose: encryption_decryption
"""

# --------------------------------------------------
import argparse
import os
from create_dictionary import create_dictionary as create_dictionary
from translate_text import translate_text as translate_text


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


if __name__ == '__main__':
    main()
