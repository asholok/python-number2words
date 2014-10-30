class Blanck(object):
	def __init__(self, root):
		self.root = root
		self.teens = root.teens
		self.dozens = root.dozens
		self.hundreds = root.hundreds
		self.cpecial_case = root.cpecial_case
		self.level = root.level
		self.thousand_endings = root.thousand_endings
		self.upper_mln_endings = root.upper_mln_endings
	
	def __call__(self, currency_value):
		if currency_value == 'uah':
			self._set_uah()
		if currency_value == 'rub':
			self._set_rub()
		if currency_value == 'eur':
			self._set_eur()
		if currency_value == 'usd':
			self._set_usd()
	
	def _set_uah(self):
		self.currency = self.root.currency_uah
		self.currency_endings = self.root.currency_endings_uah
		self.coins = self.root.coins
		self.coins_endings = self.root.coins_endings

	def _set_rub(self):
		self.currency = self.root.currency_rub
		self.currency_endings = self.root.currency_endings_rub
		self.coins = self.root.coins
		self.coins_endings = self.root.coins_endings

	def _set_usd(self):
		self.currency = self.root.currency_usd
		self.currency_endings = self.root.currency_endings_usd
		self.coins = self.root.coins_cent
		self.coins_endings = self.root.upper_mln_endings

	def _set_eur(self):
		self.currency = self.root.currency_eur
		self.currency_endings = self.root.currency_endings_eur
		self.coins = self.root.coins_cent
		self.coins_endings = self.root.upper_mln_endings
