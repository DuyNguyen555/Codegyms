# This work is teacher
def bubbleSort(list):
    for inter_num in range(len(list)-1,0,-1):
        print('Buoc lap thu'+str(inter_num))
        print(list)     
        print('=====')        
        for idx in range(inter_num):
            if list[idx] > list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp
# My work
def bubble_sort(lis):
    n = 0
    for lis_num in range(len(lis), 0, -1):    
        n += 1
        print(f"Buoc lap: ", n)
        for j in range(1, len(lis)):
            i = j - 1
            if lis[i] > lis[j]:
                lis[i], lis[j] = lis [j], lis[i]
    return(lis)

if __name__ == '__main__':
    list_game = [63, 50, 30, 75, 29, 46, 60]
                # 0,  1,  2,  3,  4,  5,  6
    bubble_sort(list_game)    