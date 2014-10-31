import os
import sys
PATH_TO_RULES = '/'.join(str(os.path.abspath(__file__)).split('/')[:-1])+'/languages'
sys.path.insert(0,PATH_TO_RULES)

import languages as langs
from blanck import Blanck

languages = { lang.preffix: Blanck(lang) for lang in langs.lang_list }


def check_coins_fem(val):
	if val in langs.coins_fem:
		return True
	return False

def check_currency_fem(val):
	if val in langs.currency_fem:
		return True
	return False

def check_lang_family(val):
	for family, family_list in langs.family_tab.items():
		if val in family_list:
			return family
#print languages['eng'].hundreds
