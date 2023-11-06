# Scrabble

Scrabble is a popular word game where players use letter tiles to create words on a game board. Each letter tile has a point value, and players earn points by forming words. The game involves strategic placement of words on the board to maximize points. Special squares on the board can multiply or increase the word or letter scores. Players use their vocabulary and word-forming skills to compete, making it a game that promotes language abilities and strategic thinking. Scrabble has been enjoyed by players of all ages since its creation in the 1930s.

## How can I run Scrabble?

- First make sure you have Git

- Use:
```
sudo apt-get install git 
```
- Once you have git, clone this repo:
```
git clone https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT.git 
```
- Inside this repo there is a DockerFile, make sure you have docker installed and run:
```
docker build -t [nombre de la imagen] . 
```
- Make sure you are in the clone repo:
```
cd scrabble-2023-VicenteCaraT
```
- Then just run it:
```
docker run -it [nombre de la imagen] 
```
- This game runs with pyrae to validate words, so make sure you have internet conection
 
## How to run the test

- Use if you have Coverage:
```
coverage run -m unittest $$ coverage report -m
```

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

![Scrabble Validations - Imgur](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/c48aec46-474f-481a-b76b-7de4a1a3ac10)

              
You can Cross Words, every time you have all the tiles to form the word.'
In this case you need tiles: 'C','A','S','A' in your rack.      
If You dont have a letter to cross a word, you can complete words    

- Validation Word 2

![Scrabble Validations - Imgur (1)](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/36222b50-dda7-4e86-b72a-464ff9f3295b)

              
You can complete words right and left.

- Validation Word 3

![Scrabble Validations - Imgur (2)](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/56f2e029-78fb-4d3f-9d0d-9fda7be426cf)

              
You can complete words up and down.

- Validation Word 4

![Scrabble Validations - Imgur (2)](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/9cccaf49-be9a-479d-b9e5-50f312696a82)


Formed words = ['EN', 'SI']

Whenever you want to put a word parallel 
horizontal to another you have to form words along 
the entire length, otherwhise you will
not be able to put the word.
You, can put the word up or down.

- Validation Word 5

![Scrabble Validations - Imgur (4)](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/d674f1a9-d295-4f1b-8902-9205036d74a6)


Formed words = ['LA', 'ES', 'MI']

Whenever you want to put a word vertically
parallel to another word, you have to 
forms words along the entire lenght,
otherwhise you will not be able to put the word.
You, can tut the word left or right

## Game Process

- To see all the entire development and versions of this proyect, check the [Changelog.md](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/blob/develop/Changelog.md)


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
- Legajo: 62089 
- GitUser: VicenteCaraT
