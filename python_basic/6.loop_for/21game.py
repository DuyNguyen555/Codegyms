def game():
    from random import randint
    # Giới hạn nhập của người chơi
    limit_number =['1','2','3']
    # Số hiện tại
    current_number = 0
    # Lựa chọn người chơi
    chose_player = int(randint(0,1))
    
    while current_number < 21:
        # Người chơi chọn
        if chose_player == 0:
            player = "human"
            print(f"Player: {player}")
            while True:
                human_number = str((input("Number: ")))
                if human_number in limit_number:
                    break
            current_number += int(human_number)
            # Người chơi chọn xong đến máy chọn 
            chose_player += 1
        else:
            # Máy chọn
            player = "computer"
            computer_number = int(randint(1,3))
            print(f"Player: {player}\nNumber: {computer_number}")
            current_number += computer_number
            # Máy chọn xong đến người chơi chọn
            chose_player -= 1
    else:
        # Kết thúc vòng lập player: Human có biến chose_player = 0, tăng thêm 1 nên điều kiện là = 1
        # Kết thúc vòng lập player: Computer có biến chose_player = 1, giảm xuống 1 nên điều kiện là = 0
        if chose_player == 1:
            print("You lost")
        else:
            print("You win")
        
def main():
    while True:
        game()
        n = input("Play again: Enter 'y' " )
        if n == 'y':
            continue
        else:
            break
        
    
if __name__ == '__main__':
    main()