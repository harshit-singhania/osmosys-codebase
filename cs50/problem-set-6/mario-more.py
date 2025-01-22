         #                                                                                         
      ##  ##                                                                                        
     ###  ###                                                                                       
    ####  ####                                                                                      
   #####  #####                                                                                     
  ######  ######                                                                                    
 #######  #######                                                                                   
########  ########  

# create this in python 

def print_pyramid(height):
    for i in range(height):
        # Calculate the number of spaces before the hashes
        spaces = ' ' * (height - i - 1)
        # Create the left and right sides of the pyramid
        hashes = '#' * (i + 1)
        # Print the line with spaces and hashes
        print(spaces + hashes + '  ' + hashes)

height = int(input("Height: "))
if 1 <= height <= 8:
    print_pyramid(height)

else:
    print("Enter a number between 1 and 8")
    height = int(input("Height: "))
