#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility
import random


class ListogramIterator:
   ''' Iterator class for Listogram '''
   def __init__(self, listogram):
       # Team object reference
       self._listogram = listogram
       # member variable to keep track of current index
       self._index = -1
 
   def __next__(self):
       ''''Returns the next item in the listogram '''
       self._index += 1
       if self._index < len(self._listogram):
           return self._listogram[self._index]
       # End of Iteration
       raise StopIteration


class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialize this as a new list
        # Add properties to track useful word counts for this histogram
        self.types = 0  # Count of distinct word types in this histogram
        self.tokens = 0  # Total count of all word tokens in this histogram
        # Count words in given list, if any
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        self.tokens += count
        for index, item in enumerate(self):
            if item[0] == word:
                self[index] = (word, item[1] + count)
                break
        else:
            self.append((word, count))
            self.types += 1



    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for index, item in enumerate(self):
            if item[0] == word:
                return item[1]

        else:
            return 0
    
    def __iter__(self):
        """Overriding iter function"""
        return ListogramIterator(self)
  
                

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        for index, item in enumerate(self):
            if item[0] == word:
                return True
        else:
            return False


    def index_of(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        for index, item in enumerate(self):
            if item[0] == target:
                return index
        else:
            return None



    def sample(self):
        """Return a word from this histogram, randomly sampled by weighting
        each word's probability of being chosen by its observed frequency."""
        random_value = random.randrange(0, self.tokens)

        position = 0

        for index, item in enumerate(self):

            position += item[1]

            if position > random_value:
                return item[0]


def print_histogram(word_list):
    print()
    print('Histogram:')
    print('word list: {}'.format(word_list))
    # Create a listogram and display its contents
    histogram = Listogram(word_list)
    print('listogram: {}'.format(histogram))
    print('{} tokens, {} types'.format(histogram.tokens, histogram.types))
    for word in word_list[-2:]:
        freq = histogram.frequency(word)
        print('{!r} occurs {} times'.format(word, freq))
    print()
    print_histogram_samples(histogram)


def print_histogram_samples(histogram):
    print('Histogram samples:')
    # Sample the histogram 10,000 times and count frequency of results
    samples_list = [histogram.sample() for _ in range(10000)]
    samples_hist = Listogram(samples_list)
    print('samples: {}'.format(samples_hist))
    print()
    print('Sampled frequency and error from observed frequency:')
    header = '| word type | observed freq | sampled freq  |  error  |'
    divider = '-' * len(header)
    print(divider)
    print(header)
    print(divider)
    # Colors for error
    green = '\033[32m'
    yellow = '\033[33m'
    red = '\033[31m'
    reset = '\033[m'
    # Check each word in original histogram
    for word, count in histogram:
        # Calculate word's observed frequency
        observed_freq = count / histogram.tokens
        # Calculate word's sampled frequency
        samples = samples_hist.frequency(word)
        sampled_freq = samples / samples_hist.tokens
        # Calculate error between word's sampled and observed frequency
        error = (sampled_freq - observed_freq) / observed_freq
        color = green if abs(error) < 0.05 else yellow if abs(error) < 0.1 else red
        print('| {!r:<9} '.format(word)
            + '| {:>4} = {:>6.2%} '.format(count, observed_freq)
            + '| {:>4} = {:>6.2%} '.format(samples, sampled_freq)
            + '| {}{:>+7.2%}{} |'.format(color, error, reset))
    print(divider)
    print()


def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument
    if len(arguments) >= 1:
        # Test histogram on given arguments
        print_histogram(arguments)
    else:
        # Test histogram on letters in a word
        word = 'abracadabra'
        print_histogram(list(word))
        # Test histogram on words in a classic book title
        fish_text = 'one fish two fish red fish blue fish'
        print_histogram(fish_text.split())
        # Test histogram on words in a long repetitive sentence
        woodchuck_text = ('how much wood would a wood chuck chuck'
                          ' if a wood chuck could chuck wood')
        print_histogram(woodchuck_text.split())


if __name__ == '__main__':
    main()

    test = Listogram()

    iterator = iter(test)
 
    print(iterator)