# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:46:48 2023

@author: Olivi
"""

import re
from collections import Counter

excluded_words = ["Summer", "Tropical", "Flamingo", "Pattern"]

def get_word_frequencies(filename):
    word_counter = Counter()
    
    with open(filename, 'r') as file:
        for line in file:
            title = line.strip()
            words = re.findall(r'\b\w+\b', title)
            filtered_words = [word for word in words if word not in excluded_words]
            word_counter.update(filtered_words)
    
    return word_counter

# Example usage
text_file_path = r"D:\easy_diffusion\TODO\TODO_EGYPTIAN_GODDESS\newTitles.txt"
frequencies = get_word_frequencies(text_file_path)

# Print word frequencies in descending order
for word, count in frequencies.most_common():
    print(f"{word}: {count}")




