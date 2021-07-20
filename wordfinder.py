"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder():

    """
    l/u path to a file, one word per line
    l/u read a file passed in. make attr listing those words
    print out "[num-of-words-read] words read"
     """
    words = []

    def __init__(self, path):
        # read file at the path

        file = open(path)

        # make a list from words in the file
        # save list to attr words
        for x in file:
            str = x.strip('\n')
            if len(str) > 0:
                self.words.append(str)

        # print 'words.len()+words read'
        print(f'{len(self.words)} words read')

    def random(self):
        return random.choice(self.words)

        # def __init__(self, path):
        #     """Read dictionary and reports # items read."""
        #     dict_file = open(path)
        #     self.words = self.parse(dict_file)
        #     print(f"{len(self.words)} words read")
        # def parse(self, dict_file):
        #     """Parse dict_file -> list of words."""
        #     return [w.strip() for w in dict_file]
        # def random(self):
        #     """Return random word."""
        #     return random.choice(self.words)
wf = WordFinder("words.txt")
print()
