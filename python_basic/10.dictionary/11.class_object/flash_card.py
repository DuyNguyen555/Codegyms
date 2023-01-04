import random

class flashcard:
    def __init__(self):
        self.card = {
            'Con ong': 'bee',
            'Con thỏ': 'rabbit',
            'Con cua': 'crab',
            'Con mèo': 'cat',
            'Con ngựa': 'horse',
            'Con khỉ': 'monkey',
            'Con lừa': 'donkey'
        }
    def quiz(self):
        while True:
            vietnamese, english = random.choice(list(self.card.items()))
            print(vietnamese,":")
            player = input()
            if player.lower() == english:
                print("True")
            else:
                print("False")
            option = int(input("Enter 0 to play continue: "))
            if option != 0:
                break

if __name__ == '__main__':
    fc = flashcard()
    fc.quiz()