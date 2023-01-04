class translate():
    def __init__(self, dictionary_words):
        """Hàm khai báo"""
        self.dis_words = dictionary_words
    
    def Eng_Viet(self, word):
        """Hàm dịch tiếng Anh sang Việt"""
        if word in self.dis_words:
            print(f"{word} -> Dịch -> {self.dis_words[word]}")
        
    def Viet_Eng(self, word):
        """Hàm dịch tiếng Việt sang Anh"""
        for i in self.dis_words:
            trans = self.dis_words[i]
            if word == trans:
                print(f"{word} -> Translate -> {i}")
                break
        
if __name__ == "__main__":
    dict_words = {
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
    trans = translate(dict_words)
    condition = ["1", "2", "3"]
    while True:
        print("Enter your option by the number:"
              "\n1. English -> Vietnam"
              "\n2. Vietnam -> English"
              "\n3. Exit")
        option = input()
        if option == condition[0]:
            print("Enter your word want to translate:")
            word = input()
            trans.Eng_Viet(word)
        elif option == condition[1]:
            print("Nhập từ bạn muốn dịch:")
            word = input()
            trans.Viet_Eng(word)
        elif option == condition[-1]:
            break