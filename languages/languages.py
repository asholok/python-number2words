#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

teens_ua = {1: 'один ', 2: 'двa ', 3 : 'три ', 4: 'чотири ', 5: 'п\'ять ', 6: 'шість ', 7: 'сім ', 8: 'вісім ', 
 9: "дев'ять ", 10: 'десять ', 11: 'одинадцять ', 12: 'дванадцять ', 13: 'тринадцять ', 14: 'чотирнадцять ',
 15: "п'ятнадцять ", 16: 'шістнадцять ', 17: 'сімнадцять ', 18: 'вісімнадцять ', 19: "дев'ятнадцять "}
dozens_ua = {2: 'двадцять ', 3: 'тридцять ', 4: 'сорок ', 5: "п'ятдесят ", 6: 'шістдесят ', 7: 'сімдесят ',
 8: 'вісімдесят ', 9: "дев'яносто "}
hundreds_ua = {1: 'сто ', 2: 'двісті ', 3: 'триста ', 4: 'чотириста ', 5: "п'ятсот ", 6: 'шістсот ', 7: 'сімсот ',
 8: 'вісімсот ', 9: "дев'ятсот "}
cpecial_case_ua = {1: 'одна ', 2: 'дві '}
currency_uah = 'грив'
currency_rub = 'руб'
currency_eur = 'євро'
currency_usd = 'доллар'
coins_ua = 'копій'
coins_cent = 'цент'
level_ua = {1: 'тисяч', 2: 'мільйон', 3: 'мільярд', 4: 'трильйон', 5: 'квадрильйон'}
currency_endings_uah = ['ня', 'ні', 'ень'] 
currency_endings_rub = ['ель', 'лі', 'лів']
currency_endings_eur = ['', '', '']
thousand_endings_ua = ['a ', 'і ', ' ']
upper_mln_endings_ua = [' ', 'и ', 'ів ']
currency_endings_usd = ['', 'и', 'ів']
coins_endings_ua = ['ка ', 'ки ', 'ок ']

CURRENCIES = ['eur', 'rub', 'uah', 'usd']

class Ua(object):
	def __init__(self, currency_value):
		self.teens = teens_ua
		self.dozens = dozens_ua
		self.hundreds = hundreds_ua
		self.cpecial_case = cpecial_case_ua
		self.level = level_ua
		self.thousand_endings = thousand_endings_ua
		self.upper_mln_endings = upper_mln_endings_ua
		
		if currency_value == 'uah':
			self._set_uah()
		if currency_value == 'rub':
			self._set_rub()
		if currency_value == 'eur':
			self._set_eur()
		if currency_value == 'usd':
			self._set_usd()
	
	def _set_uah(self):
		self.currency = currency_uah
		self.currency_endings = currency_endings_uah
		self.coins = coins_ua
		self.coins_endings = coins_endings_ua

	def _set_rub(self):
		self.currency = currency_rub
		self.currency_endings = currency_endings_rub
		self.coins = coins_ua
		self.coins_endings = coins_endings_ua

	def _set_usd(self):
		self.currency = currency_usd
		self.currency_endings = currency_endings_usd
		self.coins = coins_cent
		self.coins_endings = upper_mln_endings_ua

	def _set_eur(self):
		self.currency = currency_eur
		self.currency_endings = currency_endings_eur
		self.coins = coins_cent
		self.coins_endings = upper_mln_endings_ua