# Scrabble

Scrabble is a popular word game where players use letter tiles to create words on a game board. Each letter tile has a point value, and players earn points by forming words. The game involves strategic placement of words on the board to maximize points. Special squares on the board can multiply or increase the word or letter scores. Players use their vocabulary and word-forming skills to compete, making it a game that promotes language abilities and strategic thinking. Scrabble has been enjoyed by players of all ages since its creation in the 1930s.

## How can I run Scrabble?

- First make sure you have Git

- Use:
' sudo apt-get install git '

- Once you have git, clone this repo:
' https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT.git '

- Inside this repo there is a DockerFile, make sure you have docker installed and run:
' docker build -t [nombre de la imagen] . '

- Then just run it:
' docker run -it [nombre de la imagen] '

- This game runs with pyrae to validate words:
' pip install pyrae '

## Game Rules

This game features a 15x15 game board and 104 tiles, each with an assigned score and amount of tiles. 

### Tiles points

- O point: ?
- 1 Point: A, E, I, O, U, L, N, R, S, T
- 2 Points: D, G
- 3 Points: B, C, M, P
- 4 Points: F, H, V, Y
- 5 Points: Q
- 8 Points: J, Ñ, X
- 10 Points: Z


The board has various multipliers placed on several cells, including letter multipliers and word multipliers.

### Types of multipliers:

- Lx2
- Lx3
- Wx2
- wx3

### Valid word positioning

- Validation Word 1

       0     1     2     3  
    ┌─────┬─────┬─────┬─────┐
  0 │     │  P  │     │     │
    ├─────┼─────┼─────┼─────┤
  1 │ (C) │ (A) │ (S) │ (A) │
    ├─────┼─────┼─────┼─────┤
  2 │     │  S  │     │     │
    ├─────┼─────┼─────┼─────┤
  3 │     │  E  │     │     │
    └─────┴─────┴─────┴─────┘
              
You can Cross Words, every time you have all the tiles to form the word.'
In this case you need tiles: 'C','A','S','A' in your rack.      
If You dont have a letter to cross a word, you can complete words    

- Validation Word 2

       0     1     2     3     4     5 
    ┌─────┬─────┬─────┬─────┬─────┬─────┐
  0 │  T  │  R  │  E  │  N  │ (E) │ (S) │
    └─────┴─────┴─────┴─────┴─────┴─────┘
              
       0     1     2     3     4     
    ┌─────┬─────┬─────┬─────┬─────┐
  0 │ (L) │ (A) │  P  │  I  │  Z  │  
    └─────┴─────┴─────┴─────┴─────┘
              
You can complete words right and left.

- Validation Word 3

       0          0
    ┌─────┐    ┌─────┐     
  0 │ (S) │  0 │  S  │
    ├─────┤    ├─────┤
  1 │  O  │  1 │  O  │               
    ├─────┤    ├─────┤
  2 │  L  │  2 │  L  │
    ├─────┤    ├─────┤
  3 │  A  │  3 │ (O) │    
    └─────┘    └─────┘
              
You can complete words up and down.

- Validation Word 4

       0     1     2     
    ┌─────┬─────┬─────┐
  0 │     │     │     │     
    ├─────┼─────┼─────┤
  1 │  M  │  E  │  S  │     
    ├─────┼─────┼─────┤
  2 │     │ (N) │ (I) │     
    ├─────┼─────┼─────┤
  3 │     │     │     │    
    └─────┴─────┴─────┘

Formed words = ['EN', 'SI']

Whenever you want to put a word parallel 
horizontal to another you have to form words along 
the entire length, otherwhise you will
not be able to put the word.
You, can put the word up or down.

- Validation Word 5

       0     1     2     
    ┌─────┬─────┬─────┐
  0 │     │  L  │ (A) │     
    ├─────┼─────┼─────┤
  1 │     │  E  │ (S) │     
    ├─────┼─────┼─────┤
  2 │     │  M  │ (I) │     
    ├─────┼─────┼─────┤
  3 │     │  A  │     │    
    └─────┴─────┴─────┘

Formed words = ['LA', 'ES', 'MI']

Whenever you want to put a word vertically
parallel to another word, you have to 
forms words along the entire lenght,
otherwhise you will not be able to put the word.
You, can tut the word left or right

## Game Process

- To see all the entire development and versions of this proyect, check the Changelog.md


# -Badges-

### -CircleCI Badge Main-
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-VicenteCaraT/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-VicenteCaraT/tree/main)

### -CircleCI Badge Develop-
[![CircleCI](https://dl.circleci.com/status-badge/img/gh/um-computacion-tm/scrabble-2023-VicenteCaraT/tree/develop.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/um-computacion-tm/scrabble-2023-VicenteCaraT/tree/develop)

###  -Maintainability Badge-
[![Maintainability](https://api.codeclimate.com/v1/badges/977dc2087bbf1bbf65a4/maintainability)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-VicenteCaraT/maintainability)

### -Test Coverage Badge-
[![Test Coverage](https://api.codeclimate.com/v1/badges/977dc2087bbf1bbf65a4/test_coverage)](https://codeclimate.com/github/um-computacion-tm/scrabble-2023-VicenteCaraT/test_coverage)

# Autor

- Alumno: Vicente Cara Tapia
- legajo: 
- GitUser: VicenteCaraT
