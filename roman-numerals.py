#!/usr/bin/env python

'''
Roman Numeral & Decimal Converter
Created by Anurag Banerjee.
Copyright 2016. All rights reserved.

USAGE `python roman-numerals.py <ROMAN NUMERAL or DECIMAL NUMBER>`

'''

from sys import argv

def show_info():
	print "Roman Numeral & Decimal Converter"
	print "USAGE: roman-numerals.py <ROMAN NUMERAL or DECIMAL NUMBER>"

def convert_to_roman(decimal):
	## decimal to roman
	conversionTable = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	irregulars = {"IV": 4, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "XL": 40, "LX": 60, "LXX": 70, "LXXX": 80, "XC": 90, 	"CD": 400, "DC": 600, "DCC": 700, "DCCC": 800, "CM": 900}
	conversionTable.update(irregulars)
	return {b: a for a, b in conversionTable.items()} ## switch keys and values

def convert_to_decimal(roman):
	## roman to decimal
	conversionTable = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
	return [conversionTable[a.upper()] for a in roman if a.upper() in conversionTable]

def convert(x):
	if type(x) == list or type(x) == str:
		return convert_to_decimal(x)
	elif type(x) == int:
		return convert_to_roman(x)

def main(input):
	input = str(input) ## make iterable
	if input.isdigit():	## decimal to roman
		if int(input) > 4000: return False
		value = ""
		digits = [(eval(z + "".join(["0" for x in range(len(input[id:])-1)]))) for id, z in enumerate(input)]
		for i in digits:
			if i in convert(i): value += convert(i)[i]
			elif i/2 in convert(i) and i % 2 == 0: value += convert(i)[i/2]*2
			elif i/3 in convert(i) and i % 3 == 0: value += convert(i)[i/3]*3
		return value
	else: ## roman to decimal
		in_roman = convert(input)[::-1] ## reverse to combat the subtration priciple
		value = in_roman[0] if len(in_roman) > 0 else 0;
		while len(in_roman) > 1:
			a, b = in_roman[0:2]
			if a < b or a == b: value += b ## add if small to big
			elif a > b: value -= b ## subtract if big to small
			del in_roman[0] ## on to the next one
		return value

if __name__ == '__main__':
	if len(argv) < 2 or (type(argv[1]) != int and type(argv[1]) != str):
		show_info()
	else:
		output = main(argv[1])
		if output == False:
			output = "Number too large!"
			print output
			exit(1)
		print output




