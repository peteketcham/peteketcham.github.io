#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wordle 'helper'
"""

import re
# from pprint import pprint


def main():
    """
    """
    dict_file = "/usr/share/dict/words"
    valid_wordlist = r"""^[a-z]{5}$"""
    with open(dict_file, 'r') as file:
        words = file.readlines()
    words = [word.rstrip() for word in words if re.search(valid_wordlist, word)]
    # print(len(words))
    while True:
        guess = input("Word guess: ")
        result = input("results (g/y/b): ")
        regex_is = []
        regex_not = []
        
        for index, letter in enumerate(result):
            if letter == "g":
                regex_is.append(r"."*index + fr"{guess[index]}" + r"."*(4 - index))
            elif letter == "y":
                regex_is.append(fr"^.*[{guess[index]}].*")
                regex_not.append(r"."*index + fr"{guess[index]}" + r"."*(4 - index))
            else:
                regex_not.append(fr"{guess[index]}")
        
        for is_is in regex_is:
            words = [word for word in words if re.search(is_is, word)]
        for is_not in regex_not:
            words = [word for word in words if not re.search(is_not, word)]
            
        if len(words) < 40:
            [print(word) for word in words]
        else:
            print(f"{len(words)} words remain")
        
        try:
            _ = input("Press enter to continue, ctrl-c to exit")
        except KeyboardInterrupt as e:
            quit()
            

if __name__ == "__main__":
    main()
