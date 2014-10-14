import os
import sys
PATH_TO_RULES = '/'.join(str(os.path.abspath(__file__)).split('/')[:-1])+'/languages'
sys.path.insert(0,PATH_TO_RULES)

import languages

languages = {
	'ua': languages.Ua,
	
}


class Plural():
	coins_fem = ['uah', 'rub']
	currency_fem = ['uah']
	
	@staticmethod
	def chek_coins_fem(val):
		if val in Plural.coins_fem:
			return True
		return False

	@staticmethod
	def chek_currency_fem(val):
		if val in Plural.currency_fem:
			return True
		return False
