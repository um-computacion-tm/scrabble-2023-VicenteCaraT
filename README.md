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
- Make sure you are in the cloned repo:
```
cd scrabble-2023-VicenteCaraT
```
- Inside this repo there is a DockerFile, make sure you have docker installed and run:
```
docker build -t [nombre de la imagen] . 
```
- Then just run it:
```
docker run -it [nombre de la imagen] 
```
- This game runs with pyrae to validate words, so make sure you have internet conection
 
## How to run the test

- Use if you have Coverage:
```
coverage run -m unittest && coverage report -m
```
- For Codeclimate and Coverage
```
. test.sh
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
- Wx3

### Valid word positioning


> [!IMPORTANT]
> If you want to complete words, just put the missing letter to complete it, there is a function that checks connected words with the pyrae dictionary.
> Check the following examples with inputs


- Validation Word 1

![Scrabble Validations - Imgur](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/c48aec46-474f-481a-b76b-7de4a1a3ac10)

 > ***Input: 'CASA', (1, 0), 'H'***    

You can Cross Words, every time you have all the tiles to form the word.'
In this case you need tiles: 'C','A','S','A' in your rack.      
If You dont have a letter to cross a word, you can complete words    

- Validation Word 2

![OJxQi8G - Imgur](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/fccc2b6e-13c1-418a-a268-a4ba2751b666)

You can complete words right and left, and form words with an existing tile

- Validation Word 3

![RkBEUao - Imgur](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/46aa8985-2582-4767-b8b5-58d60841936f)

             
You can complete words up and down, and form words with an existing tile

- Validation Word 4

![Scrabble Validations - Imgur (3)](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/a1f030a0-ce35-4e17-8292-a0287f14dd89)

> ***Input: NI, (2, 1), 'H'***

Formed words = ['EN', 'SI']

Whenever you want to put a word parallel 
horizontal to another you have to form words along 
the entire length, otherwhise you will
not be able to put the word.
You, can put the word up or down.

- Validation Word 5

![Scrabble Validations - Imgur (4)](https://github.com/um-computacion-tm/scrabble-2023-VicenteCaraT/assets/128495271/d674f1a9-d295-4f1b-8902-9205036d74a6)

> ***Input: ASI, (0, 2), 'V'***

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
