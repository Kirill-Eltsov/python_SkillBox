import re
from typing import List

DIGITS = {
    1: "\\.\\!\\?", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs",
    8: "tuv", 9: "wxyz"
}

def my_t9(input_numbers: str) -> List[str]:
    with open('words.txt', 'r') as file:
        words_ = list(filter(lambda x: x, file))
    letters = map(lambda c: "[" + DIGITS[int(c)] + "]", input_numbers)
    regex = "A" + "".join(letters) + "$"
    possible_words = [w.strip() for w in words_ if re.search(regex, w, re.IGNORECASE)]
    return possible_words

if __name__ == '__main__':
    numbers = '22736368'
    words: List[str] = my_t9(numbers)
    print(*words, sep='\n')
