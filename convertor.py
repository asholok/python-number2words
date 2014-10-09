
from localization import languages

class NumToWord(object):
    def __init__(self, language):
        language = language.lower()
        if language not in languages:
            raise Exception('Language is no available')
        self._source = languages[language]

    def __convert_thousand(self, result, last_number):
        result.append(self._source.level[1])
        if last_number == 1:
            result.append(self._source.thousand_endings[0])
        if last_number > 1 and last_number < 5:
            result.append(self._source.thousand_endings[1])
        if last_number >= 5 or last_number == 0:
            result.append(self._source.thousand_endings[2])
    
    def __convert_uper_order(self, result, last_number, lvl):
        result.append(self._source.level[lvl])
        if last_number == 1:
            result.append(self._source.upper_mln_endings[0])
        if last_number > 1 and last_number < 5:
            result.append(self._source.upper_mln_endings[1])
        if last_number >= 5 or last_number == 0:
            result.append(self._source.upper_mln_endings[2])

    def __convert_currency(self, result, last_number):
        result.append(self._source.currency)
        if last_number == 1:
            result.append(self._source.currency_endings[0])
        if last_number > 1 and last_number < 5:
            result.append(self._source.currency_endings[1])
        if last_number >= 5 or last_number == 0:
            result.append(self._source.currency_endings[2])

    def __convert_whole_part(self, whole, output):
        iter_counter = 0

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
                    if hundred_rest <= 2 and iter_counter <= 2:
                        converted_part.append(self._source.cpecial_case[hundred_rest])
                    else:
                        converted_part.append(self._source.teens[hundred_rest])
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
            output.append(self._source.endings[8])
            return
        coins = int(coins)

        if coins >= 20:
            dozens = int(coins/10)
            output.append(', '+self._source.dozens[dozens])
            coins %= 10
        if coins:
            if coins <= 2:
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
    r = NumToWord('ua')
    print r.convert('5233451660.30')