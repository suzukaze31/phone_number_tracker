import pandas as pd


class PhoneNumber:
    def __init__(self, number):
        self.number = number
        self.trimmed_number = number[1:6]

    def check_format(self):
        length = len(self.number) == 10
        is_digit = self.number.isdigit
        return length and is_digit

    def get_address(self):
        outer_list = [self.trimmed_number[:i] for i in range(1, 5)]
        data = pd.read_pickle('phone_numbers_data.pickle')
        result = data[data.outer.isin(outer_list)]
        result = result[result.inner.str.len() == result.inner.str.len().min()]
        address = result['address']
        return list(address)


class SearchJob():
    def __init__(self, value):
        self.phone_number = PhoneNumber(value)

    def search(self):
        if self.phone_number.check_format() is False:
            raise ValueError('Error: Invalid format')

        self.result = self.phone_number.get_address()
        if self.result is None:
            raise ValueError('Error: Not address found')

    def finish(self):
        return self.string_converter(self.result)

    def string_converter(self, result):
        return ''.join(f'{i+1}: {item}\n' for i, item in enumerate(result))
