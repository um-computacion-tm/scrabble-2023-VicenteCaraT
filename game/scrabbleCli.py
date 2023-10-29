from game.scrabbleGame import ScrabbleGame

class ScrabbleCli():
    def __init__(self):
        self.scrabble = None

    def welcome_message(self):
        print("--------------------------------------------------------------------------------------------")
        print("------------------------------------Welcome to Scrabble------------------------------------")

    def get_player_count(self):
        while True:
            try:
                player_count = int(input("Enter the number of Players (1-3): "))
                if 1 <= player_count <= 3:
                    return player_count
                else:
                    print("Invalid number of players. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def show_game_options(self):
        print("----------------------------------------Scrabble Board-----------------------------------------")
        print(self.scrabble.board)
        print("-------------------------------------------Options---------------------------------------------")
        print("Press 1 to Put Word")
        print("Press 2 to Change your Tiles")
        print("Press 3 to Change all your Tiles")
        print("Press 4 to Pass Turn")
        print("Press 5 to End the Game")
        print("-----------------------------------------------------------------------------------------------")
        print(self.scrabble.get_current_player())

    def get_word_input(self):
        while True:
            word = input("Enter your Word: ").upper()
            if word.isalpha():
                return word
            else:
                print("Invalid word. Please enter alphabetic characters only.")

    def get_coordinates(self):
        while True:
            try:
                x = int(input("Enter your Word pos X: "))
                y = int(input("Enter your Word pos Y: "))
                return x, y
            except ValueError:
                print("Invalid input. Please enter valid numbers for coordinates.")

    def get_orientation(self):
        while True:
            orientation = input("Enter the Word orientation (H/V): ").upper()
            if orientation in ['H', 'V']:
                return orientation
            else:
                print("Invalid orientation. Please enter 'H' for horizontal or 'V' for vertical.")

    def handle_user_input(self, option):
        if option == 1:
            word = self.get_word_input()
            x, y = self.get_coordinates()
            orientation = self.get_orientation()
            if self.scrabble.round <= 2:
                self.scrabble.play_first_round(word, (x, y), orientation)
            else:
                self.scrabble.play(word, (x, y), orientation)
        elif option == 2:
            tiles_to_exchange_indices = input("Enter the indices of tiles you want to exchange (comma-separated): ").split(',')
            old_tiles_indices = [int(index.strip()) for index in tiles_to_exchange_indices]
            exchanged_tiles = self.scrabble.exchange_tiles(old_tiles_indices)
            print("Exchanged tiles: ", exchanged_tiles)
        elif option == 3:
            print('Okay, exchanging all your tiles')
            exchanged_tiles = self.scrabble.exchange_all_tiles()
            print("Exchanged tiles: ", exchanged_tiles)
        elif option == 4:
            print("Well, passing to the next player...")
            self.scrabble.next_turn()
        elif option == 5:
            print('Thanks for playing, bye...')
            exit()
        else:
            print("Incorrect Input. Please try again.")

    def client(self):
        self.welcome_message()
        player_count = self.get_player_count()
        self.scrabble = ScrabbleGame(total_players=player_count)

        while self.scrabble.is_playing():
            self.scrabble.next_turn()
            self.scrabble.start_game()

            while True:
                self.show_game_options()
                option = int(input("Choose your Option: "))
                self.handle_user_input(option)

