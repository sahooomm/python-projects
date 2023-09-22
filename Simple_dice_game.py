import random

def roll():
    min_value = 0
    max_value = 6
    roll_dice = random.randint(min_value,max_value)

    return roll_dice

def player_number():
    while True:
            player = input("Enter the number of players between 2 and 5:")
            if player.isdigit():
                player = int(player)

                if 2 <= player <= 5:
                    
                    break

                else:

                    print("Must be between 2 - 5 players.")

            else:
                print("Invalid input , try again")
    
    return player


def Score():

    players_num = player_number()

    player_score = [ 0 for i in range(players_num)]

    for player in range(players_num):
            
            print("\nplayer number:", player+1 ,"turn has started!\n")
            current_score = 0
            

            while True:
                should_roll = input("would you like to roll (y)? ")
                if should_roll.lower() != "y":
                    break

                value = roll()
                if value == 0:
                    print("You rolled a 0: Your turn done")
                    
                    break
                else:
                    current_score += value
                    print("You rolled a:", value)
                print("Your score is:", current_score)
            player_score[player] += current_score
            print("Your total score is :" , player_score[player])
    return player_score
                


def win():
     
    Score_list = Score()
    size = len(Score_list)
    max_score = max(Score_list)

    for i in range(size):
         if Score_list[i] == max_score:
              print("Player no:",i+1 , "winned the match!")


win()


