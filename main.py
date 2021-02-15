from tic_tac_toe_game import setup
from tic_tac_toe_game.play_engine import play



if __name__ == '__main__':
    setup.setup()
    play()
    new_game = input(f'Do you want to play a new game? Y/N : ').lower()
    while new_game == "y":
        play()
        new_game = input(f'Do you want to play a new game? Y/N : ').lower()
    print(f'Game over! The result is:')
    for name, win in setup.game_counter.items():
        print(f'{name}: {win}')
    print('Bye!')

