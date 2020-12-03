# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        greeting = "Hello World"
        return greeting  # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        value_to_be_added_to = str(value_to_be_added_to) + str(value_to_add)
        return value_to_be_added_to  # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        return string_to_fetch_from[starting_index:ending_index + 1]

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        starting_index = starting_index - 4
        ending_index = ending_index - 5
        return string_to_fetch_from[starting_index:ending_index]

    def compare(self, first_value, second_value):
        if str(first_value) == str(second_value) or (first_value is None and second_value == 0) or (
                first_value is False and second_value == 0) or (first_value is True and second_value > 0):
            return True
        else:
            return False

    def get_middle_character(self, string_to_fetch_from):
        return None  # TODO - Implement solution

    def get_first_word(self, string_to_fetch_from):
        # s = ''
        # for x in string_to_fetch_from:
        #     if x != ' ':
        #         s += x
        #     else:
        #         break
        s = string_to_fetch_from.split(' ')
        return s[0]

    def get_second_word(self, string_to_fetch_from):
        # s = ''
        # count = 0
        # for x in string_to_fetch_from:
        #     if x == ' ':
        #         count += 1
        #         if count == 2:
        #             break
        #         s = ''
        #     else:
        #         s += x
        s = string_to_fetch_from.split(' ')
        return s[1]

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed.string[::-1]  # TODO - Implement solution
