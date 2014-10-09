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
coins_ua = 'копій'
level_ua = {1: 'тисяч', 2: 'мільйон', 3: 'мільярд', 4: 'трильйон', 5: 'квадрильйон'}
currency_endings_uah = ['ня', 'ні', 'ень'] 
thousand_endings_ua = ['a ', 'і ', ' ']
upper_mln_endings_ua = [' ', 'и ', 'ів ']
coins_endings_ua = ['ка ', 'ки ', 'ок ']

class Ua(object):
	def __init__(self, currency_value):
		if currency_value == 'uah':
			self._set_uah()
		
	def _set_uah(self):
		self.teens = teens_ua
		self.dozens = dozens_ua
		self.hundreds = hundreds_ua
		self.cpecial_case = cpecial_case_ua
		self.currency = currency_uah
		self.coins = coins_ua
		self.level = level_ua
		self.currency_endings = currency_endings_uah
		self.thousand_endings = thousand_endings_ua
		self.upper_mln_endings = upper_mln_endings_ua
		self.coins_endings = coins_endings_ua