#!/usr/bin/env python3
"""
Module Docstring
"""
import morse_codec
import click
import beep

__author__ = "Eddine OMAR"
__version__ = "1.0.0"
__license__ = "MIT"


@click.command()
@click.option('-m', '--message', help="pass a message in the cli")
@click.option('--encode/--decode', default=True, help="encode or decode to/from morse")
@click.option('-f', '--filename', help="pass a file in the cli")
@click.option('-a', '--audio', is_flag=True, help="play the encoded morse message")
def main(message, filename, encode, audio):
    """ Main entry point of the app """
    data = ''
    res = None
    if(filename):
        try:
            file_content = open(filename)
            data = file_content.read()
        except FileNotFoundError:
            print('File {} not found'.format(filename))
            exit()
    elif(message):
        data = message
    else:
        print('Provide a message either with -m or -f option')
        exit()
    if(encode):
        res = morse_codec.encode_morse(data)
    else:
        res = morse_codec.decode_morse(data)
    print("Input: {}\nOutput: {}".format(data, res))
    if(audio and encode):
        beep.morse_code_to_beep(res)
    return 0


if __name__ == "__main__":
    main()
