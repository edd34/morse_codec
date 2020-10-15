"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import unittest
import morse_codec

class TestSequenceFunctions(unittest.TestCase):
    """ This is one of potentially many TestCases """

    def setUp(self):
        self.words_to_morse = {
            "SOS" : "... --- ...",
            "Bonjour" : "-... --- -. .--- --- ..- .-.",
            "Eddine" : ". -.. -.. .. -. .",
            "73" : "--... ...--",
            "CQ" : "-.-. --.-"
        }

        self.morse_to_words = {v: k for k, v in self.words_to_morse.items()}

    def test_encode_morse(self):
        '''Test function encode morse '''
        for i in self.words_to_morse:
            self.assertEqual(morse_codec.encode_morse(i), self.words_to_morse[i])

    def test_decode_morse(self):
        '''Test function decode morse '''
        for i in self.morse_to_words:
            self.assertEqual(morse_codec.decode_morse(i), self.morse_to_words[i].upper())


if __name__ == '__main__':
    unittest.main()
