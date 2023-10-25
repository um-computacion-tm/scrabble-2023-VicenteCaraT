from game.scrabbleGame import (ScrabbleGame,)


def main():
    player_count = get_player_count()
    game = ScrabbleGame(player_count)
    while game.is_playing():
        show_board(game.get_board())
        show_player(*game.get_current_player())
        word, coords, orientation = get_inputs()
        try:
            game.play(word, coords, orientation)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()