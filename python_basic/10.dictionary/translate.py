def WordInTheSame(word):
    """
    Hàm dùng để loại bỏ các từ giống nhau 
    """
    return sorted(set(word), key=word.index)
    # return sort

def Trans(word):
    # Danh sách từ cho sẵn
    translate ={
        'human'   : 'con người',
        'cat'     : 'con mèo',
        'dog'     : 'con chó',
        'mouse'   : 'con chuột',
        'fish'    : 'con cá',
        'cow'     : 'con bò',
        'monkey'  : 'con khỉ',
        'horse'   : 'con ngựa',
        'zebra'   : 'con ngựa vần',
        'beer'    : 'con gấu',
        'chicken' : 'con gà',
        'lion'    : 'con sư tử',
        'tiger'   : 'con hổ',
        'wolf'    : 'con sói',
        'pig'     : 'con heo',
        'bird'    : 'con chim',
        'duck'    : 'con vịt',
        'deer'    : 'con nai',
    }
    for i in word:
        if i in translate:
            print(i, ':', translate[i])
        else:
            print(i, ':', 'not in the dictionary')

if __name__ == '__main__':

    words = input("Enter the words to be translated: ").split()
    Trans(WordInTheSame(words))