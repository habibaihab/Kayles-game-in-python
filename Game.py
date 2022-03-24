lst=int(input("Please, enter the last number of the list : "))
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
empty_list = ['-' for i in range(20)]
player = 1
while True:

    while True:
        n1 = int(input(f"Player{player} How many numbers to remove 1 or 2?"))
        # checking for invalid numbers
        if n1 == 1 or n1 == 2:
            break
        else:
            print("Invalid numbers ")
    if n1 == 1:
        # if the player chosen 1 number
        player1 = int(input(f"player {player} , enter the number"))
        if player1 >= lst :
            print("invalid number")
            continue
        del num_list[player1 - 1]
        # delete the index of the list , if player1 = 5 , delete index 4
        num_list.insert(player1 - 1, "-")
        # go to the index and replace it by '-'
        print(*num_list)
        if num_list == empty_list:
            print(f"Player {player} wins!")
            exit()
            # checking for winning
    elif n1 == 2:
        # if the player chosen 2 numbers
        while True:
            player1 = int(input(f"player {player} , enter first number: "))
            if player1 >= lst:
                print("invalid number")
                continue
            player2 = int(input(f"player {player} , enter second number: "))
            if player2 >= lst:
                print("invalid number")
                continue
            if player1 - player2 == 1 or player1 - player2 == -1:
                break
            else:
                print("Numbers aren't adjacent")
        del num_list[player1 - 1]
        num_list.insert(player1 - 1, '-')
        del num_list[player2 - 1]
        num_list.insert(player2 - 1, '-')
        print(*num_list)
        if num_list == empty_list:
            print(f"Player {player} wins!")
            exit()
    if player == 1:
        player = 2
    elif player == 2:
        player = 1

