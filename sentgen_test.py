'''
Purpose: Unit tests for sentgen code
Authors: Andy Exley and Janet Davis
Date:    October 30, 2017
'''
import sentgen as sg

def weighted_select_test():
    dct = {'a': 10}
    assert sg.weighted_select(dct) == 'a'

    dct2 = {'b': 4, 'c': 2, 'd': 1}
    bcount = 0
    ccount = 0
    dcount = 0
    for i in range(8000):
        val = sg.weighted_select(dct2)
        if val == 'b':
            bcount += 1
        elif val == 'c':
            ccount += 1
        elif val == 'd':
            dcount += 1

    # These tests may fail due to extremely bad luck as well as buggy code.
    # If your code is correct, the tests should not fail twice in a row.
    assert 3000 < bcount < 5000, "Should get b about 4000 times"
    assert 1000 < ccount < 3000, "Should get c about 2000 times"
    assert dcount < 2000, "Should get d about 1000 times"
    print('weighted_select tests passed!')

def random_sentence_test():
    bigrams = {'not': {'like': 2}, 'you': {'like': 1}, 'them': {'sam-i-am': 1}, 'i': {'do': 2}, 'do': {'not': 2, 'you': 1}, 'that': {'sam-i-am': 3}, 'ham': {'i': 1}, 'green': {'eggs': 1}, 'like': {'green': 1, 'them': 1, 'that': 1}, 'sam-i-am': {'i': 1, 'do': 1, 'that': 1}, 'eggs': {'and': 1}, 'and': {'ham': 1}}

    sentence = sg.random_sentence(bigrams, 'i', 10)
    words = sentence.split()
    assert len(words) == 10, 'The sentence should be 10 words'
    assert words[0] == 'i', 'The sentence should start with "i"'
    for i in range(1, len(words)):
        previous = words[i-1]
        current = words[i]
        assert current in bigrams[previous], \
            "All bigrams in the sentence should appear in the dictionary"

    print('random_sentence test passed!')

def bigram_count_test():

    dct = sg.bigram_count('test this')
    print(dct)
    assert dct == {'test': {'this': 1}}

    dct2 = sg.bigram_count('red fish blue fish')
    assert dct2['red'] == {'fish': 1}
    assert dct2['fish'] == {'blue': 1}
    assert dct2['blue'] == {'fish': 1}

    dct3 = sg.bigram_count('the the the the')
    assert dct3 == {'the': {'the': 3}}
    
    print('bigram_count tests passed!')

    

def main():
    weighted_select_test()
    bigram_count_test()
    random_sentence_test()

if __name__ == '__main__':
    main()
