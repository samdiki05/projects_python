name = input("Hey type your name: ")
print("Hello " +  name  + " welcome to my game!")

should_we_play  = input(" Do yo want to play? ").lower()

if should_we_play == "y" or should_we_play == "yes":
    print("We are gonna play !")
    #weapon = input("Choice a weapon (sword/axe): ").lower()
    
    direction = input("Do you want to go left or right (left/right): ").lower()
    if direction == "left":
        print("Okay we went left and fell  of a cliff, game over, try again")
    elif direction == "right":
        choice = input ("Okay, you now see a bridge, do you want to swim under it or cross  it ? (swim/cross) ")
        if choice == "swim" : #and weapon == "axe"
            print("You got eaten by an alligator, you die, the end !")
        else:
            print(" You found the gold and won!")
        print("We went right")
    else:
        print("Sorry not a valid reply, you die!")


else:
    print("welcome are not gonna play!")
