"""
This file demonstrates common uses for the Python unittest module
https://docs.python.org/3/library/unittest.html
"""
import random
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

        self.morse_to_words = {
            "... --- ..." : "SOS",
            "--- -- .- .-.": "OMAR",
            "--... ...--" : "73",
            "-.-. --.-" : "CQ"
        }

    def test_encode_morse(self):
        for i in self.words_to_morse:
            self.assertEqual(morse_codec.encode_morse(i), self.words_to_morse[i])

    def test_decode_morse(self):
        for i in self.morse_to_words:
            self.assertEqual(morse_codec.decode_morse(i), self.morse_to_words[i].upper())


if __name__ == '__main__':
    unittest.main()
