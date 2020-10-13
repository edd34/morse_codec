import os
from time import sleep
time_unit = 0.1  # seconds
dot_length = time_unit
dash_length = 3*dot_length
freq = 440  # Hz
#os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))

def morse_code_to_beep(m_code):
    for symbol in list(m_code):
        print(symbol)
        if symbol == '.': #dot
            os.system('play -nq -t alsa synth {} sine {}'.format(dot_length, freq))
        elif symbol == '-': #dash
            os.system('play -nq -t alsa synth {} sine {}'.format(dash_length, freq))
        elif symbol == '/': #slash
            sleep(time_unit*7)
        elif symbol == ' ': #slash
            sleep(time_unit*3)