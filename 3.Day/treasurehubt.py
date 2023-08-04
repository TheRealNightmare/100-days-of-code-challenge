print('''  _                                              _                    _    _               
 | |                                            | |                  | |  (_)              
 | |_  _ __  ___   __ _  ___  _   _  _ __  ___  | |__   _   _  _ __  | |_  _  _ __    __ _ 
 | __|| '__|/ _ \ / _` |/ __|| | | || '__|/ _ \ | '_ \ | | | || '_ \ | __|| || '_ \  / _` |
 | |_ | |  |  __/| (_| |\__ \| |_| || |  |  __/ | | | || |_| || | | || |_ | || | | || (_| |
  \__||_|   \___| \__,_||___/ \__,_||_|   \___| |_| |_| \__,_||_| |_| \__||_||_| |_| \__, |
                                                                                      __/ |
                                                                                     |___/
''')
      
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")

cmd = input("Your are at a crossroad, whrer you wab to go? {left/right}: ").lower()


if cmd == "left":
    cmd = input("You have come to a lake. There is a n island in the middle of the lake. Type {wait} to wait for a boat. Type {swim} to swim across: ").lower()
    if cmd == "wait":
        cmd = input("You arrived at and island. There is a house with three doors. One red one yellow and one blue. Which color do you choose? {red/blue/yellow}: ").lower()
        if cmd == "red":
            print("Its a room full of fire Game over.")
        elif cmd == "yellow":
            print("You found treasure. You win!")
        elif cmd == "blue":
            print("Its a room full of hyena. Game over!")
    else:
        print("you got attacked by angry trout. Game over!")
else:
    print("Game over!")