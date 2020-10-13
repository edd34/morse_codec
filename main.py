#!/usr/bin/env python3
"""
Module Docstring
"""
import morse_codec
import beep

__author__ = "Eddine OMAR"
__version__ = "1.0.0"
__license__ = "MIT"


def main():
    """ Main entry point of the app """
    sentence = "SOS"
    print(sentence, morse_codec.encode_morse(sentence))
    beep.morse_code_to_beep(morse_codec.encode_morse(sentence))


if __name__ == "__main__":
    main()
