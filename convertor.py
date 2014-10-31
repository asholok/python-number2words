
import localization

class NumToWord(object):
    def __init__(self, language, currency):
        self._language = language.lower()
        self._currency = currency.lower()
        self._source = localization.languages[self._language]
        self._coins_plural_fem = localization.check_coins_fem(self._currency)
        self._currency_plural_fem = localization.check_currency_fem(self._currency)
        self._lang_family = localization.check_lang_family(self._language)

        self._source(self._currency)

    def __convert_thousand(self, output, last_number):
        output.append(self._source.level[1])
        if last_number == 1:
            output.append(self._source.thousand_endings[0])
        if last_number > 1 and last_number < 5:
            output.append(self._source.thousand_endings[1])
        if last_number >= 5 or last_number == 0:
            output.append(self._source.thousand_endings[2])
    
    def __convert_uper_order(self, output, last_number, lvl):
        output.append(self._source.level[lvl])
        if last_number == 1:
            output.append(self._source.upper_mln_endings[0])
        if last_number > 1 and last_number < 5:
            output.append(self._source.upper_mln_endings[1])
        if last_number >= 5 or last_number == 0:
            output.append(self._source.upper_mln_endings[2])

    def __convert_currency(self, output, last_number):
        output.append(self._source.currency)
        if last_number == 1:
            output.append(self._source.currency_endings[0])
        if last_number > 1 and last_number < 5:
            output.append(self._source.currency_endings[1])
        if last_number >= 5 or last_number == 0:
            output.append(self._source.currency_endings[2])

    def __convert_teens(self, output, last_number, lvl):
        if self._currency_plural_fem and last_number <= 2 and lvl <= 1:
            output.append(self._source.cpecial_case[last_number])
        elif last_number <= 2 and lvl == 1:
            output.append(self._source.cpecial_case[last_number])
        else:
            output.append(self._source.teens[last_number])

    def __convert_whole_part(self, whole, output):
        iter_counter = 0
        
        if self._lang_family == 'rom' and int(whole) == 1:
            output.insert(0, self._source.teens[part]+self._source.currency[:-1])
            return

        while whole:
            converted_part = []
            part = int(whole[-3:])
            hundreds = int(part/100)
            hundred_rest = part%100
            
            if part:
                if hundreds:
                    converted_part.append(self._source.hundreds[hundreds])
                if hundred_rest >= 20:
                    dozens = int(hundred_rest/10)
                    converted_part.append(self._source.dozens[dozens])
                    hundred_rest %= 10
                if hundred_rest:
                    self.__convert_teens(converted_part, hundred_rest, iter_counter)
                if iter_counter >= 2:
                    self.__convert_uper_order(converted_part, hundred_rest, iter_counter)
                if iter_counter == 1:
                    self.__convert_thousand(converted_part, hundred_rest)
                if iter_counter == 0:
                    self.__convert_currency(converted_part, hundred_rest)
                output.insert(0,''.join(converted_part))
            iter_counter += 1
            whole = whole[:-3]

    def __convert_coins_name(self, quantity, output):
        output.append(self._source.coins)
        if quantity == 1:
            output.append(self._source.coins_endings[0])
        if quantity > 1 and quantity < 5:
            output.append(self._source.coins_endings[1])
        if quantity >= 5 or quantity == 0:
            output.append(self._source.coins_endings[2])

    def __convert_coins_part(self, coins, output):
        if len(coins) == 1: #one digit protection (0.5 muts be "fifty" not "five")
            output.append(', '+self._source.dozens[int(coins)])
            output.append(self._source.coins)
            output.append(self._source.coins_endings[2])
            return
        coins = int(coins)
        
        if self._lang_family == 'rom' and coins == 1:
            output.append(', '+self._source.teens[coins]+self._source.coins[:-1])
            return
        
        if coins >= 20:
            dozens = int(coins/10)
            output.append(', '+self._source.dozens[dozens])
            coins %= 10
        if coins:
            if self._coins_plural_fem and coins <= 2:
                output.append(self._source.cpecial_case[coins])
            else:
                output.append(self._source.teens[coins])
        self.__convert_coins_name(coins, output)

    def convert(self, number):
        result = []
        number_array = number.split('.')

        self.__convert_whole_part(number_array[0], result)
        if len(number_array) == 2:
            if number_array[1]:
                self.__convert_coins_part(number_array[1], result)
        return ''.join(result)

if __name__ == '__main__':
    r = NumToWord('eng', 'uah')
    print r.convert('5231451661.01')