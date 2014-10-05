import os
import sys
PATH_TO_RULES = '/'.join(str(os.path.abspath(__file__)).split('/')[:-1])+'/languages'
sys.path.insert(0,PATH_TO_RULES)

import languages

languages = {
	'ua': languages.Ua,
	
}
