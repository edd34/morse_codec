"""
Module beep
This module enable beep generation from the python program
"""

import os
from time import sleep
TIME_UNIT = 0.1  # seconds
DOT_LENGTH = TIME_UNIT
DASH_LENGTH = 3*DOT_LENGTH
FREQ = 440  # Hz
#os.system('play -nq -t alsa synth {} sine {}'.format(duration, FREQ))

"""
Function morse_code_to_beep
arg : m_code a valid morse code
return : None
desc : generate beep according to morse code
"""
def morse_code_to_beep(m_code):
    '''Take a morse code'''
    for symbol in list(m_code):
        print(symbol)
        if symbol == '.': #dot
            os.system('play -nq -t alsa synth {} sine {}'.format(DOT_LENGTH, FREQ))
        elif symbol == '-': #dash
            os.system('play -nq -t alsa synth {} sine {}'.format(DASH_LENGTH, FREQ))
        elif symbol == '/': #slash
            sleep(TIME_UNIT*7)
        elif symbol == ' ': #slash
            sleep(TIME_UNIT*3)
