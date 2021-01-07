'''
Code from section 6.5, "Analyzing text", p. 279-287
J. Havill (2016), _Discovering Computer Science_
'''

def find(text, target):
    """Find the index of the first occurrence of target in text.
    
    Parameters:
        text: a string object to search in
        target: a string object to search for
        
    Return value: the index of the first occurrence of target in text
    """
    for index in range(len(text) - len(target) + 1):
        if text[index:index + len(target)] == target:
            return index
    return -1

def concordanceEntry(fileName, word):
    """Print all lines in a file containing the given word.
    
    Parameters:
        fileName: the name of the text file as a string
        word: the word to search for
        
    Return value: None
    """
    text = open(fileName, 'r', encoding = 'utf-8')
    lineCount = 1
    for line in text:
        found = find(line, word)
        if found >= 0:             # found the word in line
            space = ' ' * (80 - len(word) - found)
            print('{0:<6}'.format(lineCount) + space + line.rstrip())
        lineCount = lineCount + 1
    text.close()

def main():
    textFile = open('moby_dick.txt', 'r', encoding = 'utf-8')
    text = textFile.read()
    textFile.close()

    word = input('Search for: ')
    while word != 'q':
        index = find(text, word)
        print(word, 'first appears at position', index)
        word = input('Search for: ')

main()