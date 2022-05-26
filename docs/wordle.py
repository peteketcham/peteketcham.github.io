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
    dict_file = "/usr/share/dict/words" # NOTE: MacOS dict location
    
    valid_wordlist = r"^[a-z]{5}$"
    with open(dict_file, 'r') as file:
        words = [word.rstrip() for word in file if re.search(valid_wordlist, word)]
    
    print("Guess word.  Results are g=green, y=yellow, b=black/no match")
    _ = input("Press ctrl-c to exit at anytime")
    
    try:
        while True:
            guess = input("Word guess: ")
            result = input("Results (g/y/b): ")
            regex_is = []
            regex_not = []
            
            for index, letter in enumerate(result):
                if letter == "g":
                    # Match words that have that exact letter in that exact spot
                    regex_is.append(r"."*index + fr"{guess[index]}" + r"."*(4 - index))
                elif letter == "y":
                    # Match words that have that exact letter, but not in that spot
                    regex_is.append(fr"^.*[{guess[index]}].*")
                    regex_not.append(r"."*index + fr"{guess[index]}" + r"."*(4 - index))
                else:
                    regex_not.append(fr"{guess[index]}")
            
            for is_is in regex_is:
                words = [word for word in words if re.search(is_is, word)]
            for is_not in regex_not:
                words = [word for word in words if not re.search(is_not, word)]
                
            if len(words) < 50:
                [print(word) for word in words]
            else:
                print(f"{len(words)} words remain")
                
    except KeyboardInterrupt as e:
        quit()
            

if __name__ == "__main__":
    main()
