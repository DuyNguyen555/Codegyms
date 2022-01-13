def count_word(word):
    frequency = {}
    for i in word:
        frequency[i] = frequency.get(i, 0) + 1
    for word, num in frequency.items():
        print(word ,':', num)

if __name__ == '__main__':
    words = 'abcabcdefghi'
    count_word(words)