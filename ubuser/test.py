def  print_hand(hand, name = 'Guest'):
    print(name + ' picked: ' + hand)

print('Starting the Rock Paper Scissors game!')

player_name = input('Please enter your name: ')

print_hand('Rock', player_name)
