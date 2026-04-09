#!/usr/bin/env python

def mapper():
    """
    Reads in a sentence and maps the values.
    Mapping the values means it will give a count of 1 to every word in the sentence.

    Words are defined if there is a space between them.
    """
    #stdin = standard input
    for line in sys.stdin:
        # strip white space at the beginning 
        # and end of the line
        line = line.strip()
        line = line.replace(",", "")
        line = line.replace(".", "")

        #split the line into words
        words = line.split()

        # process each word and assign
        # a value of 1 to each word
        for word in words:
            print(word + "\t1")


if __name__=="__main__":
    mapper()

import sys
def reduce_mapped():

    current_word = None
    # If it set to none, it will be falsey
    current_count = 0
    for line in sys.stdin:
        line = line.strip()
        word, count = line.split("\t", 1)
        count = int(count)

        if current_word == word:
            current_count += count
        
        else:
            # if there is a current word
            # thats is not none and its not
            # the same as the word we're
            # currently on in our iterations
            if current_word:
                print(current_word + "\t" + str(current_word))

            current_count = count
            current_word = word