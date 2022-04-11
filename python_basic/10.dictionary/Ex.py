def count_word(word):
    frequency = {}
    for i in word:
        frequency[i] = frequency.get(i, 0) + 1
    for word, num in frequency.items():
        print(word ,':', num)
        
def _khoitaokey():
    animals = ["birds","frog"]
    #tạo key mặc định cho 1 từ điển animals có 
    #giá trị là 100
    result = dict.fromkeys(animals,100)
    print("RESULTS:",result)
    print("FROG",result.get("frog"))
    print("?:= ",result.get("?"))
    
if __name__ == '__main__':
    words = 'abcabcdefghi'
    count_word(words)
    # _khoitaokey()