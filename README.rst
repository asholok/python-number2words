======
README
======

NAME
====

Number2words - form Number to words converter for currencies

SYNOPSIS
========

Common usage::
	from Number2words import converter

	language = 'eng'
	currency = 'usd'
	number = 1342.17 # or string '1342.17'
	conv = converter.NumToWords(language, currency)
	result = conv.convert(number)

Available language and currencies::
	from Number2words import localization

	# dict where key is available language and value is available currenceis
	languages_currencies = localization.available_currenceis

DESCRIPTION
===========
	Before use converter need to find what is languages and currencies available. Number input - Float must be round to at least two digits after sign. Number input - String must contain only one dot(if number not whole), and have no spases or non digits signs(except one dot), and not more than two digits after dot
