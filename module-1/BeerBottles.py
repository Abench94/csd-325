# Adam Bench
# 03/15/2025
# Assignment 1.3
# A program to sing a song about bottles based on user input.
def main():
  
  again = '1' 
  while (again == '1'):
    # Get the number of bottles from the user.
    valid_bottles = False
    # Validates input.
    while not valid_bottles:
        try:
            bottles = int(input("How many bottles are on the wall? "))
            if isinstance(bottles, (int)):
                valid_bottles = True
        except ValueError:
                print("Please enter a valid number.")
          
    # Initiate while loop to sing the song based on input.          
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.\n"
              f"Take one down, pass it around, {bottles - 1} bottles of beer on the wall.\n")
        bottles -= 1
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.\n"
                  f"Take one down, pass it around, no more bottles of beer on the wall.\n")
    # Remind the user to get more beer now that they are out.  
    print("Time to get more beer!\n")
    # Ask the user if they want to run the program again.
    again = input("Would you like to sing again? (1 for yes, 2 for no) ")
    
# Call the main function.    
if __name__ == "__main__":
    main()
              