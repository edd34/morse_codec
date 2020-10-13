# Morse Codec
Morse Codec is a python library intended to encode and decode word to morse code and vice versa. It can also generate beep according to a given morse code.

## Installation (optionnal)
If you want to use the beep feature, please install sox on your computer :

* On Debian / Ubuntu / Linux Mint, run this in your terminal:

```
sudo apt install sox
```
* On Mac, run this in your terminal (using macports):
```
sudo port install sox
```
## Usage

```python
import morse_codec, beep
sentence = "SOS"
print(sentence, morse_codec.encode_morse(sentence))
beep.morse_code_to_beep(morse_codec.encode_morse(sentence))
```

## Test
```python
python3 test.py
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
