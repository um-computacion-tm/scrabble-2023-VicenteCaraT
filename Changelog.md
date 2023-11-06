# Changelog

## [1.8.0] 5-11-2023

### Changed

- method put() added shuffle, due to other methods
- various modifications in class Board, changed coordinate (x, y) to row and col, due to problems in the validations in method valid_word_in_place(). All functions logic in class Board method changed due to row and col
- handle_user_input in class ScrabbleCli changed due to complexity, now all options has its function
- methods play_first_round() and play() changed due to scores fix
- changed tile repr due to complications with fstrings
- Readme changed

### Added

- added has_jocker and convert_jocker_to_letter in class Player 
- added option 6 and 7 in ScrabbleCli options to convert joker and see all the valid moves in this game
- added varios functions in ScrabbleGame to convert jokers, get_joker_indx(), get_valid_letter_input()


## [1.7.0] 31-10-2023

### Added

- added method find_and_validate_words_adjacent_vertical(), this methids validates words created by putting tow vertical adjacent words

### Changed

- changed method find_and_validate_words_adjacent_horizontal(), reverse the tile when tiles are up

### Fixing

- Still fixing scores and wildcards. 
- all validations for board finished


## [1.6.0] 30-10-2023

### Added

- added method find_and_validate_words_adjacent_horizontal(), this method validates words created by putting tow horizontal adjacent words 

### Working

- working on find_and_validate_words_adjacent_vertical(), scores , wildcards and testing

## [1.5.0] 29-10-2023

### Added

- added method no_tiles_placed(), to see if there are tiles in the position and orientation of the word
- added method has_neighbor_tiles(), to see if tiles are connected
- added method find_and_validate_words_down(), find_and_validate_words_down(), find_and_validate_words_left(), find_and_validate_words_right()
- added get_directions() and is_valid_position(), to verify id directions and positions are valid
- added has_corssword(), to verify if the tiles that cross are the same
- removed refill(), and added get_tiles()
- added show_tiles() (__repr__ for Player)
- added file ScrabbleCli with all the functions to play the game
- added function is_playing()
- added function exchange_tiles() and exchange_all_tiles(), to allow the player to change his tiles
- added round_set(), to give tiles to all the players and refill tiles after a round
- added validate_word_fist_round() and play_first_round(), to verify the position of the fist round
- added get_current_player()
- added testting


### Changed

- valid_word_in_place(), to verify all the posible word connections #FIXING
- changed put_word() due to an error
- changed validate_word
- main()

### Fixing

- find_and_validate_words_adyacent_V(), find_and_validate_words_adyacent_H()
- valid_word_in_place

## [1.4.0] 24-10-2023

### Added

- added new_tiles(), function that allows to the player to exchange tiles
- added game_status(), fist_round_set(),game_over(), get_player_count()
- added more testting 

### Changed

- method is_empty() changed, more simplified 

## [1.3.0] 22-20-2023

### Fixing

- fixing show_board(), with multipliers
- fixing get_multipliers()
- Multipliers list fixed up

### Added

- Added test put_word() in show_board()
- Added test put_word() in show_board() with overlapping multipliers

## [1.2.0] 21-10-2023

### Added

- method is_word_connected() #fixing
- test for put_word(), put_first_word()

### Fixing

- fixing put_fist_word(), show_board(), put_word()

## [1.1.0] 20-10-2023

### Added

- method put_first_word() in class Board
- method refill() in class Player

### Fixing 

- fixing show_board test and method 
- fixing get_multipliers to show the board with all multiplier cells

## [9.0.0] 18-10-2023

### Added

- adding more test for Board()

## [8.0.0] 17-10-2023

### Added 

- added show_board test #fixing

## [7.0.0] 13-10-2023

### Added

- added put_word()

### Changed

- tiles['Ch','LL','RR'] removed


## [6.0.0] 10-10-2023

### Added

- added get_multipliers() #fixing

### Fixing

- fixing has_letter()



## [5.0.0] 07-10-2023

### Added

- added show_board()
- added repr, in class Tile, Square
- added tests por each repr

## [4.0.0] 06-10-2023

### Added

- added method has_letter()
- added method play_tiles()

### Changed

- no log_level dictionary
- calculate_tiles, tiles as instances of Tile


## [3.0.0] 05-10-2023

### Added

- added local codeclimate

### Changed

- Test separated by class
- class board constructor changed

## [2.0.0] 03-10-2023

### Added

- Dictionary added

### Changed
- method validate_word(), changed due to dictionary implementation

## [1.0.0] 28-09-2023

### Fixing

- fixing test (Tile like objetct)
- fixing code

## [0.9.0] 26-09-2023

### Fixing
- validate_word()
- CHANGELOG

## [0.8.0] 25-09-2023

### Fixing

- fixing validate_word()


## [0.7.0] 24-09-2023

### Added 

- added validate_word() 

## [0.6.0] 19-09-2023

### Added

- added main.py

## [0.5.0] 18-09-2023

### Added

- method is_empty()

## [0.4.0] 17-09-2023

### Changed

- complexity reduction in method calculate_score_l_w()

## [0.3.0] 12-09-2023

### Changed

- method word_is_valid() changed 
- method calculate_score_l_w() changed
- atributes from class Square modified 

## [0.2.0] 10-09-2023

### Added

- New method in Board word_is_valid()

## [0.1.0] 09-09-2023

### Added

- Added multiplier active 

## [0.0.9] 06-09-2023

### Added

- New method added in scrabbleGame next_turn

## [0.0.8] 05-09-2023

### Changed

- method calculate_score_l_w() changed, now this method can calculate tiles and words with multipliers
- All socre tests modified 

## [0.0.7] 03-09-2023

### Added

- Added Codeclimate

### Changed

- Separated classes by files

## [0.0.6] 29-08-2023

### Added

- New class ScrabbleGame

## [0.0.5] 27-08-2023

### Added

- New class added Player
- method starting_tiles()

## [0.0.4] 26-08-2023

### Added

- New class added Board
- Added CircleCi and env
- New method in Square add_tile()

## [0.0.3] 21-08-2023

### Added

- New class added Square
- Added method calculate_score() for letter multipliers [DL, TL]
- Test for each multiplier

## [0.0.2] 19-08-2023

### Added

- Added a method called calculate_tiles() to create the amount of tiles the game has
- Test added for the new method
- New attribute total_tiles to sow all the tiles in game

### Changed

- Methods and tests changed due to all new things added

## [0.0.1] 17-08-2023

### Added

- Two classes created Tile and BagTiles
- Methods for BagTile get() and put()
- All letters with each value added