import math

class line_part:
    kind = word or space
    val = ''

class line:
    def __init__(self, k: int):
        self.max_line_length = k
        self.line_str = ''
        self.words = list()
    def __str__(self):
        extra_spaces_needed = self.max_line_length - self.check_total_length()
        spaces_per_gap = math.floor(extra_spaces_needed / len(self.words)-1)
        leftover_spaces = extra_spaces_needed % len(self.words)-1
        start_adding_leftover_space_from = len(self.words)-1 - leftover_spaces

        return self.line_str
    def check_total_length(self) -> int:
        total_word_count = len(self.words)
        total_char_length = 0
        for w in self.words:
            total_char_length += len(w)
        total_char_length += total_word_count - 1
        return total_char_length

word_list = [
    'The',
    'quick',
    'brown',
    'fox',
    'jumped',
    'over',
    'the',
    'lazy',
    'dog.'
    ]
k = 16

justified = []
line_count = 0

for word in word_list:
    current_line_length = 0
    if len(justified):
        current_line_length = len(justified[line_count])
    if current_line_length + 1 + len(word) <= k:
        justified[line_count] += ' ' + word
    else:
        line_count += 1
        justified[line_count] = word

print(justified)
