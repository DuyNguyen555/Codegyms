def triangle_star():
    i = int(input())
    while True:
        if i == 0:
            break
        else:
            print("*"*i)
            i -= 1
            
def greet(name,counter):
    return f"Hi, {name}!", counter + 1
    
def main():
    # triangle_star()
#    cach 1
    counter = 0
    print(greet("Alice",counter))
    print(f"Counter is {counter}")
    print(greet("Bob",counter))
    print(f"Counter is {counter}")
#    counter = 0
#    greeting,counter = greet("Alice",counter)
#    print(f"{greeting}\n Counter is {counter}")
#    greeting,counter = greet("Bob",counter)
#    print(f"{greeting}\n Counter is {counter}")

if __name__ == '__main__':
    main()