# create half pyramid in python 

height = int(input("Height: "))
if 1 <= height <= 8:
    for i in range(height+1): 
        for j in range(1, i+1): 
            print("#", end="")
        print()
else:
    print("Enter a number between 1 and 8")
    height = int(input("Height: "))