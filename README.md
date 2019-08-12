## Synopsis

The Project is about developing a game called Connect 4 in a row which involves 2 players.
Game Rules:
1. Enter any number between 0-6 based on availability of the block
2. If 4 consecutive blocks of same player matches in a horizonatal line, Player wins
3. If 4 consecutive blocks of same player matches in a vertical line, Player wins
3. If 4 consecutive blocks of same player matches in a diagonal left line, Player wins
4. If 4 consecutive blocks of same player matches in a diagonal right line, Player wins


### Prerequisites

1. Running docker service
2. Requirements file present as requirements.txt file

### Project Structure
game.py - Python script with code related to game connect 4 in a row
README.md - Read me file containing additional description of project
requirements.txt - requirement file which consists of list of python packages required

### Execution Steps
1. Checkout project from github
2. Navigate to directory same as that of Dockerfile
3. Build docker image using following command
docker build -t connect .
4. Execute docker image created using following command
docker run connect
5. Follow the instructions as per messages displayed
