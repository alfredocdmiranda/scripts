#!/usr/bin/python
# -*- coding: utf-8 -*-
__AUTHOR__ = "Alfredo Miranda <alfredocdmiranda@gmail.com>"
__DESCRIPTION__ =  "Encoder and decoder of morse code."

import sys

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
  	'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

def verify_encode(msg):
	keys = CODE.keys()
	for char in msg:
		if char.upper() not in keys and not char == ' ':
			raise BaseException("Error the character \"{0}\" cannot be translated to Morse Code".format(char))

def verify_decode(dic,search_code):
	for char,code in dic.iteritems():
		if code == search_code:
			return char
	raise BaseException("Error the code \"{0}\" cannot be translated to Morse Code".format(search_code))

def encoder(msg):
	verify_encode(msg)
	for char in msg:
		if char == ' ':
			print(' '*6),
		else:
			print(CODE[char] + " "*2),

def decoder(msg):
	msg = msg.split("       ")
	msg_encoded = []
	msg_decoded = ""
	for word in msg:
		msg_encoded.append(word.split(" "))

	for word_encoded in msg_encoded:
		for letter_encoded in word_encoded:
			msg_decoded += verify_decode(CODE,letter_encoded)
		msg_decoded += " "
	print(msg_decoded)

def main():
	"""
	Use the parameter -e to encode and -d to decode.
	Ex: morse_code.py -e (Alphabet to Morse Code)
	    morse_code.py -d (Morse Code to Alphabet)
	"""
	try:
		msg = raw_input('MESSAGE: ').upper()
		if sys.argv[1] == "-e":
			encoder(msg)
		elif sys.argv[1] == '-d':
			decoder(msg)
		else:
			print("Error: Don't have this option.'")
	except BaseException as error:
		print(error)

if __name__ == "__main__":
	main()
