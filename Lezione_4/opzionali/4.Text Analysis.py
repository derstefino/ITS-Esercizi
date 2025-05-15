'''
    4. Text Analysis:

    Create a function that takes a paragraph and counts the number of occurrences of each word.
    The function should print a report showing the most frequent words and their number of occurrences.
    You can use a for loop to iterate over the words in the text and a dictionary to store the occurrences.

'''
import re

def word_occ_counter(par:str) -> None:

    list_of_words = re.findall(r"\b[a-zA-Z]+\b", par)

    occurences = {} 

    for word in list_of_words:

        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1

    
    print(occurences)


word_occ_counter("C'era una volta una volta che voltava ogni volta")


