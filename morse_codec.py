"""
Module morsecodec
"""

char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

dots_to_char = {v: k for k, v in char_to_dots.items()}

def encode_morse(sentence):
    '''Takes a sentence as argument, return an encoded morse code'''
    upper_sentence = sentence.upper()
    res = ""
    for char in upper_sentence:
        if not char in char_to_dots.keys():
            return -1
        res += (char_to_dots[char]) + ' '
    return res[:-1]

def decode_morse(morse_code):
    '''Takes a morse code as argument, return a plain text decoded'''
    res = ""
    for char in morse_code.split(' '):
        if not char in dots_to_char.keys():
            return -1
        res += (dots_to_char[char])
    return res
