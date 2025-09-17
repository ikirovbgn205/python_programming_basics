player_one = input()
player_two = input()

player_one_points = 0
player_two_points = 0

while True:
    player_one_card = int(input())
    player_two_card = int(input())

    if player_one_card == 'End of Game':
        print(f'{player_one} has {player_one_points} points')
        print(f'{player_two} has {player_two_points} points')
        break

    elif player_one_card > player_two_card:
        result = player_one_card - player_two_card
        player_one_points += result

    elif player_one_card < player_two_card:
        result = player_two_card - player_one_card
        player_two_points += result

    elif player_one_card == player_two_card:
        print('Number wars')

        player_one_card = int(input())
        player_two_card = int(input())

        if player_one_card > player_two_card:
            print(f'{player_one} is winner with {player_one_points} points')
        elif player_one_card < player_two_card:
            print(f'{player_two} is winner with {player_two_points} points')


